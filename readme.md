# Registration System
## With that project, you can add, delete and edit a person to system

**Features:**
- All pages was done using the Class Based Views (CBV);
- Page of Login ( _only users created in admin area can access_ )
- Only superuser can delete from website;
- Login/Logout;
- Page Created using Bootstrap 4
- Database SQLite3;
- Search bar to find a user
- Greeting to the user at the header;
- Add person to SQLite3;
- Edit person from SQLite3;
- Delete person from SQLite3;

**Thanks to:**
- https://www.djangoproject.com/ - for providing the Django Framework 
- https://colorlib.com/ - for providing the free login page with boostrap 4
- https://www.bootstrapcdn.com/ - for providing the Bootstrap 4 CDN to use in page
- https://django-bootstrap-form.readthedocs.io - for providing the free bootstrap to use in form
- https://docs.python.org/3/library/datetime.html - for providing the free library to datetime to LOG
- https://pillow.readthedocs.io/en/stable/ - to providing the Pillow library for free.
- https://github.com/henriquebastos/python-decouple - to create a way to set the sensitive variables

**How to setup the System in your computer**
- Clone the project to your computer
- with VENV enabled, run the command `pip install -r requirements-dev.txt`
- Create a file '.env' in your root directory of project, and set the `SECRET_KEY=` and the `DEBUG=`
- Run the server `python manage.py runserver`
- Open your favorite browser and type the URL - http://localhost:8080 or http://127.0.0.1:8080
- Create a superuser with the command `python manage.py createsuperuser`
- Use the user created to login in System.
