from django.db import models
from django.urls import reverse

class VacancyStatus(models.TextChoices):
    """Статусы для вакансий"""
    NEW = 'NEW', 'Новая вакансия'
    STUDENT_APPLIED = 'STUDENT_APPLIED', 'Заявка студента создана'
    UNDER_REVIEW = 'UNDER_REVIEW', 'Заявка на рассмотрении подразделения'
    INTERVIEW_SCHEDULED = 'INTERVIEW_SCHEDULED', 'Ожидает собеседования'
    INTERVIEW_STAGE = 'INTERVIEW_STAGE', 'На стадии собеседования'
    CLOSED = 'CLOSED', 'Вакансия закрыта'

class Vacancy(models.Model):
    """Модель вакансии"""

    hr = models.ForeignKey(
        "users.User", related_name="created_vacancies",
        verbose_name="HR, создавший вакансию", on_delete=models.CASCADE
    )
    description = models.TextField(verbose_name="Описание вакансии")
    requirements = models.TextField(verbose_name="Требования к кандидатам")
    deadline = models.DateField(verbose_name="Срок подачи заявок", null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=VacancyStatus.choices,
        default=VacancyStatus.NEW,
        verbose_name="Статус вакансии"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активна ли вакансия"
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return f"Вакансия - {self.id}, статус - {self.status}"

    def get_absolute_url(self):
        return reverse("vacancies:detail", kwargs={"pk": self.pk})

    def deactivate(self):
        """Деактивировать вакансию"""
        self.is_active = False
        self.save()

class Application(models.Model):
    """Модель заявки студента на вакансию"""

    student = models.ForeignKey(
        "users.User", related_name="applications",
        verbose_name="Студент", on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        Vacancy, related_name="applications",
        verbose_name="Вакансия", on_delete=models.CASCADE
    )
    cover_letter = models.TextField(verbose_name="Сопроводительное сообщение")
    resume = models.FileField(upload_to="resumes/", verbose_name="Резюме")
    preferred_start_date = models.DateField(
        verbose_name="Предпочтительная дата начала работы", null=True, blank=True
    )
    interview_date = models.DateTimeField(
        verbose_name="Дата и время собеседования", null=True, blank=True
    )
    interview_location = models.CharField(
        max_length=255, verbose_name="Место проведения собеседования", null=True, blank=True
    )
    interview_link = models.URLField(
        verbose_name="Ссылка для онлайн-встречи", null=True, blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=VacancyStatus.choices,
        default=VacancyStatus.STUDENT_APPLIED,
        verbose_name="Статус заявки"
    )

    class Meta:
        verbose_name = "Заявка на вакансию"
        verbose_name_plural = "Заявки на вакансии"

    def __str__(self):
        return f"Заявка от {self.student} на вакансию {self.vacancy}"

    def get_absolute_url(self):
        return reverse("applications:detail", kwargs={"pk": self.pk})
