from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('breeds/', views.breed_list, name='breed_list'),
    path('breeds/update/<int:pk>/', views.breed_update, name='breed_update'),
    path('breeds/delete/<int:pk>/', views.breed_delete, name='breed_delete'),

    path('feedtypes/', views.feedtype_list, name='feedtype_list'),
    path('feedtypes/update/<int:pk>/', views.feedtype_update, name='feedtype_update'),
    path('feedtypes/delete/<int:pk>/', views.feedtype_delete, name='feedtype_delete'),

    path('medicationdrugs/', views.medicationdrug_list, name='medicationdrug_list'),
    path('medicationdrugs/update/<int:pk>/', views.medicationdrug_update, name='medicationdrug_update'),
    path('medicationdrugs/delete/<int:pk>/', views.medicationdrug_delete, name='medicationdrug_delete'),

    path('feedingrecords/', views.feedingrecord_list, name='feedingrecord_list'),
    path('feedingrecords/update/<int:pk>/', views.feedingrecord_update, name='feedingrecord_update'),
    path('feedingrecords/delete/<int:pk>/', views.feedingrecord_delete, name='feedingrecord_delete'),
]
