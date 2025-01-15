from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class ProfilUzytkownika(models.Model):
    uzytkownik = models.OneToOneField(User, on_delete=models.CASCADE)
    limit_budzetu = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.uzytkownik.username

class CelOszczednosciowy(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)
    kwota_docelowa = models.DecimalField(max_digits=10, decimal_places=2)
    obecna_kwota = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Transakcja(models.Model):
    TYP_TRANSAKCJI = (
        ('przychod', 'Przychód'),
        ('wydatek', 'Wydatek'),
    )

    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True)
    typ = models.CharField(max_length=10, choices=TYP_TRANSAKCJI)
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.uzytkownik.username} - {self.typ}: {self.kwota} ({self.kategoria})"

class Budzet(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    miesiac = models.DateField()
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budżet: {self.kategoria} ({self.miesiac})"

class Powiadomienie(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc = models.TextField()
    przeczytane = models.BooleanField(default=False)
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Powiadomienie dla {self.uzytkownik.username}: {self.tresc}"