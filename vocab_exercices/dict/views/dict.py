from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from core.models import Lemme, Mot
import json

# Create your views here.


@csrf_exempt
def search(request):
    # get search parameters
    if request.method == 'POST':
        srch_prmt = json.loads(request.body)
        # {'query': , 'range_strt': , 'range_end': , 'lem_mot': }
        print(srch_prmt)

        if srch_prmt['lem_mot'] == 'lem':
            results = Lemme.objects.filter(
                lemme__icontains=srch_prmt['query']).filter(
                niveau2__lte=srch_prmt['range_end']).filter(
                niveau2__gte=srch_prmt['range_strt'])
            results = list(results)

            # transforming results
            treated_results = []
            for item in results:
                treated_results.append({
                    'id': item.id,
                    'word': item.lemme
                })
        else:
            temp_results = Mot.objects.filter(
                mot__icontains=srch_prmt['query'])
            treated_results = []
            for mot in temp_results:
                lem = mot.lemma
                # lem = Lemme.objects.get(id=mot.lemma)
                if lem.niveau2 <= int(srch_prmt['range_end']) and lem.niveau2 >= int(srch_prmt['range_strt']):
                    treated_results.append({
                        'id': mot.id,
                        'word': mot.mot
                    })
            print(treated_results)

        # print(treated_results)
        print(type(treated_results))
        return JsonResponse({'results': treated_results})

    # find all relevant words

    # render page
    return render(request, 'search/search.html')


# @csrf_exempt
# def get_lemme_info(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             id = data['id']
#             lemme = data['lemme']
#             lemme_objet = Lemme.objects.get(id=id)
#             try:
#                 niv = Niveau.objects.get(lemme_objet.niveau).nom
#             except:
#                 niv = "N/A"
#             try:
#                 defn = Definition.objects.filter(lemme=lemme)[0].definition
#             except:
#                 defn = "N/A"
#             try:
#                 exmpl = Example.objects.filter(lemme=lemme)[0].example
#             except:
#                 exmpl = "N/A"
#             try:
#                 cnjgs = conjugaison.objects.filter(lemme=lemme)
#                 cnjg = [{'temps': c.temp,
#                          'table': c.get_table()} for c in cnjgs]
#             except:
#                 cnjg = "N/A"

#             response = {
#                 'lemme': lemme_objet.lemme,
#                 'pos_tag': lemme_objet.get_pos_tag(),
#                 'categories': lemme_objet.get_categories(),
#                 'niveau': niv,
#                 'synonymes': lemme_objet.synonymes,
#                 'antonymes': lemme_objet.antonymes,
#                 'definition': defn,
#                 'example': exmpl,
#                 'conjugaison': cnjg
#             }

#             return JsonResponse(response)

#         except json.JSONDecodeError:
#             return HttpResponse('Invalid JSON data', status=400)


# def dictionnaire(request):
#     list_mots_niv = Lemme.objects.all()
#     list_mots_niv = [{'id': i.id, 'lemme': i.lemme} for i in list_mots_niv]
#     if request.method == 'GET':
#         # Perform actions for GET request
#         id = request.GET.get('id')
#         if id is not None:
#             print(id)
#             search_result = Lemme.objects.get(id=int(id))
#             dfnts = Definition.objects.filter(lemme=search_result)
#             exmple = Example.objects.filter(lemma=search_result)
#             cnjg = conjugaison.objects.filter(lemme=search_result)

#             context = {
#                 'result': search_result.lemme,
#                 'definitions': [d.definition for d in dfnts],
#                 'synonymes': search_result.get_texte_syn(),
#                 'antonymes': search_result.get_texte_ant(),
#                 'examples': [e.example for e in exmple],
#                 'conjugaison': [re.sub(r'\s+', ' ', c.texte.replace('\n', ' ')).strip() for c in cnjg],
#                 'list_mots_niv': list_mots_niv
#             }

#             print(context['conjugaison'])

#             return render(request, 'html/dict.html', context)

#     # Handle other request methods
#     context = {
#         'result': None,
#         'list_mots_niv': list_mots_niv
#     }

#     return render(request, 'html/dict.html', context)
