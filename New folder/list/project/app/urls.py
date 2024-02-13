from django.urls import path,views

urlpatterns = [
    path(''),
    path('',views.index,name='index')
]