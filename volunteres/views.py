from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()
# Create your views here.


@login_required
def list_volunteres(request):
    volunteres = User.objects.filter(is_voluntere=True)

    return render(request, 'volunteres/list.html', {'volunteres': volunteres})
