from django.urls import path,re_path
from main import views

urlpatterns = [
    path('', views.hello),
    path('cal',views.even_odd),
    path('api/<int:id>',views.get_api_data),
    path('json-data',views.json_view),
    path('json-d/<data>',views.jsonsecond),
    path('welcome/',views.simple_view),
    path('url/<int:a>/<int:b>',views.add),
    re_path(r'^welcome/(?P<username>[a-zA-Z0-9_#@]+)/$', views.fname),
    re_path(r'date/(?P<date>\d{4}-\d{2}-\d{2})/$',views.report),
    re_path(r'^user123/(?P<email>[a-zA-Z0-0.%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,})/$',views.email_url)
]
