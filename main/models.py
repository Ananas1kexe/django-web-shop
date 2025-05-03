from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField("Name", max_length=50, unique=True)
    description = models.CharField("Description", max_length=500)
    author = models.CharField("Author", max_length=50, default="not specified", blank=True)
    image = models.ImageField("Image", blank=True)
    text = models.FileField("Text")
    price = models.IntegerField("Price", default=0, validators=[MinValueValidator(0)])
    TOPICS = [
        ("Modern prose", "Modern prose"),
        ("Fantasy", "Fantasy"),
        ("Romantic fantasy", "Romantic fantasy"),
        ("Fighting fantasy", "Fighting fantasy"),
        ("Urban fantasy", "Urban fantasy"),
        ("Dark fantasy", "Dark fantasy"),
        ("Alternate history", "Alternate history"),
        ("Fanfic", "Fanfic"),
    ]
    
    
    topic = models.CharField("Topic", choices=TOPICS)
    def __str__(self):
        return self.title



class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("the username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("username", max_length=50, unique=True)
    password = models.CharField("password", max_length=255)
    avatar = models.ImageField("Avatar", blank=True)
    verify = models.BooleanField("Verify", default=False)
    blok = models.BooleanField("Block", default=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    objects = UserManager()
    
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "book")
        
        
        
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("name", max_length=50)
    reason = models.TextField("reason", max_length=350)
    note = models.TextField("note", max_length=350, blank=True)
    resolved = models.BooleanField(name="resolved", default=False)
    action_taken = models.CharField(name="action_taken", max_length=50, blank=True)
    created = models.DateTimeField("created", auto_now_add=True)
    R_REASONS = [
        ("vocr", "Violation of community rules"),
        ("soa", "Spam or advertisement"),
        ("obor", "Offensive behavior or language"),
        ("iopc", "Inappropriate or prohibited content"),
        ("fsosa", "Fraud, scam, or suspicious activity"),
        ("ibtod", "Inappropriate book title or description"),
        ("poci", "Plagiarism or copyright infringement"),
    ]
    
    r_reason = models.CharField("r_reason", choices=R_REASONS, blank=True)
    proof = models.ImageField("proof")
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)

    
    def __str__(self):
        return f"Report by {self.user.username}: {self.user}(crated: {self.created})"