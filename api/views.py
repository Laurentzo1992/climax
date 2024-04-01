from django.shortcuts import redirect, render
from .forms import UploadFileForm
from .models import Employee, Profession
import pandas as pd
from django.db.models import Avg


# Fonction d'affichage des employes
def employee(request):
    employes = Employee.objects.all().order_by('-created')
    return render(request, 'api/employe.html', {"employes":employes})

# Fonction d'affichage des statitiques
def statistique(request):

    moyenne_salaires_par_type_profession = Employee.objects.values('profession__libelle').annotate(moyenne_salaire=Avg('sal_employee'))

    return render(request, 'api/statistique.html', {"moyenne_salaires_par_type_profession": moyenne_salaires_par_type_profession})


# Fonction de gestion des fichiers d'import de données
def handle_uploaded_file(file):
    df = pd.read_csv(file, header=None)
    for index, row in df.iterrows():
        nom = row[0]
        prenom = row[1]
        age = row[2]
        sal_employee = row[4]
        libelle_profession = row[3]
        
        profession, created = Profession.objects.get_or_create(
            libelle=libelle_profession
        )
        
        employee, created = Employee.objects.get_or_create(
                nom=nom,
                prenom=prenom,
                age=age,
                sal_employee=sal_employee,
                profession=profession
            )
        


# Vue d'interface d'import coté utilisateur
def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('employee')
    else:
        form = UploadFileForm()
    return render(request, 'api/home.html', {'form': form})



