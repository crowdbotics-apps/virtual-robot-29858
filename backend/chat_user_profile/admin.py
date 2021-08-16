from django.contrib import admin
from .models import Profile, VerificationCode, Contact

admin.site.register(Contact)
admin.site.register(VerificationCode)
admin.site.register(Profile)

# Register your models here.
