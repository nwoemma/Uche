from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import UserRegistrationForm, UserLoginForm, ProfileCompletionForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.forms import SetPasswordForm  

# Create your views here.
def header_view(request, page_name):
    titles = {
        'register':"Tasty - Register Here",
        'authenticated_home':"Tasty - Home",
        'about': 'Tasty - About Us',
        'gallery':'Tasty - Our Gallery',
        'menu':'Tasty - Our Menu',
        'contact':'Tasty - Contact Us',
        'reservation':"Tasty - Our Reservation",   
        'login': "Tasty - Login"
    }
    titles.get(page_name,"Default titles")
    return render(request, f"{page_name}.html", {"page_titles":titles})

def register(request):  
    print("🟢 Entering register view")  # ✅ Debugging line

    form = UserRegistrationForm()  
    if request.method == "POST":  
        print("📝 Processing registration form submission")  # ✅ Debugging line

        form = UserRegistrationForm(request.POST)  
        if form.is_valid():  
            print("✅ Form is valid, creating user")  # ✅ Debugging line

            user = form.save(commit=False)  
            user.set_unusable_password()  # Prevent login until password is set  
            user.save()  
            
            request.session["temp_user_id"] = user.id  # ✅ Store user ID in session  
            print(f"📌 Stored user_id in session: {user.id}")  # ✅ Debugging line

            messages.success(request, "Registration successful! Set your password now.")  
            return redirect("users:set_password")  # 🔥 No need for user_id in URL  
        
        else:
            print(f"❌ Form errors: {form.errors.as_json()}")  # ✅ Debugging line
            messages.error(request, "There were errors in the form. Please correct them.")

    print("👀 Rendering registration form")  # ✅ Debugging line
    return render(request, "users/register.html", {"form": form, "page_title": "Tasty - Register Here"})


def set_password(request):
    print("🟢 Entering set_password view")  # ✅ Debugging: Entry log

    user_id = request.session.get("temp_user_id")  # ✅ Retrieve user_id from session
    print(f"🔍 Retrieved user_id from session: {user_id}")  # ✅ Debugging: Check retrieved user_id

    if not user_id:
        print("❌ Error: No user_id found in session!")  # ✅ Debugging: No user_id case
        messages.error(request, "No user ID found! Please register again.")
        return redirect("users:register")  # 🔥 Redirect to registration if missing
    
    # Ensure user exists
    try:
        user = User.objects.get(id=user_id)
        print(f"✅ User found: {user}")  # ✅ Debugging: User found
    except User.DoesNotExist:
        print("❌ Error: User not found in database!")  # ✅ Debugging: User not found
        messages.error(request, "User not found! Please register again.")
        return redirect("users:register")

    if request.method == "POST":
        print("📝 Processing password form submission")  # ✅ Debugging: Form submission start
        form = SetPasswordForm(user, request.POST)
        
        if form.is_valid():
            print("✅ Form is valid, saving new password")  # ✅ Debugging: Form validation success
            form.save()
            messages.success(request, "Password set successfully! Complete your profile now.")
            print(f"➡️ Redirecting to complete_profile for user_id: {user.id}")  # ✅ Debugging: Redirect log
            return redirect("users:complete_profile", user_id=user.id)
        else:
            print(f"❌ Form errors: {form.errors}")  # ✅ Debugging: Form validation failure
    
    else:
        print("👀 Rendering password form")  # ✅ Debugging: Rendering form
        form = SetPasswordForm(user)

    return render(request, "users/set_password.html", {"form": form})



def complete_profile(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = ProfileCompletionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile completed! You can now log in.")
            return redirect("users:login_user")
    else:
        form = ProfileCompletionForm(instance=user)
    return render(request, "users/complete_profile.html", {"form": form})

def login_user(request):
    print("🟢 Entering login_user view")  # ✅ Debugging: Entering the function
    
    if request.method == "POST":
        print("📝 Processing login form submission")  # ✅ Debugging: Detecting POST request
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"📌 Received username: {username}")  # ✅ Debugging: Checking received username

        user = authenticate(username=username, password=password)
        if user is not None:
            print(f"✅ Authentication successful for user: {username}")  # ✅ Debugging: Successful login
            login(request, user)
            messages.success(request, f"Hello {username}! You have been logged in")
            return redirect("pages:home")
        
        print("❌ Authentication failed: Invalid username or password")  # ✅ Debugging: Failed login
        messages.error(request, "Login failed. Please check your username and password.")

    print("👀 Rendering login page")  # ✅ Debugging: Rendering login page
    return render(request, 'users/login_user.html', {"page_title": "Tasty - Login "})

