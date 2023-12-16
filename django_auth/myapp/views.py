from django.shortcuts import render

def my_view(request):
    # ...
    return render(request, 'my_template.html', {'login_url': 'login', 'logout_url': 'logout'})
