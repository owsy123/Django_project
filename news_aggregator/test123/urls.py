from django.urls import path
from . import views

urlpatterns = [
    path('news',views.index,name='Index'),
    path('news/favourite',views.favourite,name='Favourite')

]

