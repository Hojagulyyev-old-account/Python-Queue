from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('example/', views.ExampleView.as_view(), name='example'),
    path('change_queue/<str:time>/<int:id>/<str:date>/', views.change_queue, name='change_queue'),
]
