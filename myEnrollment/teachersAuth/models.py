from django.db import models
# Followed the tutorial https://www.youtube.com/watch?v=PUzgZrS_piQ&list=PLlameCF3cMEu-LbsQYUDUVkiZ2jc2rpLx
from django_countries.fields import CountryField
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, AbstractUser # AbstractUser, AbstractBaseUser

# We need to add username as required field in order to create the superuser on CLI
# Because of that we have to override create_superuser()
class CustomUserManager(BaseUserManager):
    #use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            password= password,
            email=self.normalize_email(email),
            **extra_fields
        )
        # change password to hash,
        # tested we still have to do in serializer - I guess this is related
        # to saving user from admin ?
        user.set_password(password)
        #user.profile_picture = profile_picture
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        user = self.model(
            first_name= first_name,
            last_name= last_name,
            password= password,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

# Create your models here.
class Teacher(AbstractUser):
    class Meta:
        verbose_name = ('Nastavnik')
        verbose_name_plural = ('Nastavnici')
        ordering = ['email']
    # Django by default creates username as unique and as USERNAME_FIELD, we have to override it
    username= None
    country= CountryField(default='BA')
    email= models.CharField(max_length = 50, unique= True)
    password= models.CharField(max_length = 255)
    objects = CustomUserManager()

    # We want that Django logs in with email and password
    USERNAME_FIELD = 'email'
    EMAIL_FIELD= 'email'
    # Required fields is used by createsuperuser(), no need for username_field and password
    # AbstractUser has fields which we can use for superuser()
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return f'{self.email}'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)