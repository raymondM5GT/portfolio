from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),

    path('project/<str:pk>', views.projectPage, name='project'),
    path('add-project/', views.addProject, name='addProject'),
    path('edit-project/<str:pk>', views.editProject, name='editProject'),

    path('inbox/', views.inboxPage, name='inbox'),
    path('message/<str:pk>', views.messagePage, name='message'),

    path('add-skill/', views.addskill, name='add-skill'),
    
    path('add-endorsement/', views.addEndorsement, name='add-endorsement'),


]
