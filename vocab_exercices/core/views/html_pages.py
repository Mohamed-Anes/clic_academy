import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from ..models import *
import random
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Page views


# class log_in(TemplateView):
#     template_name = 'index.html'

def log_in(request):
    logout(request)
    mssg = ""
    if request.method == "POST":
        print("here here")

        form = AuthenticationForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            print("here here 2")

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username + "  " + password)
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    etudiant = Etudiant.objects.get(user=user)
                    if etudiant is not None:
                        login(request, user)
                        mssg = f"You are now logged in as {username}."
                        return redirect("home")
                except:
                    try:
                        enseignant = Enseignant.objects.get(user=user)
                        if enseignant is not None:
                            login(request, user)
                            mssg = f"You are now logged in as {username}."
                            return redirect("home")
                    except:
                        try:
                            expert = Expert.objects.get(user=user)
                            if expert is not None:
                                login(request, user)
                                mssg = f"You are now logged in as {username}."
                                return redirect("home")
                        except:
                            mssg = "Invalid username or password."
            else:
                mssg = "Invalid username or password."
        else:
            mssg = "Invalid username or password."

    form = AuthenticationForm()
    return render(request, "index.html", {'login_form': form, "mssg": mssg})


def dictionnaire(request):
    list_mots_niv = Lemme.objects.all()
    list_mots_niv = [{'id': i.id, 'lemme': i.lemme} for i in list_mots_niv]
    if request.method == 'GET':
        # Perform actions for GET request
        id = request.GET.get('id')
        if id is not None:
            print(id)
            search_result = Lemme.objects.get(id=int(id))
            dfnts = Definition.objects.filter(lemme=search_result)
            exmple = Example.objects.filter(lemma=search_result)
            cnjg = conjugaison.objects.filter(lemme=search_result)

            context = {
                'result': search_result.lemme,
                'definitions': [d.definition for d in dfnts],
                'synonymes': search_result.get_texte_syn(),
                'antonymes': search_result.get_texte_ant(),
                'examples': [e.example for e in exmple],
                'conjugaison': [re.sub(r'\s+', ' ', c.texte.replace('\n', ' ')).strip() for c in cnjg],
                'list_mots_niv': list_mots_niv
            }

            print(context['conjugaison'])

            return render(request, 'html/dict.html', context)

    # Handle other request methods
    context = {
        'result': None,
        'list_mots_niv': list_mots_niv
    }

    return render(request, 'html/dict.html', context)


class etudiant(TemplateView):
    template_name = 'html/etud.html'


# class exo1(TemplateView):
#     template_name = 'html/etudaint-exo1.html'


@csrf_exempt
def exo1(request):
    # cas d'envoie de réponse
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data['id']
            reponse = data['reponse']
            exercice = Exo1.objects.get(id=id)
            print("checking answer")
            if exercice.check_answer(reponse):
                # increment score TO-DO
                user = request.user
                user.score += 1
                return JsonResponse({'right': True})
            else:
                return JsonResponse({'right': False})
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    # cas de géneration de l'exercice
    else:
        exercice = Exo1.objects.create()
        exercice.choose_phrase()
        shuffled = exercice.mix()
        return render(request, 'html/etudaint-exo2.html', {'id': exercice.id, 'phrase': shuffled})


# fill in the blanks exercise
@csrf_exempt
def exo2(request):
    # cas d'envoie de réponse
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data['id']
            reponse = data['reponse']
            exercice = Exo3.objects.get(id=id)
            print("checking answer")
            if exercice.check_answer(reponse):
                # increment score TO-DO
                user = request.user
                user.score += 1
                return JsonResponse({'right': True, })
            else:
                return JsonResponse({'right': False, })
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    # cas de géneration de l'exercice
    else:
        exercice = Exo3.objects.create()
        exercice.choose_phrase()
        return render(request, 'html/etudaint-exo1.html', {'id': exercice.id, 'phrase': exercice.get_phrase_mot_vide()})


# # choix de définition (model Exo2)
@csrf_exempt
def exo3(request):
    # cas d'envoie de réponse
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data['id']
            reponse = data['reponse']  # response is an id
            print("REPONSE : ", reponse)
            exercice = Exo3.objects.get(id=id)
            print("checking answer")
            if exercice.check_answer(reponse):
                # increment score TO-DO
                user = request.user
                user.score += 1
                return JsonResponse({'right': True, })
            else:
                return JsonResponse({'right': False, })
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    # cas de géneration de l'exercice
    else:
        exercice = Exo2.objects.create()
        right = exercice.get_definitions()
        if right is not None:
            pass
        else:
            print("ERROR CHOOSING WORD AND DEFINITION")
            return render(request, 'html/etudaint-exo3.html')

        wrongs = exercice.get_random()
        wrongs.append(right)
        wrongs = random.sample(wrongs, len(wrongs))
        return render(request, 'html/etudaint-exo3.html', {'id': exercice.id, 'phrases': wrongs})

# # conjugaison (model Exo4)


@csrf_exempt
def exo4(request):  # CHANGE ALL OF THIS
    # cas d'envoie de réponse
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data['id']
            reponse = data['reponse']  # response is an id
            print("REPONSE : ", reponse)
            exercice = Exo3.objects.get(id=id)
            print("checking answer")
            if exercice.check_answer(reponse):
                # increment score TO-DO
                user = request.user
                user.score += 1
                return JsonResponse({'right': True, })
            else:
                return JsonResponse({'right': False, })
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)

    # cas de géneration de l'exercice
    else:
        exercice = Exo4.objects.create()
        right = exercice.choose_temps()
        if right is not None:
            pass
        else:
            print("ERROR CHOOSING WORD AND DEFINITION")
            return render(request, 'html/etudaint-exo3.html')

        wrongs = exercice.get_table_conjg()
        return render(request, 'html/etudaint-exo4.html', {'id': exercice.id, 'phrases': wrongs})


# class etudiant(TemplateView):
#     template_name = 'etudain/etud.html'


class analyse_prof(TemplateView):
    template_name = 'html/analyse_prof.html'


class dicte_prof(TemplateView):
    template_name = 'html/dict_prof.html'


class page_prof(TemplateView):
    template_name = 'html/page_prof.html'


class profile(TemplateView):
    template_name = 'html/profile.html'


def validation(request):
    if request.method == 'GET':
        # Perform actions for GET request
        id = request.GET.get('id')
        if id is not None:
            print(id)
            search_result = Lemme.objects.get(id=int(id))
            dfnts = Definition.objects.filter(lemme=search_result)
            exmple = Example.objects.filter(lemma=search_result)
            cnjg = conjugaison.objects.filter(lemme=search_result)

            context = {
                'result': search_result.lemme,
                'id': search_result.id,
                'definitions': [d.definition for d in dfnts],
                'synonymes': search_result.get_texte_syn(),
                'antonymes': search_result.get_texte_ant(),
                'examples': [e.example for e in exmple],
                'conjugaison': [c.get_texte for c in cnjg],
            }

            return render(request, 'html/valider.html', context)

    # Handle other request methods
    context = {
        'result': None,
    }
    return render(request, 'html/valider.html', context)
