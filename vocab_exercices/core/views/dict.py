from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import *
import random
from django.db.models import Q


@csrf_exempt
def get_lemme_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data['id']
            lemme = data['lemme']
            lemme_objet = Lemme.objects.get(id=id)
            try:
                niv = Niveau.objects.get(lemme_objet.niveau).nom
            except:
                niv = "N/A"
            try:
                defn = Definition.objects.filter(lemme=lemme)[0].definition
            except:
                defn = "N/A"
            try:
                exmpl = Example.objects.filter(lemme=lemme)[0].example
            except:
                exmpl = "N/A"
            try:
                cnjgs = conjugaison.objects.filter(lemme=lemme)
                cnjg = [{'temps': c.temp,
                         'table': c.get_table()} for c in cnjgs]
            except:
                cnjg = "N/A"

            response = {
                'lemme': lemme_objet.lemme,
                'pos_tag': lemme_objet.get_pos_tag(),
                'categories': lemme_objet.get_categories(),
                'niveau': niv,
                'synonymes': lemme_objet.synonymes,
                'antonymes': lemme_objet.antonymes,
                'definition': defn,
                'example': exmpl,
                'conjugaison': cnjg
            }

            return JsonResponse(response)

        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)


@csrf_exempt
def get_mots(request):
    if request.method == 'POST':
        try:
            # envoyé par javascript
            # data_prototype = {
            #     'query' : 'ككل',
            #     'type_recherche' : 'l' / 'm',
            #     'page' : 23,
            #     'nivs' : 'one' / 'multiple' / 'all',
            #     'niveau' : '17'
            # }
            print('1 - CHECKPOINT 1')
            data = json.loads(request.body)
            print(data)
            query = data['query']
            page = data['page']
            results = []
            nb_pages = 0

            print('2 - CHECKPOINT 2')
            niv_cond = None
            if data['nivs'] == 'all':
                niv_cond = Q(niveau2__lte=20)
            elif data['nivs'] == 'one':
                niv_cond = Q(niveau2=data['niveau'])
            elif data['nivs'] == 'multiple':
                niv_cond = Q(niveau2__gte=data['niveau'])

            niv_cond = Q(niveau2__is_null=True)

            print('3 - CHECKPOINT 3')
            if data['type_recherche'] == 'l':
                queryset = Lemme.objects.filter(
                    Q(lemme__contains=query), niv_cond)
                # print('HELLO : ', queryset)
                for i in range(100):
                    try:
                        results.append(
                            {queryset[i + 100*page].id: queryset[i + 100*page].lemme})
                    except:
                        break
            else:
                queryset = Mot.objects.filter(Q(mot__contains=query), niv_cond)
                for i in range(100):
                    try:
                        results.append(
                            {queryset[i + 100*page].id: queryset[i + 100*page].mot})
                    except:
                        break

            print('4 - CHECKPOINT 4')

            print(Mot.objects.filter(Q(mot__icontains=query)))
            nb_pages = len(queryset)/100

            print('\n\n', results, '\n\n')

            return JsonResponse({'nb_pages': nb_pages,
                                 'results': results})

        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)


class proxy(TemplateView):
    template_name = "essentials/proxy.html"
