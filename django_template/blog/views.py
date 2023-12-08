from django.shortcuts import render
def detail(request):
    return render(request, "blog/detail.html")

def home(request):
    return render(request, "blog/bloghome.html")
# Create your views here.
