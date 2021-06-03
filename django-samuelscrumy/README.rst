=====
samuelscrumy
=====

Django-samuelscrumy is a Django app that helps you create goals and goal status with web based authentication and authorization.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "samuelscrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'samuelscrumy',
    ]

2. Include the samuelscrumy URLconf in your project urls.py with a namespace of samuelscrumy like this::

    path('samuelscrumy/', include('samuelscrumy.urls', namespace='samuelscrumy')),

3. Run ``python manage.py migrate`` to create the samuelscrumy models.

4. Start the development server and visit http://127.0.0.1:8000/samuelscrumy/ to register, to login navigate to http://127.0.0.1:8000/samuelscrumy/accounts/login/,
then visit  http://127.0.0.1:8000/admin/ to create goals and goal statuses (you'll need the Admin app enabled) , and then navigate to  http://127.0.0.1:8000/samuelscrumy/home to check all available goals

5. Visit http://127.0.0.1:8000/samuelscrumy/addgoal to create a new goal. 