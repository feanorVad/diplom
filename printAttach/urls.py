from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
#from rest_framework import routers


from account import views as acc_views


from workplace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',
         views.Index,
         name='index'),

    path(
        'abonents/',
        views.AbonListView.as_view(),
        name='abonents-list'
    ),
    path(
        'abonents/<int:pk>/',
        views.AbonentDetailView.as_view(),
        name='abonents-detail'
    ),
    path(
        'abonents/<int:pk>/update/',
        views.AbonentUpdateView.as_view(),
        name='abonents-update'
    ),
    path(
        'abonents/create/',
        views.AbonentCreateView.as_view(),
        name='abonents-create'
    ),
    path(
        'abonents/<int:pk>/delete/',
        views.AbonentDeleteView.as_view(),
        name='abonents-delete'
    ),
    path(
        'tarifs/',
        views.TarifListView.as_view(),
        name='tarifs-list'
    ),
    path(
        'tarifs/<int:pk>/',
        views.TarifDetailView.as_view(),
        name='tarifs-detail'
    ),
    path(
        'tarifs/<int:pk>/update/',
        views.TarifUpdateView.as_view(),
        name='tarifs-update'
    ),
    path(
        'tarifs/create/',
        views.TarifCreateView.as_view(),
        name='tarifs-create'
    ),
    path(
        'tarifs/<int:pk>/delete/',
        views.TarifDeleteView.as_view(),
        name='tarifs-delete'
    ),
    ]
