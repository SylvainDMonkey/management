# Django commands

# Activate / Deactivate
venv\Scripts\activate.bat
venv\Scripts\deactivate.bat

# 1.Vérifier la version de Django :
python -m django --version

# 2.Commencer un projet :
django-admin startproject nomDuProjet

# 3.Démarrer l'application depuis le dossier contenant le fichier manage.py :
python manage.py runserver (0:8000) => Optionnel : permet de changer le port du serveur

# 4.Pour créer une application :
python manage.py startapp nomApplication

# 5.Pour créer des migrations :
python manage.py makemigrations => inclut toutes les modèles de l'application
python manage.py makemigrations nomModel => => inclut uniquement le modèle de l'application renseignée

# 6.Pour valider la migration vers la base de données :
python manage.py migrate => inclut toutes les modèles de l'application
python manage.py migrate nomModel => => inclut uniquement le modèle de l'application renseignée

# 7.Pour reverse une migration :
python manage.py migrate <migration_name> => <migration_name> serait le numéro de migration comme 0001

# 8.Pour vérifier les modifications apportés par les migrations :
python manage.py sqlmigrate polls (0001) => Numéro du fichier qui s'incrémente à chaque migration incluse

# 9.(Optionnel) Pour vérifier sans inclure de migration le statut du projet :
python manage.py check

# 10.Pour utiliser l'API Django :
python manage.py shell

# 11. Pour créer un superutilisateur :
python manage.py createsuperuser

# 12. Pour vérifier les données en format JSON :
python manage.py dumpdata nomApp --options
python manage.py dumpdata nomApp --indent 4 > nomDossier(communément appelé fixtures)/nomApp.json => Permet d'importer un fichier Json de la BDD dans un dossier sous format JSON
django-admin dumpdata -o mydata.json.gz => Permet de compresser dans l’un des formats bz2, gz, lzma ou xz un fichier JSON compressé  de la BDD
```