# Generated by Django 4.1.4 on 2023-01-12 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import teachersAuth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secondarySchools', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('previous_login', models.DateTimeField(blank=True, null=True, verbose_name='previous login')),
                ('is_verified', models.BooleanField(default=False)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_code', to='secondarySchools.coursessecondaryschool')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_id', to='secondarySchools.secondaryschool')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Nastavnik',
                'verbose_name_plural': 'Nastavnici',
                'db_table': 'teachers',
                'ordering': ['email'],
            },
            managers=[
                ('objects', teachersAuth.models.CustomUserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='teacher',
            constraint=models.UniqueConstraint(fields=('id', 'email', 'course_code'), name='composite-pk-id-email-course'),
        ),
    ]
