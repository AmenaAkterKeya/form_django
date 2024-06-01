from django.urls import path
from . import views
urlpatterns = [
    path('',views.myModel,name='myModel'),
]
