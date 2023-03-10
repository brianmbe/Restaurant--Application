from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('registeruser')
    else:
        forms = UserForm()

    return render(request, 'userAccount/register_user.html', {
        "forms": forms
    })
