from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from . import views


app_name = 'dlapp'

# url patterns 
urlpatterns = [
    path('', views.home, name='home'),
    path('search/',views.search, name='search'),
    path('upload/', views.model_form_upload, name='upload'),
    path('view_pdf/<str:pk>/', views.pdf_view, name='pdf_view'),
    path('download/', views.download, name='download'),
    path('list/', views.holdings_list, name='list'),

   ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
