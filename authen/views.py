from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
def index(request):
    return render(request,'index.html')

User = get_user_model()

from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        nid = request.POST.get('nid')
        profile_picture = request.FILES.get('profile_picture')  # Get the uploaded profile picture file

        # Check if the username is unique
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists')
            return render(request, 'signup.html')

        # Check if the user with the provided email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists')
            return render(request, 'signup.html')

        # Check if the NID is unique
        if User.objects.filter(nid=nid).exists():
            messages.error(request, 'User with this NID already exists')
            return render(request, 'signup.html')
        
        #Passwords don't match, handle the error
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        
        # Create a new user object
        user = User(email=email, username=username, phone=phone, nid=nid)

        # Set the profile picture if it was provided
        if profile_picture:
            user.profile_picture = profile_picture

        user.password = make_password(password1)
        user.save()

        # Optionally, log in the user after sign up
        # You can use Django's built-in login function
        # login(request, user)

        # Redirect to a success page or any other desired page
        messages.success(request,"Successfully Signed Up!")
        return redirect('auth_login')

    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone')
        password = request.POST.get('password')

        # Check if the user exists with the provided email or phone number
        user = None
        try:
            user = User.objects.get(email=email_or_phone)
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone=email_or_phone)
            except User.DoesNotExist:
                pass

        if user is not None:
            # User found, authenticate with the provided password
            authenticated_user = authenticate(request, username=user.email, password=password)
            if authenticated_user is not None:
                # Authentication successful, log in the user
                login(request, authenticated_user)
                return redirect('index')
        
        # Authentication failed, display an error message
        messages.error(request, 'Invalid email/phone number or password')

    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('auth_login')