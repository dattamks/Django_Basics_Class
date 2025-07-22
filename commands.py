# Install Django

pip install django

# check libraries
pip freeze

#uninstall all libraries
pip freeze | xargs pip uninstall -y

#to add all installed libraries to requirements.txt
pip freeze > requirements.txt


##### Django Related Commands

# Create Django Project
django-admin startproject projectname .

# to start a django server
python manage.py runserver

# to create an app
 python manage.py startapp appname