# Generated by Django 4.2.1 on 2023-06-06 21:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nom', models.CharField(max_length=30, null=True)),
                ('prenom', models.CharField(max_length=30, null=True)),
                ('date_naissance', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('chemin_image', models.TextField(null=True)),
                ('is_etudiant', models.BooleanField(default=False)),
                ('is_enseignant', models.BooleanField(default=False)),
                ('is_expert', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_exercice', models.CharField(choices=[('1', 'reorder'), ('2', 'connect'), ('3', 'fill_in_the_blanks'), ('4', 'conjugate')], max_length=1, null=True)),
                ('valeur', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Lemme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemme', models.CharField(max_length=15)),
                ('freq_brute', models.IntegerField()),
                ('freq_relative', models.DecimalField(decimal_places=10, max_digits=12)),
                ('pos_tag', models.CharField(choices=[('L', 'حرف'), ('N', 'اسم'), ('V', 'فعل'), ('P', 'ضمير')], max_length=1, null=True)),
                ('niveau2', models.IntegerField(default=0, null=True)),
                ('categories', models.CharField(max_length=17)),
                ('antonymes', models.ManyToManyField(related_name='antonymes', to='core.lemme')),
                ('antonymes_valides', models.ManyToManyField(related_name='antonymes', to='core.lemme')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('difficulte', models.IntegerField(null=True)),
                ('age_recommande', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('niveau_academique', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Exo1',
            fields=[
                ('exercice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.exercice')),
                ('phrase', models.TextField(null=True)),
            ],
            bases=('core.exercice',),
        ),
        migrations.CreateModel(
            name='Exo2',
            fields=[
                ('exercice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.exercice')),
                ('mot_cible', models.TextField(max_length=15, null=True)),
                ('definition', models.TextField(null=True)),
            ],
            bases=('core.exercice',),
        ),
        migrations.CreateModel(
            name='Exo3',
            fields=[
                ('exercice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.exercice')),
                ('phrase', models.TextField(null=True)),
                ('mot_vide', models.CharField(max_length=15, null=True)),
            ],
            bases=('core.exercice',),
        ),
        migrations.CreateModel(
            name='Exo4',
            fields=[
                ('exercice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.exercice')),
                ('mot_cible', models.CharField(max_length=15, null=True)),
            ],
            bases=('core.exercice',),
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('niveau_academique', models.CharField(max_length=30, null=True)),
                ('nb_validations', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot', models.CharField(max_length=15)),
                ('analyse_morph', models.TextField(null=True)),
                ('est_valide', models.BooleanField(default=False)),
                ('pos_tag', models.CharField(choices=[('L', 'حرف'), ('N', 'اسم'), ('V', 'فعل'), ('P', 'ضمير')], max_length=1, null=True)),
                ('lemma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lemme')),
            ],
        ),
        migrations.AddField(
            model_name='lemme',
            name='niveau',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.niveau'),
        ),
        migrations.AddField(
            model_name='lemme',
            name='synonymes',
            field=models.ManyToManyField(related_name='synonymes', to='core.lemme'),
        ),
        migrations.AddField(
            model_name='lemme',
            name='synonymes_valides',
            field=models.ManyToManyField(related_name='synonymes', to='core.lemme'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='mot',
            field=models.ForeignKey(max_length=15, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lemme'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.TextField()),
                ('est_valide', models.BooleanField(default=False)),
                ('lemma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lemme')),
            ],
        ),
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.TextField()),
                ('est_valide', models.BooleanField(default=False)),
                ('lemme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lemme')),
            ],
        ),
        migrations.CreateModel(
            name='conjugaison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_valide', models.BooleanField(default=False)),
                ('prnm_je', models.CharField(max_length=30)),
                ('prnm_nous', models.CharField(max_length=30)),
                ('prnm_tu_M', models.CharField(max_length=30)),
                ('prnm_tu_F', models.CharField(max_length=30)),
                ('prnm_vous_2M', models.CharField(max_length=30)),
                ('prnm_vous_PM', models.CharField(max_length=30)),
                ('prnm_vous_PF', models.CharField(max_length=30)),
                ('prnm_il', models.CharField(max_length=30)),
                ('prnm_elle', models.CharField(max_length=30)),
                ('prnm_ils_2', models.CharField(max_length=30)),
                ('prnm_ils_P', models.CharField(max_length=30)),
                ('prnm_elles_P', models.CharField(max_length=30)),
                ('temps', models.CharField(choices=[('A', 'الماضي'), ('B', 'المضارع'), ('C', 'المضارع المنصوب'), ('D', 'الماضي المبني للمجهول'), ('E', 'المضارع المبني للمجهول'), ('F', 'المضارع المجزوم'), ('G', 'الأمر')], max_length=1, null=True)),
                ('lemme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.lemme')),
            ],
        ),
        migrations.AddIndex(
            model_name='lemme',
            index=models.Index(fields=['lemme'], name='core_lemme_lemme_602bb6_idx'),
        ),
        migrations.AddIndex(
            model_name='lemme',
            index=models.Index(fields=['id'], name='core_lemme_id_a679d4_idx'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='niveau',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.niveau'),
        ),
    ]
