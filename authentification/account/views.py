from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from user_agents import parse
# Create your views here.

def sing_in(request):

    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('dashboard')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'login.html', {})

def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('sing_in')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'register.html', context)

# def get_mac_version(request) -> str:
#     user_agent_string = request.headers.get('User-Agent')
#     user_agent = parse(user_agent_string)
#     if user_agent.os.family == 'Mac OS X':
#         return user_agent.os.version_string
#     else:
#         return 'Unknown'
    
@login_required(login_url='sing_in')
def dashboard(request):
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    device_type = ''
    if user_agent.os.family == 'iOS' or user_agent.os.family == 'Mac':
        return render(request, 'admin.html',  {})
    else:
        device_type = 'Desktop device'
    context = {'device_type': device_type}
    print(context)
    if device_type == 'Desktop device':
        # Show the captcha form for other devices
        if request.method == 'GET':
            # Check the captcha
            captcha_response = request.POST.get('captcha-response') #*****
            print('captchaa',captcha_response)
            if captcha_response:
                # If the captcha is validated, redirect to dashboard
                return redirect('dashboard') #*****
            else:
                context['error'] = True
                context['message'] = 'Please complete the captcha'
        return render(request, 'captcha.html', context)

def admin_d(request):
    return render(request, 'admin.html')

def log_out(request):
    logout(request)
    return redirect('sing_in')