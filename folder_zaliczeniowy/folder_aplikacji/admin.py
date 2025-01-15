from django.contrib import admin

from .models import ProfilUzytkownika, CelOszczednosciowy, Transakcja, Budzet, Powiadomienie

# Register your models here.
admin.site.register(ProfilUzytkownika)
admin.site.register(CelOszczednosciowy)
admin.site.register(Transakcja)
admin.site.register(Budzet)
admin.site.register(Powiadomienie)