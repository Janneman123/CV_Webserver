from django.urls import path
from . import views
# froo django.urls import include

urlpatterns=[
path('',views.index,name="index")]