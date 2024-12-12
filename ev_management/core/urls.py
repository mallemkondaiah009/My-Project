from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('centers/', views.nearby_centers, name='nearby_centers'),
    path('book-slot/<int:center_id>/', views.book_slot, name='book_slot'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment_page'),
    path('dashboard/<int:payment_id>/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('', RedirectView.as_view(url='/register/', permanent=True), name='root'),
]
