# City Hospital Django Project

## Project Overview

This project is a Django-based hospital website for City Hospital. It showcases a modern healthcare brand, lists departments and doctors, and allows visitors to submit appointment bookings. The site is designed as a front-end clinic website with a small data model and admin-managed content.

The project includes:

- A landing page with promotional content and a hero carousel
- About page with hospital information and statistics
- Department listing page
- Doctor listing page with department-based doctor records
- Contact page with contact details and a visual contact form layout
- Appointment booking form connected to a Django model
- Booking confirmation page after successful form submission
- Admin dashboard for managing departments, doctors, and bookings

## Technology Stack

- Python
- Django 5.2.7
- SQLite database
- Bootstrap 5 for layout and styling
- Crispy Forms with Bootstrap 5 template pack
- Pillow for doctor image uploads
- HTML, CSS, and JavaScript

## Project Structure

```text
django_tutorial/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── PROJECT_DOCUMENTATION.md
├── README.md
├── django_tutorial/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       ├── 0001_initial.py
│       ├── 0002_doctors.py
│       ├── 0003_alter_doctors_doc_spec.py
│       └── 0004_alter_doctors_doc_spec_booking.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── booking.html
│   ├── confirmation.html
│   ├── contacts.html
│   ├── department.html
│   └── doctors.html
├── static/
│   ├── css/
│   ├── images/
│   └── js/
└── uploads/
    └── doctor/
```

## Main App: home

The `home` app is the core application of the project. It contains:

- Models for departments, doctors, and booking records
- A custom appointment form
- Views for home, about, booking, doctors, department, and contact pages
- URL routes for the public website
- Admin registration for data management

## Configuration

The project configuration is defined in `django_tutorial/settings.py`.

### Installed apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'crispy_forms',
    'crispy_bootstrap5',
]
```

### Database

The application uses SQLite for development:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Static files and media

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/media/'
```

This allows local static assets and uploaded doctor images to be served during development.

## Models

### departments

The `departments` model stores hospital departments.

Fields:

- `dep_name` - Department name
- `dep_description` - Department description

Methods:

- `__str__()` returns the department name

### doctors

The `doctors` model stores doctor details and links each doctor to a department.

Fields:

- `doc_name` - doctor's full name
- `doc_spec` - specialization
- `dep_name` - foreign key to a department
- `doc_image` - uploaded profile image

Specializations include:

- Dermatologist
- Cardiologist
- Neurologist
- Psychologist
- Paediatrician

### booking

The `booking` model stores patient appointment requests.

Fields:

- `p_name` - patient name
- `p_phone` - patient phone number
- `p_email` - patient email
- `doc_name` - selected doctor
- `booking_date` - requested appointment date
- `booked_on` - date when booking was created automatically

## Forms and Booking Flow

The booking form is defined in `home/forms.py`.

Features:

- Uses a Django `ModelForm`
- Uses a date input widget for `booking_date`
- Includes custom labels for patient and doctor fields
- Saves appointment data when the form is valid

Booking view flow:

1. User opens the booking page
2. The view creates an empty form
3. User submits the appointment data
4. The form is validated
5. If valid, the booking is saved
6. User is redirected to the confirmation page

## URL Routes

Main project URLs are in `django_tutorial/urls.py` and app routes are in `home/urls.py`.

Routes:

- `/` - home page
- `/about/` - about page
- `/booking/` - appointment booking form
- `/doctors/` - doctor listing page
- `/department/` - department listing page
- `/contacts/` - contact page
- `/admin/` - Django admin dashboard

## Views

The `home/views.py` file contains the main logic:

- `index(request)` - renders the home page
- `about(request)` - renders the about page
- `booking(request)` - handles booking form display and submission
- `doctors(request)` - fetches all doctors and passes them to the template
- `department(request)` - fetches all departments and passes them to the template
- `contacts(request)` - renders the contact page

## Templates

The templates folder contains the front-end pages:

- `base.html` - shared header, navigation, footer, and page skeleton
- `index.html` - landing page content and banner carousel
- `about.html` - hospital story and stats
- `doctors.html` - doctor cards and doctor details
- `department.html` - department display page
- `booking.html` - appointment form
- `confirmation.html` - successful booking confirmation
- `contacts.html` - contact information and contact form layout

## Admin Panel

The admin configuration is in `home/admin.py`.

Registered models:

- `departments`
- `doctors`
- `booking`

The booking model uses a custom admin configuration that displays:

- ID
- Patient name
- Phone number
- Email
- Doctor
- Booking date
- Booked date

This makes it easy to review appointment requests from the admin interface.

## Migrations

The project includes these migrations:

- `0001_initial.py` - creates `departments`
- `0002_doctors.py` - creates `doctors`
- `0003_alter_doctors_doc_spec.py` - updates specialization choices
- `0004_alter_doctors_doc_spec_booking.py` - updates field adjustments and creates `booking`

## Setup Instructions

### 1. Activate the virtual environment

On Windows PowerShell:

```powershell
cd "c:\Users\User\adwaith\django tutorial"
.\djvenv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Apply migrations

```powershell
python manage.py migrate
```

### 4. Create an admin user

```powershell
python manage.py createsuperuser
```

### 5. Run the development server

```powershell
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Notes and Limitations

This project is a learning/demo application, and a few areas can be improved for production use:

- `DEBUG` is enabled in `settings.py`
- `ALLOWED_HOSTS` is empty
- Secret key is hardcoded and should be moved to environment variables
- The contact form is currently a visual-only layout and does not save or send messages
- Booking form validation can be improved for better user feedback
- There are no automated tests yet
- Static/media setup is development-oriented rather than production-ready

## Summary

This project demonstrates a simple but complete Django website for a hospital. It uses Django models, templates, URL routing, admin management, Bootstrap styling, and form handling to create a functional front-end medical appointment system. It is an excellent example of beginner-level Django application development with real database-backed content.
