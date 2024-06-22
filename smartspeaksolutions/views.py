from django.shortcuts import render


def custom_404_view(request, exception):
    """ 
    Http Error Handler 404 - Page Not Found 
    """
    return render(request, "error/404.html", status=404)


def custom_500_view(request):
    """ 
    Http Error Handler 500 - Internal Server Error 
    """
    return render(request, "error/500.html", status=500)


def custom_403_view(request, exception):
    """ 
    Http Error Handler 403 - Forbidden Error 
    """
    return render(request, "error/403.html", status=403)

def blog(request):
    return render(request, 'blog.htm', {})