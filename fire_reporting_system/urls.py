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
    path('edit-team/<int:pid>/',edit_team,name='edit-team'),
    path('delete-team/<int:pid>/',delete_team,name='delete-team'),

    path('reporting/',reporting,name='reporting'),

    path('new-request/',new_request,name='new-request'),

]
