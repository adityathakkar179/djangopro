from django.contrib import admin
from django.urls import path,include
from . import views
from jobpply.views import login_view, register_view, logout_view
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index_main,name='index'),
    path('jobpply/login/', login_view),
    path('jobpply/register/', register_view),
    path('jobpply/logout/', logout_view),
    path('jobpply/reset',views.reset,name='reset'),
    path('^', include('django.contrib.auth.urls'))
    

]