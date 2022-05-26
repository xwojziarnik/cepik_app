🇬🇧

# Cepik App

## Table of contents:

- [The aim of the project](#the-aim-of-the-project)
- [What is our motivation?](#motivation)
- [Features](#features)
- [Technologies](#technologies)
- [Documentation](#documentation)
- [Team](#team)
- [Installation & setup](#installation--setup)
- [Run](#run)


## The aim of the project

REST API application where user can <details><summary><b>CRUD</b></summary>(Create / Read / Update / Delete)</details> on vehicles or driving licenses registered in Poland in specified time.

## What is our motivation?

We want to:
- Get to know Django framework better,
- Try to work in a team as a developers,
- Write an app using public API,
- Consolidate things we have learned at course

Also this is our project for graduate [Python od podstaw](https://sdacademy.pl/kursy/python/) course organized by [Software Development Academy](https://sdacademy.pl/).

## Features

- [] Listing interesting facts on home page,
- [] CRUD on vehicles registered in Poland,
- [] CRUD pn driving licences registered in Poland,

## Technologies

- Python 3,
- Django Framework,
- SQLite 3,
- Bootstrap,

## Doceumentation

- [Python 3](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/4.0/)
- [SQLite 3](https://www.sqlite.org/docs.html)
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

## Team
<details>
<summary>Click to get links and visit us on LinkedIn!</summary>

- [Dawid Gapiński](https://www.linkedin.com/in/dgapinski)
- [Łukasz Kacik](https://www.linkedin.com/in/%C5%82ukasz-kacik-093691224/)
- [Patryk Skonieczny](https://www.linkedin.com/in/pskonieczny33/)
- [Wojciech Ziarnik](https://www.linkedin.com/in/wojciech-ziarnik-23ba971a1)

</details>

## Installation & setup

1.Installation:

- Python:

Visit https://www.python.org/downloads/ and type which installing package you prefer (by your operating system) and download the package.

After download, go through installation process.

After above, let's check if Python is installed on your computer. To do this, open your terminal or command prompt and type:

For MacOS/Linux:
```
python3 --version
```

For Windows:
```
python --version
```


- [Virtual environment](https://docs.python.org/3/library/venv.html):

Open terminal/command prompt and create directory where you will create a django project using commands below:

```
ls                                                   # to check content of your domain directory
mkdir <directory_name>                               # to create a separated directory for project
cd <directory_name>                                  # just to go into new directory
python3 -m venv <virtualenv_name>                    # to create virtualenv using MacOS terminal
python -m venv <virtualenv_name>                     # to create virtualenv on Windows
source <virtualenv_name>/bin/activate                # to activate virtualenv on MacOS
<virtualenv_name>\Scripts\activate                   # to activate virtualenv on Windows

(<virtualenv_name>) <username>@<actual_directory> %  # after above you should see the (<virtualenv_name>). This line appears on MacOS.
```

- Django:

If you did above tutorials, now you should have scheme of your files like:

```
Desktop/
    <directory_name>/
        <virtualenv_name>
```

Now we can install Django framework. Simply type in your terminal/command prompt:

```
pip3 install django     # on MacOS
pip install django      # on Windows
```

To check if it's installed correctly, type:
```
python3 -m django --version     # on MacOS
python -m django --version      # on Windows
```

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

Perfect! Now, it's time to last episode.

##  Run

We've seen how to run venv. Keep that running!

Now, we can create new project and apps in our project, like this:

```
django-admin startproject <project_name> .      # Pro-tip: write a dot in the end of the command to create project IN CURRENT directory. Otherwise Django will create subdirectory and then will create project files in subdirectory.
```
Let's check what upper command created:
```
Desktop/
    <directory_name>/
        <virtualenv_name>
        manage.py
        <project_name>/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
```

Now all we need is our first app. So we have to type command:
```
python3 manage.py startapp <app_name>       # on MacOS
python manage.py startapp <app_name>        # on Windows
```

Now, our scheme of files looks something like below:
```
Desktop/
    <directory_name>/
        <virtualenv_name>
        manage.py
        <project_name>/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
```

Now, you can check if everything is correct. In this case type command:
```
python3 manage.py runserver     # using MacOS
python manage.py runserver      # using Windows
```

.. or we can simply clone this repo, and see if it's working on our machine (in case we did everything above count creating virtualenv):
```
git init                                                # to initialize repository
git clone https://github.com/xwojziarnik/cepik_app      # to clone this repository into your local machine

python3 manage.py runserver     # using MacOS
python manage.py runserver      # using Windows
```

And that's it! Great job!
