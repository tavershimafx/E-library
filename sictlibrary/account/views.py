from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Account is disabled')
        else:
            return HttpResponse('Invalid login credentials')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})


def register_user(request):
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new user object but don't save it just yet
            new_user = user_form.save(commit=False)
            # set the chosen password - for hashing, security
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            context = {'new_user':new_user}
            return render(request, 'account/register_done.html', context)
    else:
        form=UserRegistrationForm()
        context = {'form': form}
        # context = {'user_form':user_form}
    return render(request, 'account/register.html', context ) # {'form':form}



#view for login Authentication
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})
