from django.http import HttpResponse


def show_main_page(request):
    return HttpResponse('Здесь будет карта')
