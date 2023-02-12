=====
Team
=====

Team is a Django app to manage team members such as Add,Remove in an Organization

To be installed Softwares- Python,Pip,Django

Quick start
-----------
To install the app package,run the command with app package 

python -m pip install --user django-team-0.1.tar.gz

After testing,you can uninstall the app package by running below command

python -m pip uninstall django-team

1. Add "team" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'team',
    ]

2. Include the team URLconf in your project urls.py like this::

    path('', include('team.urls')),

3. Run ``python manage.py migrate`` to create the team models.

4. Run ``python manage.py createsuperuser`` to create a superadmin for this app.

4. Run ``python manage.py runserver`` to start the application

5. Visit http://127.0.0.1:8000/ and login as superadmin

6. Create a team user with appropriate data and permission.

7. To edit a team member data,click the user and modify the properties. To delete, click the delete button in edit page.

8. A team member can login to the app by first registering and then login with the registered credentials.While registering, the email address should be the same as team user email address