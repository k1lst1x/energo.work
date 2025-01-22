from django.shortcuts import render
from django.utils.translation import activate, get_language


def main(request):
    lang = request.GET.get('lang', 'ru')
    if lang not in ['en', 'ru', 'kz']:  # Проверка допустимости языка
        lang = 'en'  # Если нет, используем английский
    activate(lang)  # Переключаем язык
    
    # Отображаем шаблон с текущим языком
    return render(request, 'vacancies/main.html', {'current_language': lang})