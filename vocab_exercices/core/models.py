from django.db.models import Q
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import random

# Create your models here.

# user model


class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30, null=True)
    prenom = models.CharField(max_length=30, null=True)
    date_naissance = models.DateField(null=True)
    email = models.EmailField(null=True)
    chemin_image = models.TextField(null=True)
    # user type
    is_etudiant = models.BooleanField(default=False)
    is_enseignant = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)


# profiles
class Etudiant(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    niveau = models.ForeignKey(
        to='Niveau', on_delete=models.SET_NULL, null=True, default=None)
    niveau2 = models.IntegerField(default=17, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Enseignant(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    niveau_academique = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class Expert(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    niveau_academique = models.CharField(max_length=30, null=True)
    nb_validations = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.user.username


class temps_conj(models.TextChoices):
    PASSE = 'A', ('الماضي')
    PRESENT = 'B', ('المضارع')
    SUBJONCTIF = 'C', ('المضارع المنصوب')
    PASSE_PASSIF = 'D', ('الماضي المبني للمجهول')
    PRESENT_PASSIF = 'E', ('المضارع المبني للمجهول')
    JUSSIF = 'F', ('المضارع المجزوم')
    IMPERATIF = 'G', ('الأمر')


class Exercice(models.Model):

    EXERCISE_TYPES = (
        ('1', 'reorder'),
        ('2', 'connect'),
        ('3', 'fill_in_the_blanks'),
        ('4', 'conjugate'),
    )

    type_exercice = models.CharField(
        max_length=1, choices=EXERCISE_TYPES, null=True)
    valeur = models.IntegerField(default=1)
    user = models.ForeignKey(
        to=CustomUser, on_delete=models.CASCADE, null=True)
    mot = models.ForeignKey(max_length=15, to="Lemme",
                            on_delete=models.CASCADE, null=True)

    def get_word(self):
        try:
            word = Lemme.objects.filter(rank=self.user.score)[0]
        except Exception as e:
            print(e)
            words = Lemme.objects.all()
            word = random.choice(words)
        return word


# ordonnancement
class Exo1(Exercice):
    phrase = models.TextField(null=True)

    def choose_phrase(self):
        word = self.get_word()
        try:
            phrase = Example.objects.filter(lemma=word)[0]
            phrase = phrase.example.split('\n')
            phrase = random.choice(phrase)
        except Exception as e:
            print(e)
            try:
                phrase = Example.objects.exclude(
                    example__in=[None, ""])
                # phrase = Example.objects.filter(~Q(example__in=[None, ""]))
                phrase = random.choice(phrase)
                phrase = phrase.example.split('\n')
                phrase = random.choice(phrase)
                print("|||", phrase, "|||")
            except:
                phrase = self.choose_phrase()

        self.phrase = phrase
        self.save()

    def mix(self):
        sentences = [
            "أنا طالب في المدرسة.",
            "أحب القراءة.",
            "هل تسكن في المدينة؟",
            "أنا أحب الرياضة.",
            "هل تتحدث العربية؟",
            "الجو حار اليوم.",
            "أنا أعمل في مكتب.",
            "هل تحب الطعام الإيطالي؟",
            "الطالب يدرس الرياضيات.",
            "أحب أن أسافر حول العالم."
        ]

        if self.phrase == None:
            self.phrase = random.choice(sentences)
            self.save()
        temp = self.phrase.split()
        random.shuffle(temp)
        return temp

    def check_answer(self, reponse):
        if self.phrase.strip() == reponse.strip():
            return True
        return False


# choix de définition
class Exo2(Exercice):
    mot_cible = models.TextField(max_length=15, null=True)
    definition = models.TextField(null=True)

    def get_definitions(self):
        word = self.get_word()
        self.mot_cible = word.lemme
        try:
            dfn = Definition.objects.filter(lemme=word)[0]
            id = dfn.id
            dfn = dfn.definition.split('\n')
            self.definition = random.choice(dfn)
            self.save()
            return {'id': id, 'dfn': self.definition}
        except Exception as e:
            print(e)
            dfn = Definition.objects.all()
            dfn = random.choice(dfn)
            id = dfn.id
            dfn = dfn.definition.split('\n')
            self.definition = random.choice(dfn)
            self.save()
            return {'id': id, 'dfn': self.definition}

    def check_answer(self, id):
        dfn = Definition.objects.get(id=id)
        dfn = dfn.definition.split('\n')
        if self.definition in dfn:
            return True
        return False

    def get_random(hello):
        all_objects = Definition.objects.all()

        # Randomly select three objects
        random_objects = random.sample(list(all_objects), 3)
        return [{'id': o.id, 'dfn': o.definition} for o in random_objects]


# remplissage de mot vide
class Exo3(Exercice):
    phrase = models.TextField(null=True)
    mot_vide = models.CharField(max_length=15, null=True)

    # doit etre redéfinie
    def choose_phrase(self):
        word = self.get_word()
        try:
            phrase = Example.objects.filter(lemma=word)[0]
            phrase = phrase.example.split('\n')
            phrase = random.choice(phrase)
        except Exception as e:
            print(e)
            phrase = Example.objects.exclude(
                example__in=[None, ""])
            phrase = random.choice(phrase)
            phrase = phrase.example.split('\n')
            phrase = random.choice(phrase)

        self.mot_vide = word.lemme
        self.phrase = phrase
        self.save()

    def get_phrase_mot_vide(self):
        sen_list = self.phrase.split()
        for i in range(0, len(sen_list)):
            if sen_list[i] == self.mot_vide:
                sen_list[i] = None
                break
        return sen_list

    def check_answer(self, mot_reponse):
        if mot_reponse == self.mot_vide:
            return True
        else:
            return False

# conjugaison


class Exo4(Exercice):
    mot_cible = models.CharField(max_length=15, null=True)
    temps_conjugaison = models.CharField(
        max_length=1,
        choices=temps_conj.choices,
        null=True
    )

    cnjg = models.TextField(null=True)

    # doit etre redéfinie
    def choose_temps(self):
        self.mot_vide = "تجنب"
        self.temps_conjugaison = random.choice("ABCDEFG")
        self.save()

    def get_table_conjg(self):
        word = self.get_word()
        self.mot_cible = word.lemme
        self.save()

        try:
            conjg = conjugaison.objects.filter(lemme=word)
            conjg = random.choice(conjg)
            self.cnjg = conjg.texte
            return conjg.texte
        except Exception as e:
            print(e)
            conjg = conjugaison.objects.all()
            conjg = random.choice(conjg)
            self.cnjg = conjg.texte
            return conjg.texte

    # change this

    def check_answer(self, text):
        if self.cnjg == text:
            return True
        else:
            return False


# MCD

class pos_tags(models.TextChoices):
    LETTRE = 'L', ('حرف')
    NOM = 'N', ('اسم')
    VERBE = 'V', ('فعل')
    PRENOM = 'P', ('ضمير')


categories_dict = {
    'literature': 'l',
    'religions': 'r',
    'economics': 'e',
    'history': 'h',
    'technology': 't',
    'novels': 'n',
    'politics': 'p',
    'poetry': 'o',
    'health': 'a',
    'psychology': 'c',
    'phylosophy': 'y',
    'arts': 'f',
    'children.stories': 'd',
    'plays': 'g',
    'primaire': 'x',
    'moyenne': 'z',
    'secondaire': 'w'
}


class Lemme(models.Model):
    lemme = models.CharField(max_length=15)
    freq_brute = models.IntegerField()
    freq_relative = models.DecimalField(max_digits=12, decimal_places=10)
    # synonyme + antonyme sont clé étrangere
    synonymes = models.ManyToManyField(to="self", related_name="synonymes")
    synonymes_valides = models.ManyToManyField(
        to="self", related_name="synonymes")
    antonymes = models.ManyToManyField(to="self", related_name="antonymes")
    antonymes_valides = models.ManyToManyField(
        to="self", related_name="antonymes")

    rank = models.BigIntegerField(null=True)

    # definition = models.OneToOneField(to="Definition", null=True, on_delete=models.SET_NULL)
    pos_tag = models.CharField(
        max_length=1,
        choices=pos_tags.choices,
        null=True
    )

    niveau = models.ForeignKey(
        to="Niveau", null=True, on_delete=models.SET_NULL)
    niveau2 = models.IntegerField(default=0, null=True)
    categories = models.CharField(max_length=17)

    syn_texte = models.TextField(null=True)
    ant_texte = models.TextField(null=True)

    def __str__(self):
        return self.lemme

    def get_pos_tag(self) -> pos_tags:
        # Get value from choices enum
        return pos_tags[self.pos_tag]

    def get_categories(self):
        return [cat for code, cat in categories_dict.items() if code in self.categories]

    class Meta:
        indexes = [
            models.Index(fields=['lemme',]),
            models.Index(fields=['id',]),
        ]

    def get_texte_syn(self):
        return self.syn_texte

    def get_texte_ant(self):
        return self.ant_texte


class Mot(models.Model):
    mot = models.CharField(max_length=15)
    analyse_morph = models.TextField(null=True)
    est_valide = models.BooleanField(default=False)
    lemma = models.ForeignKey(to=Lemme, on_delete=models.CASCADE, null=True)
    pos_tag = models.CharField(
        max_length=1,
        choices=pos_tags.choices,
        null=True
    )

    def __str__(self):
        return self.mot

    def get_pos_tag(self) -> pos_tags:
        # Get value from choices enum
        return pos_tags[self.pos_tag]


class Niveau(models.Model):
    nom = models.CharField(max_length=30)
    difficulte = models.IntegerField(null=True)
    age_recommande = models.IntegerField(null=True)

    def __str__(self):
        return self.nom


class Definition(models.Model):
    definition = models.TextField(null=True)
    est_valide = models.BooleanField(default=False)
    lemme = models.ForeignKey(to=Lemme, on_delete=models.CASCADE, null=True)


class Example(models.Model):
    example = models.TextField(null=True)
    est_valide = models.BooleanField(default=False)
    lemma = models.ForeignKey(to=Lemme, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.example


class conjugaison(models.Model):
    lemme = models.ForeignKey(to=Lemme, on_delete=models.CASCADE, null=True)
    est_valide = models.BooleanField(default=False)
    texte = models.TextField(null=True)
    prnm_je = models.CharField(max_length=30, null=True)
    prnm_nous = models.CharField(max_length=30, null=True)
    prnm_tu_M = models.CharField(max_length=30, null=True)
    prnm_tu_F = models.CharField(max_length=30, null=True)
    prnm_vous_2M = models.CharField(max_length=30, null=True)
    prnm_vous_PM = models.CharField(max_length=30, null=True)
    prnm_vous_PF = models.CharField(max_length=30, null=True)
    prnm_il = models.CharField(max_length=30, null=True)
    prnm_elle = models.CharField(max_length=30, null=True)
    prnm_ils_2 = models.CharField(max_length=30, null=True)
    prnm_ils_P = models.CharField(max_length=30, null=True)
    prnm_elles_P = models.CharField(max_length=30, null=True)

    temps = models.CharField(
        max_length=1,
        choices=temps_conj.choices,
        null=True
    )

    def get_temps(self) -> temps_conj:
        # Get value from choices enum
        return temps_conj[self.temps]

    # def __str__(self):
    #     return self.lemme + " : " + self.get_temps()

    def get_table(self):
        return [
            self.prnm_je,
            self.prnm_nous,
            self.prnm_tu_M,
            self.prnm_tu_F,
            self.prnm_vous_2M,
            self.prnm_vous_PM,
            self.prnm_vous_PF,
            self.prnm_il,
            self.prnm_elle,
            self.prnm_ils_2,
            self.prnm_ils_P,
            self.prnm_elles_P,
        ]

    def get_texte(self):
        return self.texte
