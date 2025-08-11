from django.urls import path
from main import views

urlpatterns = [
    path('', views.hello),
    path('cal',views.even_odd),
    path('api/<int:id>',views.get_api_data),
    path('json-data',views.json_view),
    path('json-d/<data>',views.jsonsecond),
    path('welcome/',views.simple_view),
    path('url/<int:a>/<int:b>',views.add),
]
