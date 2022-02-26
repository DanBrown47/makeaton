from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('success/', TemplateView.as_view(template_name='success.html')),
    path('starter/', TemplateView.as_view(template_name='starter.html'), name='starter'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('tokens/', include('tokens.urls', namespace='tokens')),
]
