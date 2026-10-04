from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Static HTML content served by Django
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/', include('restaurant.urls')),
    # User registration and authentication (Djoser)
    path('api/registration/', include('djoser.urls')),
    path('api/registration/', include('djoser.urls.authtoken')),
    # Convenience token endpoints: /api/token/login/ and /api/token/logout/
    path('api/', include('djoser.urls.authtoken')),
]
