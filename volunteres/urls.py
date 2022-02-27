
from django.urls import path, include

from volunteres.views import list_volunteres


app_name = 'volunteres'

urlpatterns = [
    path('', list_volunteres, name='list')
]

handler404 = 'authentication.views.error'
