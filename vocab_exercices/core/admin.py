from .models import CustomUser
from .models import Example
from .models import Definition
from .models import Niveau
from .models import Mot
from .models import Lemme
from .models import Exo4
from .models import Exo3
from .models import Exo2
from .models import Exo1
from .models import Etudiant
from .models import Enseignant
from .models import Expert
from .models import conjugaison
from django.contrib import admin

# Register your models here.

admin.site.register(CustomUser)

admin.site.register(Etudiant)

admin.site.register(Enseignant)

admin.site.register(Expert)

admin.site.register(Exo1)

admin.site.register(Exo2)

admin.site.register(Exo3)

admin.site.register(Exo4)

# MCD

admin.site.register(Lemme)

admin.site.register(Mot)

admin.site.register(Niveau)

admin.site.register(Definition)

admin.site.register(Example)

admin.site.register(conjugaison)
