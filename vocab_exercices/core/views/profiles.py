from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    # create_profile(None)
    # return redirect('home')
    print("------ at home : ", request.user)
    if not request.user.is_authenticated:
        print("------ going to log_in : ", request.user)
        # return render(request, 'essentials/base.html')
        return redirect('log_in')
    if request.user.is_etudiant:
        print("------ going to etudiant")
        return redirect('etudiant')
    if request.user.is_enseignant:
        print("------ going to enseignant")
        return redirect('page_prof')
    else:
        print("------ going to validation")
        return redirect('validation')


def logout_request(request):
    logout(request)
    return redirect('home')


# useless
def login_request(request):
    mssg = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    officier = Officier.objects.get(system_user=user)
                    if officier is not None:
                        login(request, user)
                        mssg = f"You are now logged in as {username}."
                        return redirect("home_page")
                except:
                    mssg = "Invalid username or password."
            else:
                mssg = "Invalid username or password."
        else:
            mssg = "Invalid username or password."

    form = AuthenticationForm()
    return render(request, "login.html", {'login_form': form, "mssg": mssg})


@login_required
def test_profile(request):

    context = {}

    return render(request, "essentials/profile.html", context)


def create_profile(data):
    # data = {
    #     'username': 'broccoli',
    #     'password': 'broccoli',
    #     'nom': 'broc',
    #     'prenom': 'coli',
    #     'date_naissance': '2005-06-17',
    #     'email': 'broc@coli.com',
    #     'chemin_image': 'images/my_logo.png',
    #     'type': 'etudiant',
    #     'niveau' : 'Prof'
    # }

    # try:
    # user = authenticate(username=data['username'], password=data['password'])
    # user = CustomUser.objects.get(username=data['username'])
    # except:
    # if user is None:

    user = CustomUser.objects.create(
        username=data['username'],
        # password=data['password'],
        nom=data['nom'],
        prenom=data['prenom'],
        date_naissance=data['date_naissance'],
        email=data['email'],
        # chemin_image=data['chemin_image'],
    )
    user.set_password(data['password'])
    user.save()

    if data['type'] == 'etudiant':
        user.is_etudiant = True
        user.save()
        etudiant = Etudiant.objects.create(user=user)
        print(etudiant.user.password)
        etudiant.save()
    elif data['type'] == 'enseignant' or data['type'] == 'professeur':
        user.is_enseignant = True
        user.save()
        enseignant = Enseignant(user=user)
        enseignant.niveau_academique = data['niveau']
        enseignant.save()

    user.save()
    return user


@csrf_exempt
@require_http_methods(["POST"])
def check_login(request):
    print("here")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process the JSON data as needed
            username = data['username']
            password = data['password']

            print(data)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    if user.is_etudiant:
                        etudiant = Etudiant.objects.get(user=user)
                        if etudiant is not None:
                            print('________ logging in as : ', user)
                            login(request, user)
                            return redirect("home")
                    elif user.is_enseignant:
                        enseignant = Enseignant.objects.get(user=user)
                        if enseignant is not None:
                            login(request, user)
                            return redirect("home")
                    else:
                        expert = Expert.objects.get(user=user)
                        if expert is not None:
                            login(request, user)
                            return redirect("home")
                except:
                    mssg = "Invalid username or password1."
            else:
                mssg = "Invalid username or password2."

            print(mssg)

            return HttpResponse('JSON data received successfully')
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    return HttpResponse('Invalid request method', status=405)


@csrf_exempt
@require_http_methods(["POST"])
def check_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # # Process the JSON data as needed
            username = data['username']
            password = data['password']
            # nom = data['nom']
            # prenom = data['prenom']
            # date_naissance = data['date_naissance']
            # email = data['email']
            # # chemin_image = data['chemin_image']
            # type = data['type']
            # # niveau pour etudiant, niveau académique pour enseignant
            # niveau = data['niveau']

            print(data)
            user = authenticate(request, username=username, password=password)
            if user is None:
                user = create_profile(data)
                login(request, user)
                return redirect("home")
            else:
                mssg = "error : existing user."

            print(mssg)

            return HttpResponse('JSON data received successfully')
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    return HttpResponse('Invalid request method', status=405)
