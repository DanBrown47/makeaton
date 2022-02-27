from django.contrib import admin
from django.urls import path, include
from django.shortcuts import s
from django.views.generic import TemplateView
import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('success/', TemplateView.as_view(template_name='success.html')),
    path('starter/', TemplateView.as_view(template_name='starter.html'), name='starter'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('tokens/', include('tokens.urls', namespace='tokens')),
    path('volunteres/', include('volunteres.urls', namespace='volunteres')),

]

handler404 = 'authentication.views.error'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
