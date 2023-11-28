from django.urls import path
from . import views
from .views import (
    SubjectListView, 
    SubjectDetailView, 
    SubjectCreateView, 
    SubjectUpdateView, 
    SubjectDeleteView
)

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
]
