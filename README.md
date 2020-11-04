# django_forms_with_ajax
## Table of Contents

- [About](#about)
- [Installing](#installing)
- [Usage](#usage)

## About <a name = "about"></a>

JavaScript integration - Ajax - with Python and Django

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [installing](#installing) for notes on how to installing the project your system.

### Prerequisites

Python, Django and JavaScript

```
pip install django
```

### Installing <a name = "installing"></a>
    virtualenv .venv
    source .venv/bin/actvate #Linux/Mac
    .venv/Scripts/activate #Windows
    pip install -r requirements.txt

### Migration:
    python manage.py makemigrations
    python manage.py migrate
### Create superuser:
    python manage.py createsuperuser
    username: ...
    password: ...



End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

    python manage.py runserver
