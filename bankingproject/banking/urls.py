from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from banking import views

app_name = 'banking'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('blank/', views.blank, name='blank'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)