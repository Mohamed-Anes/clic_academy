from django.views.decorators.csrf import csrf_exempt
import os
from django.views.generic.base import TemplateView
from django.shortcuts import render
from ..models import *
import random
import json
from django.http import HttpResponse, JsonResponse


# Create your views here.


def exercise_list(request):
    return render(request, 'exercices/list.html')


def exercise_1(request):

    mot = Lemme.objects.order_by('?').first()

    phrase = "set up"

    choix = Mot.objects.filter(lemma=mot)

    choix = random.sample(list(choix), 3)

    context = {
        'sentence': phrase,
        'right_1': mot,
        'wrong_2': choix[0],
        'wrong_3': choix[1],
        'wrong_4': choix[2]
    }
    return render(request, 'exercices/exercise_1.html', context)


def exercise_2(request):
    context = {
        'phrase': 'تربيها غريزة العقل التجارب'.split()
    }
    return render(request, 'exercices/exercise_2.html', context)


# FUNCTIONS FOR LOADING THE DICTIONARY
def testerrorword(word):
    t = list(word)
    if ('ة' in t[0:-4]):
        return False
    return True


def supprimer_lettres_repetees(chaine):

    chars = list(chaine)
    unique_chars = []
    for char in chars:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)


def list_son_repetion(lst):

    duplicates = []
    for i in range(len(lst)):
        if not (lst[i] in duplicates):
            duplicates.append(lst[i])
    return duplicates


def load_dictionary():
    import xml.etree.ElementTree as xml
    import os

    word_exs = {}
    dict_file = os.path.join('static', 'finale_module3.xml')

    # Getting the data from xml file - DONE ONCE -
    tree = xml.parse(dict_file)
    root = tree.getroot()
    words = root.findall('word')

    dict_word_counts = {}
    dict_frequency_moy = {}
    dict_familleMorphologique = {}
    dict_nbdocument = {}
    dict_word_general = {}
    dict_frequency = {}
    dict_poids = {}
    dict_categorie = {}
    dict_word_sp = {}
    dict_word_niveau_0 = {}

    i = 0
    longest = 0

    for word in words:
        value = word.get('value')
        frequency = int(word.get('frequency'))
        nb_document_appart = int(word.get('nb_document_appart'))
        famille_Morphologique = word.get('famille_Morphologique')
        frequency_moy = float(word.get('frequency_moy'))
        list_frequency = word.get('list_frequency')
        categorie = word.get('catégorie')

        list_frequency = ''.join(
            c for c in list_frequency if c not in ['[', ']', "'", ' '])
        list_frequency = list_frequency.split(",")
        famille_Morphologique = ''.join(
            c for c in famille_Morphologique if c not in ['[', ']', "'", ' '])
        famille_Morphologique = famille_Morphologique.split(",")

        if (len(value) > 17 or testerrorword(value) == False):  # error
            #         file.write(str(i)+" "+value+" \n")
            i += 1
        else:
            #         if (len(famille_Morphologique)==1 and len(categorie)==1 and nb_document_appart==1):
            #             dict_word_niveau_0[value]=dict_word_niveau_0.get(value,0)+frequency_moy
            # #             nb_mots += frequency
            # #             nb_moy_norm += frequency_moy
            #         else:
            if len(value) > longest:
                longest = len(value)
            dict_frequency_moy[value] = dict_frequency_moy.get(
                value, 0)+frequency_moy
            dict_categorie[value] = supprimer_lettres_repetees(
                dict_categorie.get(value, "")+categorie)
            dict_frequency[value] = dict_frequency.get(
                value, []) + list_frequency
            dict_word_counts[value] = dict_word_counts.get(
                value, 0) + frequency
    #             nb_mots += frequency
    #             nb_moy_norm+=frequency_moy

            dict_familleMorphologique[value] = list_son_repetion(
                dict_familleMorphologique.get(value, []) + famille_Morphologique)
            dict_nbdocument[value] = dict_nbdocument.get(
                value, 0) + nb_document_appart

    print("good words : ", len(dict_frequency_moy))
    print("wrong words : ", i)
    print("longest : ", longest)

    # creation de niveaux
    # for i in range(0, 19):
    #     niv = Niveau(nom=f"{i}")
    #     niv.save()
    #     print("created niveau")

    i = 0
    j = 0
    nums = 0

    lemmes = []
    mots = []

    for lem, freq in dict_word_counts.items():
        try:
            niv = len(dict_categorie[lem])
            if niv == 1 and dict_nbdocument[lem] == 1 and len(dict_familleMorphologique[lem]) == 1:
                niv = 0
                nums += 1

            i += 1
            j += 1

            # if i < 1126:
            #     continue

            print(i, " ", j)
            # creation de lemmas
            lemme_object = Lemme(
                lemme=lem[0:-2],
                freq_brute=freq,
                freq_relative=dict_frequency_moy[lem],
                pos_tag=lem[-1],
                # niveau=Niveau.objects.get(nom=str(len(dict_categorie[lem]))),
                niveau2=niv,
                categories=dict_categorie[lem]
            )
            # lemme_object.save()
            lemmes.append(lemme_object)

            # creation de famille morphologique
            for mot in dict_familleMorphologique[lem]:
                mot_object = Mot(
                    mot=mot,
                    lemma=lemme_object,
                    pos_tag=lem[-1],
                )
                # mot_object.save()
                mots.append(mot_object)

            if j > 500:
                j = 0
                Lemme.objects.bulk_create(lemmes)
                Mot.objects.bulk_create(mots)
                print("\n\n\n --------- bulk created ", i, " ---------\n\n\n")
                lemmes = []
                mots = []
        except:
            continue

            # creation de définitions

            # creation des examples
    print('nums of 0 niveau : ', nums)


def load(request):
    insert_words()


def search_results(request, i):
    query = request.GET.get('query')
    # if request.method == 'GET' and i != 0:
    if query is not None:

        model1_results = Lemme.objects.filter(lemme__icontains=query)
        model2_results = Mot.objects.filter(mot__icontains=query)

        context = {
            'query': query,
            'lemmes': model1_results,
            'mots': model2_results,
        }

        return render(request, 'essentials/search.html', context)

    # else
    lemmes = Lemme.objects.all()[(i*50):(i*50 + 100)]
    # add control to not get out of range
    # print(lemmes[(i*50):(i*50 + 100)])

    mots = Mot.objects.all()[(i*50):(i*50 + 100)]
    # print(mots[(i*50):(i*50 + 100)])

    return render(request, 'essentials/search.html', context={'lemmes': lemmes, 'mots': mots})


def search_expert(request):
    print("requesting")
    query = request.GET.get('query')
    # if request.method == 'GET' and i != 0:
    if query is not None:
        print(query)
        if query == "":
            query = "ا"

        model1_results = Lemme.objects.filter(lemme__icontains=query)

        model1_results = [
            {
                "id": m.id,
                "lemme": m.lemme
            }
            for m in model1_results
        ]

        context = {
            'lemmes': model1_results,
        }

        return JsonResponse(context)

    return JsonResponse({'lemmes': []})


@csrf_exempt
def modifier_lemme(request):
    print("MODIFYING")
    if request.method == 'POST':
        # Get the JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            response_data = {'message': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)

        # Access the JSON data
        # username = data.get('username')
        # password = data.get('password')

        try:
            lem = Lemme.objects.get(id=data.get('id'))
            lem.syn_texte = data.get('synonymes')
            lem.ant_texte = data.get('antonymes')
            lem.save()
        except Exception as e:
            print('error in lemma', e)

        try:
            dfn = Definition.objects.filter(lemme=lem)[0]
            dfn.definition = data.get('definitions')
            dfn.save()
        except Exception as e:
            print('error in definition', e)

        try:
            exmpl = Example.objects.filter(lemma=lem)[0]
            exmpl.example = data.get('examples')
            exmpl.save()
        except Exception as e:
            print('error in example', e)

        try:
            cnjg = conjugaison.objects.filter(lemme=lem)[0]
            cnjg.texte = data.get('conjugaison')
            cnjg.save()
        except Exception as e:
            print('error in conjugaison', e)

        # Perform some processing or logic
        # ...

        # Return a JSON response
        response_data = {'message': 'Data received successfully'}
        return JsonResponse(response_data)

    # Return an error response for non-POST requests
    response_data = {'message': 'Invalid request method'}
    return JsonResponse(response_data, status=405)


def search_etudiant(request):
    print("requesting")
    query = request.GET.get('query')
    # if request.method == 'GET' and i != 0:
    if query is not None:
        print(query)
        if query == "":
            query = "ا"

        model1_results = Lemme.objects.filter(lemme__icontains=query)

        model1_results = [
            {
                "id": m.id,
                "lemme": m.lemme
            }
            for m in model1_results
        ]

        context = {
            'lemmes': model1_results,
        }

        return JsonResponse(context)

    return JsonResponse({'lemmes': []})


def load_myriad(request):
    # Open the JSON file
    with open('static/youcef_antonyme2.txt', 'r', encoding="utf-8") as file:
        # Load JSON data
        data = json.load(file)
    # print(data)
    i = 0
    for key, item in data.items():
        lem = Lemme.objects.filter(lemme=key)
        # print(lem)
        # print(len(lem))
        for l in lem:
            l.ant_texte = item
            l.save()
            i += 1
            print(i)

    return HttpResponse('Done')


def insert_words():

    import xml.etree.ElementTree as xml
    import os

    dict_file = os.path.join('static', 'finale_module3.xml')

    # Getting the data from xml file - DONE ONCE -
    tree = xml.parse(dict_file)
    root = tree.getroot()
    words = root.findall('word')

    dict_word_counts = {}
    dict_frequency_moy = {}
    dict_familleMorphologique = {}
    dict_nbdocument = {}
    dict_frequency = {}
    dict_categorie = {}

    i = 0
    longest = 0

    for word in words:
        value = word.get('value')
        frequency = int(word.get('frequency'))
        nb_document_appart = int(word.get('nb_document_appart'))
        famille_Morphologique = word.get('famille_Morphologique')
        frequency_moy = float(word.get('frequency_moy'))
        list_frequency = word.get('list_frequency')
        categorie = word.get('catégorie')

        list_frequency = ''.join(
            c for c in list_frequency if c not in ['[', ']', "'", ' '])
        list_frequency = list_frequency.split(",")
        famille_Morphologique = ''.join(
            c for c in famille_Morphologique if c not in ['[', ']', "'", ' '])
        famille_Morphologique = famille_Morphologique.split(",")

        if (len(value) > 17 or testerrorword(value) == False):  # error
            i += 1
        else:
            if len(value) > longest:
                longest = len(value)
            dict_frequency_moy[value] = dict_frequency_moy.get(
                value, 0)+frequency_moy
            dict_categorie[value] = supprimer_lettres_repetees(
                dict_categorie.get(value, "")+categorie)
            dict_frequency[value] = dict_frequency.get(
                value, []) + list_frequency
            dict_word_counts[value] = dict_word_counts.get(
                value, 0) + frequency
    #             nb_mots += frequency
    #             nb_moy_norm+=frequency_moy

            dict_familleMorphologique[value] = list_son_repetion(
                dict_familleMorphologique.get(value, []) + famille_Morphologique)
            dict_nbdocument[value] = dict_nbdocument.get(
                value, 0) + nb_document_appart

    print("good words : ", len(dict_frequency_moy))
    print("wrong words : ", i)
    print("longest : ", longest)

    i = 0
    j = 0
    nums = 0

    # instantiating lists for bulk creation
    lemmes = []
    mots = []
    dfnts = []
    exmpls = []
    cnjgs = []

    # getting info from files
    niv1_words = os.path.join('static', 'niv1_words.txt')
    with open(niv1_words, 'r', encoding='utf-8') as words:
        words_list = words.read()
        words_list = words_list.split()

    niv1_words = os.path.join('static', 'niv1_dfnt.txt')
    with open(niv1_words, 'r', encoding='utf-8') as dfnts_file:
        dfnts_dict = json.load(dfnts_file)

    niv1_words = os.path.join('static', 'niv1_exmpl.txt')
    with open(niv1_words, 'r', encoding='utf-8') as exmpls_file:
        exmpls_dict = json.load(exmpls_file)

    niv1_words = os.path.join('static', 'niv1_conjg.txt')
    with open(niv1_words, 'r', encoding='utf-8') as cnjgs_file:
        cnjgs_dict = json.load(cnjgs_file)

    # file needs to be checked
    # niv1_words = os.path.join('static', 'niv1_syn_snt.txt')
    # with open(niv1_words, 'r', encoding='utf-8') as syn_file:
    #     syn_dict = json.load(syn_file)

    # all 1000 words are present as nouns, 593 of them are present as verbs
    for word in words_list:
        my_word = word + '.N'
        try:
            i += 1
            j += 1

            print(i, " ", j)
            # creation de lemmas
            lemme_object = Lemme(
                lemme=word,
                freq_brute=dict_word_counts[my_word],
                freq_relative=dict_frequency_moy[my_word],
                pos_tag='N',
                # niveau=Niveau.objects.get(nom=str(len(dict_categorie[lem]))),
                niveau2=1,
                categories=dict_categorie[my_word]
            )
            # lemme_object.save()
            lemmes.append(lemme_object)

            # creation de famille morphologique
            for mot in dict_familleMorphologique[my_word]:
                mot_object = Mot(
                    mot=mot,
                    lemma=lemme_object,
                    pos_tag='N',
                )
                # mot_object.save()
                mots.append(mot_object)

            # creation de definition
            dfnt_object = Definition(
                definition=dfnts_dict.get(word),
                lemme=lemme_object
            )
            dfnts.append(dfnt_object)

            # creation de example
            exmpl_object = Example(
                example=exmpls_dict.get(word),
                lemma=lemme_object
            )
            exmpls.append(exmpl_object)

            # creation de conjugaison
            if type(cnjgs_dict.get(word)) == type(list()):
                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[0],
                    lemme=lemme_object,
                    temps='A'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[1],
                    lemme=lemme_object,
                    temps='B'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[2],
                    lemme=lemme_object,
                    temps='C'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[3],
                    lemme=lemme_object,
                    temps='F'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[4],
                    lemme=lemme_object,
                    temps='D'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[5],
                    lemme=lemme_object,
                    temps='E'
                )
                cnjgs.append(cnjg_object)

                cnjg_object = conjugaison(
                    texte=cnjgs_dict.get(word)[6],
                    lemme=lemme_object,
                    temps='G'
                )
                cnjgs.append(cnjg_object)

            # if j > 500:
            #     j = 0
            #     Lemme.objects.bulk_create(lemmes)
            #     Mot.objects.bulk_create(mots)
            #     print("\n\n\n --------- bulk created ", i, " ---------\n\n\n")
            #     lemmes = []
            #     mots = []

        except Exception as e:
            print(e)
            continue

    lemmes = sorted(lemmes, key=lambda obj: obj.freq_relative)
    i = 0
    for lem in lemmes:
        lem.rank = i
        i += 1

    print("dfnts : ", len(dfnts))
    print("exmpls : ", len(exmpls))
    print("cnjgs : ", len(cnjgs))

    try:
        Lemme.objects.bulk_create(lemmes)
        Mot.objects.bulk_create(mots)
        Definition.objects.bulk_create(dfnts)
        Example.objects.bulk_create(exmpls)
        conjugaison.objects.bulk_create(cnjgs)
    except Exception as e:
        print(e)
        print(type(dfnts[0]), type(dfnts[1]), type(dfnts[5]))
        print(dfnts[0])
        print(dfnts[0].lemme)
        print(dfnts[0].definition)
        print(dfnts[0].id)
        print(dfnts[1])
        print(dfnts[1].lemme)
        print(dfnts[1].definition)
        print(dfnts[1].id)
        print(dfnts[5])
        print(dfnts[5].lemme)
        print(dfnts[5].definition)
        print(dfnts[5].id)

    # for lem, freq in dict_word_counts.items():
    #     try:
    #         niv = len(dict_categorie[lem])
    #         if niv == 1 and dict_nbdocument[lem] == 1 and len(dict_familleMorphologique[lem]) == 1:
    #             niv = 0
    #             nums += 1

    #         i += 1
    #         j += 1

    #         print(i, " ", j)
    #         # creation de lemmas
    #         lemme_object = Lemme(
    #             lemme=lem[0:-2],
    #             freq_brute=freq,
    #             freq_relative=dict_frequency_moy[lem],
    #             pos_tag=lem[-1],
    #             # niveau=Niveau.objects.get(nom=str(len(dict_categorie[lem]))),
    #             niveau2=niv,
    #             categories=dict_categorie[lem]
    #         )
    #         # lemme_object.save()
    #         lemmes.append(lemme_object)

    #         # creation de famille morphologique
    #         for mot in dict_familleMorphologique[lem]:
    #             mot_object = Mot(
    #                 mot=mot,
    #                 lemma=lemme_object,
    #                 pos_tag=lem[-1],
    #             )
    #             # mot_object.save()
    #             mots.append(mot_object)

    #         if j > 500:
    #             j = 0
    #             Lemme.objects.bulk_create(lemmes)
    #             Mot.objects.bulk_create(mots)
    #             print("\n\n\n --------- bulk created ", i, " ---------\n\n\n")
    #             lemmes = []
    #             mots = []
    #     except:
    #         continue

    #         # creation de définitions

    #         # creation des examples
    # print('nums of 0 niveau : ', nums)

    return HttpResponse("hello world")
