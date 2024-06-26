from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#___________________________________________________________ProfileManager
class ProfileManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, username, email, password=None):
            if not email:
                  raise ValueError('Email required')
            
            if not username:
                  raise ValueError('Username required')
            
            user = self.model(
                  email       = self.normalize_email(email),
                  username    = username,
                  first_name  = first_name,
                  last_name   = last_name,
            )

            user.set_password(password)
            user.save(using=self._db)
            return user
      
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
                email         = self.normalize_email(email),
                username      = username,
                password      = password,
                first_name    = first_name,
                last_name     = last_name,
        )
        user.is_admin   = True
        user.is_staff   = True
        user.is_active  = True
        user.save(using=self._db)
        return user


#___________________________________________________________Profile
class Profile(AbstractBaseUser):
      '''
      Custom user model for user accounts.
      '''
      first_name        = models.CharField(max_length=50)
      last_name         = models.CharField(max_length=50)
      username          = models.CharField(max_length=50, unique=True)
      email             = models.EmailField(max_length=100, unique=True)
      phone_number      = models.CharField(max_length=50)
      
      # Required
      date_joined       = models.DateTimeField(auto_now_add=True)
      last_login        = models.DateTimeField(auto_now_add=True)
      is_admin          = models.BooleanField(default=False)
      is_staff          = models.BooleanField(default=False)
      is_active         = models.BooleanField(default=False)


      # Login with email
      USERNAME_FIELD    = 'email'
      REQUIRED_FIELDS   = ['username', 'first_name', 'last_name']

      objects = ProfileManager()

      def full_name(self):
            return f'{self.first_name} {self.last_name}'

      def __str__(self):
            return self.email

      def has_perm(self, perm, obj=None):
            return self.is_admin
      
      def has_module_perms(self, add_label):
            return True



#___________________________________________________________UserProfile
class UserProfile(models.Model):

      user              = models.OneToOneField(Profile, on_delete=models.CASCADE)
      address           = models.CharField(blank=True, max_length=100)
      profile_picture   = models.ImageField(blank=True, upload_to='userprofile/')
      address           = models.CharField(blank=True, max_length=50)
      city              = models.CharField(blank=True, max_length=20)
      country           = models.CharField(blank=True, max_length=20)
      
      def __str__(self):
            return self.user.first_name
      
      def full_address(self):
            return f'{self.address}'