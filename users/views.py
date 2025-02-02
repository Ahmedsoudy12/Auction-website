from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib import messages

# function-bases views for the login, logout and signup pages

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            # messages.success(request, "You have successfully logged in!")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, 'login.html')


@login_required
def profile(request):
    if request.method == 'POST':
        # Include request.FILES to handle file uploads
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # Save the form, including the uploaded file
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = CustomUserUpdateForm(instance=request.user)  # Pre-fill the form with the user's current data

    return render(request, 'profile.html', {'form': form, 'user': request.user})


def logout_user(request):
    logout(request)  # Logs out the user
    # messages.success(request, "You have successfully logged out!")
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Save the user instance
            user.gender = form.cleaned_data['gender']
            user.notify_me = form.cleaned_data['notify_me']
            user.save()
            messages.success(request, "Your account has been created successfully!")
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to a page but put in the 'view_function_name'
        else:
            messages.error(request, "Please correct the errors below.")
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
