import datetime
from django.http import HttpResponse, HttpResponseNotFound

from blog.models import Blog

from django.shortcuts import render

from django.http import Http404

def current_datetime(request):

    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    # if request == False:
    #     return HttpResponseNotFound("<h1>Page not found</h1>")
    # else:
    #     return HttpResponse("<h1>Page was found</h1>")

    # return HttpResponse(status=201)

    return HttpResponseNotFound("<h1>Page not found</h1>")


def detail(request):
    try:
        p = Blog.objects.get(pk=1)
    except Blog.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "blog/detail.html", {"poll": p})


async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)