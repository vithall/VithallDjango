"""
Definition of urls for VithallDjango.
"""

from datetime import datetime
from re import template
from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('app/<int:id>/detail',views.detail,name='detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('delete/', views.delete, name='delete'),
    path('add/', views.add, name='add'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': "用户登录",
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(
        template_name='app/loggedoff.html',
        next_page='/'
        ),
        name='logout'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
