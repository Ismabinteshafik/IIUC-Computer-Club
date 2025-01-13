from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('team/', views.team_view, name='team'),
    path('signin/', views.login_view, name='signin'), 
    path('signin/', views.signup, name='signin'),  # Ensure this matches the login URL
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)