from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='bookings')

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
]
