from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/new/', views.entry_new, name='entry_new'),
    path('entry/<int:pk>/edit/', views.entry_edit, name='entry_edit'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),
    path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]