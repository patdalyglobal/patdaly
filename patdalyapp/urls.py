from patdalyapp import views
from django.urls import path
from .views import project_list, project_detail, project_create, project_edit, project_delete, contractor_list, \
    contractor_detail, contractor_create, contractor_edit, contractor_delete, supervisor_list, supervisor_detail, \
    supervisor_create, supervisor_edit, supervisor_delete

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('services/web/', views.web, name='web'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),

    # ----------- Plateau State Budget and Planning -------------#

    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/new/', project_create, name='project_create'),
    path('projects/<int:pk>/edit/', project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', project_delete, name='project_delete'),

    path('contractors/', contractor_list, name='contractor_list'),
    path('contractors/<int:pk>/', contractor_detail, name='contractor_detail'),
    path('contractors/new/', contractor_create, name='contractor_create'),
    path('contractors/<int:pk>/edit/', contractor_edit, name='contractor_edit'),
    path('contractors/<int:pk>/delete/', contractor_delete, name='contractor_delete'),

    path('supervisors/', supervisor_list, name='supervisor_list'),
    path('supervisors/<int:pk>/', supervisor_detail, name='supervisor_detail'),
    path('supervisors/new/', supervisor_create, name='supervisor_create'),
    path('supervisors/<int:pk>/edit/', supervisor_edit, name='supervisor_edit'),
    path('supervisors/<int:pk>/delete/', supervisor_delete, name='supervisor_delete'),
]
