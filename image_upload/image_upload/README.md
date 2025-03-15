# Django Image Upload and Gallery

## Description

This project is a simple Django application that allows users to upload images, view them in a gallery, and delete them if necessary. The project uses PostgreSQL as the database and implements basic functionality for image management, including listing, uploading, and deleting images. Optionally, you can expose an API using Django Rest Framework.

## Prerequisites

Before running this project, ensure that you have the following installed:

- Python 3.x
- PostgreSQL
- Git

# Setting up the Project

1. Clone the repository

Start by cloning this repository to your local machine:

git clone https://github.com/RemeMboup/image-upload.git
cd image-upload

2. Create and activate a virtual environment
It's a good practice to use a virtual environment to manage dependencies.


python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

3. Install the dependencies
Install the required dependencies listed in requirements.txt:

pip install -r requirements.txt

4. Set up PostgreSQL
Ensure that PostgreSQL is installed and running. Create a new database for this project:

# In PostgreSQL
CREATE DATABASE db_test_upload;

5. Update your settings.py to include your PostgreSQL database configuration. In your settings.py, change the DATABASES configuration as follows:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_test_upload',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
6. Apply the migrations
Run the following command to create the necessary database tables:

python manage.py migrate

7. Create a superuser
If you'd like to access the Django admin interface, create a superuser:

python manage.py createsuperuser

8. Run the development server
Start the Django development server:


python manage.py runserver
Now, you can access the project at http://127.0.0.1:8000/.