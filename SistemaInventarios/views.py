from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    return render(request,'index.html')

@csrf_exempt
def UsuarioInicioSesion(request):
    return render(request, 'Login.html')

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            return render(request, 'Login.html', {'error_message': 'Invalid login'})
    else:
        return redirect('login')

@csrf_exempt
@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login')