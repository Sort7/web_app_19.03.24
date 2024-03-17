from main.views import menu


def get_menu(request):
    return {'upper_menu': menu}