from django.db import models

    
class Profession(models.Model):
    libelle = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    modified = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
    
class Employee(models.Model):
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    profession = models.ForeignKey(Profession, blank=True, null=True, on_delete=models.CASCADE)
    sal_employee = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    modified = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)