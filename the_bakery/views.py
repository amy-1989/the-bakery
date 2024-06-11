from django.shortcuts import render

def handler404(request, exception):
    """ Renders a custom 404 error page"""
    return render(request, "errors/404.html", status=404)


def handler500 (request):
    """Renders a custom 500 error page"""
    return render(request, "errors/500.html", status=500)

