from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponsePermanentRedirect
from .forms import RegistrationForm, LoginForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return HttpResponsePermanentRedirect(reverse('crowdfunding:crowdfunding'))
                    # return render(request, 'login/success.html', {})
                else:
                    return render(request, 'login/login_and_registration.html', {'not_valid_user':True})
        else:
            if request.POST.get('type') == 'register':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password'],
                    )
                    return HttpResponsePermanentRedirect(reverse('crowdfunding:crowdfunding'))
                    # return render(request, 'login/success.html', {'user':user})
    else:
        if request.user.is_authenticated():
            return HttpResponsePermanentRedirect(reverse('crowdfunding:crowdfunding'))
            # return render(request, 'login/success.html', {})
        else:
            return render(request, 'login/login_and_registration.html', {})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)