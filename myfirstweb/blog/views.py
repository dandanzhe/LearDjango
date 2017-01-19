from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

# Create your views here.

def hello(request):
    return HttpResponse('<html>hello world</html>')

def current_datatime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body><html>" % now
    return HttpResponse(html)



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def sum_n(request,n):
    try:
        n = int(n)
    except ValueError:
        raise Http404()
    num=sum(xrange(n+1))
    html="<html><body>sum(1-n)=%s</body></html>"%num
    return HttpResponse(html)


def love(request,name):
    try:
        name=str(name)
    except ValueError:
        raise Http404()
    html="<html><body>I Love %s</body></html>"%name
    return HttpResponse(html)

def hhhh(request):
    t = get_template('hello.html')
    html = t.render(Context({'name': "fuxiaodan"}))
    return HttpResponse(html)


def httprendertoresponse(request):
    return render_to_response('search_form.html')