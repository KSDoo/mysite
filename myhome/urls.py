from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('new/', views.new, name='new'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
