from django.urls import path
# from .views import home, exercise_list, exercise_1, exercise_2, load, search_results
from .views.html_pages import *
from .views.temp import *
from .views.profiles import *
from .views.dict import *

urlpatterns = [
    # TEMP
    # path('list', exercise_list, name='exercise_list'),
    # path('ex1', exercise_1, name='exercise_1'),
    # path('ex2', exercise_2, name='exercise_2'),
    path('load', load, name='load'),
    # path('search/<int:i>', search_results, name='search'), # due to working on better version

    # HTML PAGES
    path('log_in', log_in, name='log_in'),
    path('', log_in, name='log_in'),
    path('dictionnaire', dictionnaire, name='dict'),
    path('etudiant', etudiant.as_view(), name='etudiant'),
    path('exo1', exo1, name='exo1'),
    path('exo2', exo2, name='exo2'),
    path('exo3', exo3, name='exo3'),
    path('exo4', exo4, name='exo4'),
    path('profile', profile.as_view(), name='profile'),
    # path('etudiant', etudiant.as_view(), name='etudiant'),
    path('analyse_prof', analyse_prof.as_view(), name='analyse_prof'),
    path('dicte_prof', dicte_prof.as_view(), name='dicte_prof'),
    path('page_prof', page_prof.as_view(), name='page_prof'),
    path('validation/', validation, name='validation'),
    # path('', , name=),


    # PROFILES
    path('home', home, name='home'),
    path('test_profile', test_profile, name='test_profile'),
    path('log_out', logout_request, name='log_out'),

    path('check_login', check_login, name='check_login'),
    path('check_signup', check_signup, name='check_signup'),

    # DICT
    path('dict/proxy', proxy.as_view(), name='dict_proxy'),
    path('dict/search', get_mots, name='dict_search'),

    # TEMP
    path('load_json', load_myriad, name='load_json'),

    # VALIDATION
    path('search_expert/', search_expert, name='search_expert'),
    path('modifier_lemme', modifier_lemme, name='modifier_lemme'),

    # recherche etudiant
    path('search_etudiant/', search_etudiant, name='search_etudiant'),






]
