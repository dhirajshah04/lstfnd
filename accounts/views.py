from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm,\
                    UserEditForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
    )
from .models import Profile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.is_staff = True
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html',
                          {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
            return render(request, 'registration/register.html', {'user_form':user_form})

    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form':user_form})

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password = password)
        login(request, user)
        messages.success(request, 'Logged In sucessfully!')
        return redirect('dashboard')

    return  render(request, "user/login.html", {"form": form, "title":title})

def logout_view(request):
    logout(request)
    return redirect('post_list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the errow below')
            return render(request, 'user/change_password.html', {'form':form})

    else:
        form = PasswordChangeForm(request.user, request.POST)
        return render(request, 'user/change_password.html', {'form': form})


@login_required()
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'user/profile_edit.html',
                            {'user_form': user_form,
                             'profile_form': profile_form})


@login_required()
def profile(request):
    pro_info = Profile.objects.filter(user=request.user)
    return render(request, 'user/profile.html', {'pro_info':pro_info})