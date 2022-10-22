from django.contrib import admin
from django.urls import path
from firereport.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',index,name='index'),
    path('admin-login/',admin_login,name='admin-login'),
    path('dashboard/',dashboard,name='dashboard'),

    path('add-team/',add_team,name='add-team'),
    path('manage-team/',manage_team,name='manage-team'),

]
