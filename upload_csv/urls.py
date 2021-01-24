from django.urls import path
from . import views


urlpatterns = [
    #path('', views.home,name='home'),
    path('', views.upload,name='upload'),
    path('datatable',views.datatable,name='datatable')
]
