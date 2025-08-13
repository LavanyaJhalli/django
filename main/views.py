from django.http import HttpResponse 
import requests
from django.http import JsonResponse

def hello(request):
    return HttpResponse("Hello World")  

def even_odd(request):
    a=10
    if(a%2==0):
        return HttpResponse("Even")
    else:
        return HttpResponse("Odd")

def get_api_data(request,id):
    url=f'https://jsonplaceholder.typicode.com/posts/{id}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return JsonResponse(data)
    else:
        return  JsonResponse({'error':'failed to fetch data'},status=500)

def json_view(request):
    data={"name":"Lavanya","course":"django"}
    return JsonResponse(data)

def jsonsecond(request,data):
    d={
        "name":"lavanya",
        "course":["django","python","php","laravel"],
        "city":"jalandhar",
    }
    if data in d:
        return JsonResponse({data:d[data]})
    else:
        return HttpResponseNotFound(f"key '{data}' not found.")

def simple_view(request):
    name=request.GET.get('name','guest')
    return HttpResponse(f"Hello {name}!")

def add(request,a,b):
    return HttpResponse(f"adding {a} & {b} gives: {a+b}")

def fname(request,username):
    return HttpResponse(f"Welcome {username}")   

def report(request,date):
    return HttpResponse(f"Report for date: {date}")

def email_url(request,email):
    return HttpResponse(f"user email is: {email}")