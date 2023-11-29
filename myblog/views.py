from django.http import  HttpResponse
from django.template.loader import render_to_string

def index(request): 
    content = render_to_string("myblog/index.html")
    return HttpResponse(content)

