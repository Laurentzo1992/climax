import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.conf import settings
from api.models import Employee, Profession

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        filename, extension = os.path.splitext(filepath)
        if extension.lower() in ['.csv', '.json', '.txt']:
            handle_file(filepath, extension.lower())

def handle_file(filepath, extension):
    if extension == '.csv':
        df = pd.read_csv(filepath)
    elif extension == '.json':
        df = pd.read_json(filepath)
    elif extension == '.txt':
        df = pd.read_csv(filepath, delimiter='\t')
    
    for index, row in df.iterrows():
        # Traiter et enregistrer les données dans la base de données
        employee, created = Employee.objects.get_or_create(
            nom=row['nom'],
            prenom=row['prenom'],
            age=row['age']
        )
        profession, created = Profession.objects.get_or_create(
            libelle=row['libelle'],
            description=row['description']
        )
        # Associer l'employé à la profession
        employee.profession = profession
        employee.save()

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=settings.MEDIA_ROOT, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
