from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CustomUser
def welcome(request):
    return render(request, 'main.html')

def about_view(request):
    return render(request, 'club/about.html')

def services_view(request):
    return render(request, 'club/services.html')


def team_view(request):
    return render(request, 'club/team.html')


def tasks(request):
    return render(request, 'tasks.html')

# List of valid executive member IDs
EXECUTIVE_MEMBER_IDS = ["EX123", "EX456", "EX789"]  # Add all valid IDs here.

# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST['txt']
        email = request.POST['email']
        password = request.POST['pswd']
        executive_id = request.POST['id']

        # Validate executive ID
        if executive_id not in EXECUTIVE_MEMBER_IDS:
            return render(request, 'signin.html', {
                'error': 'Invalid Executive ID. Contact Admin for Assistance.'
            })

        # Create the user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            executive_id=executive_id,
            is_executive=True
        )
        return redirect('login')  # Redirect to login after signup

    return render(request, 'signin.html')

# Login view
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['pswd']
#         executive_id = request.POST['id']

#         user = authenticate(request, username=email, password=password)

#         # Check if the user exists and is an executive member
#         if user is not None and user.is_executive and user.executive_id == executive_id:
#             login(request, user)
#             return render(request, 'main.html', {
#                 'message': 'You logged in as Executive Member.'
#             })
#         else:
#             return render(request, 'signin.html', {
#                 'error': 'Invalid credentials or not an Executive Member.'
#             })

#     return render(request, 'signin.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']
        executive_id = request.POST['id']

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_executive and user.executive_id == executive_id:
            login(request, user)
            return render(request, 'main.html', {'message': 'You logged in as Executive Member.'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials or not an Executive Member.'})

    return render(request, 'signin.html')  # Rendering the signin.html template
