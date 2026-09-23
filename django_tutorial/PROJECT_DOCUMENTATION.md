# City Hospital Django Project

## 1. Project Overview

This project is a Django-based hospital website for **City Hospital**. It provides public pages for hospital information, departments, doctors, contact details, and appointment booking.

The application currently supports:

- A home page with a Bootstrap carousel and hospital introduction.
- About, departments, doctors, booking, and contact pages.
- Department records managed through Django models and the admin site.
- Doctor records linked to departments and displayed dynamically.
- Appointment booking through a Django `ModelForm`.
- Image uploads for doctor profiles.
- A booking confirmation page after a valid appointment form submission.
- Django admin management for departments, doctors, and bookings.

The project is configured as a development application using SQLite, local static files, and local media files.

## 2. Technology Stack

- Python
- Django 5.2.7, as declared in `requirements.txt`
- SQLite database
- Django Crispy Forms 2.6
- Crispy Bootstrap 5 2026.3
- Pillow 12.3.0 for image fields
- Bootstrap 5.1.3 loaded from a CDN
- Font Awesome 5 loaded from a CDN
- Custom CSS in `static/css/style.css`

The Django settings file contains a generated header referring to Django 6.0.7, while the installed dependency listed in `requirements.txt` is Django 5.2.7. Keep these versions aligned when setting up or upgrading the project.

## 3. Directory Structure

```text
django_tutorial/
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- PROJECT_DOCUMENTATION.md
|-- django_tutorial/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- home/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|   |-- migrations/
|       |-- __init__.py
|       |-- 0001_initial.py
|       |-- 0002_doctors.py
|       |-- 0003_alter_doctors_doc_spec.py
|       |-- 0004_alter_doctors_doc_spec_booking.py
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- about.html
|   |-- booking.html
|   |-- confirmation.html
|   |-- contacts.html
|   |-- department.html
|   |-- doctors.html
|-- static/
|   |-- css/style.css
|   |-- images/
|   |-- js/
|-- uploads/
|   |-- doctor/
```

## 4. Installation and Setup

### Prerequisites

- Python installed and available on the command line.
- Windows PowerShell or another terminal.
- The project folder opened in VS Code.

### Create or activate the virtual environment

The repository already contains a virtual environment named `djvenv`. Activate it in PowerShell from the repository root:

```powershell
.\djvenv\Scripts\Activate.ps1
```

If execution policy prevents activation, use the environment's Python executable directly or adjust the local PowerShell policy according to your machine's security rules.

### Install dependencies

From the Django project directory, run:

```powershell
pip install -r requirements.txt
```

### Apply migrations

```powershell
python manage.py migrate
```

### Create an administrator

```powershell
python manage.py createsuperuser
```

Follow the prompts for the username, email address, and password.

### Start the development server

```powershell
python manage.py runserver
```

Open the following URLs in a browser:

- Website: `http://127.0.0.1:8000/`
- Admin site: `http://127.0.0.1:8000/admin/`

## 5. Configuration

The main configuration is in `django_tutorial/settings.py`.

### Installed applications

The project uses Django's built-in applications plus:

- `home`
- `crispy_forms`
- `crispy_bootstrap5`

### Templates

The template directory is configured as:

```python
DIRS = ['templates']
```

Templates inherit from `templates/base.html`, which provides the navigation bar, Bootstrap resources, custom stylesheet, and footer.

### Database

The project uses SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Static files

Static files are served from `static/` during development:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

The main stylesheet is `static/css/style.css`. Images used by the pages are in `static/images/`.

### Uploaded media

Doctor images are uploaded into `uploads/doctor/` because the doctor model uses `upload_to='doctor'`.

```python
MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/media/'
```

The root URL configuration serves media files during development using Django's `static()` helper.

### Crispy Forms

The project uses the Bootstrap 5 Crispy Forms template pack:

```python
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

## 6. Data Model

The models are defined in `home/models.py`.

### `departments`

Stores hospital department information.

| Field | Type | Details |
|---|---|---|
| `id` | Auto-created primary key | Added by Django |
| `dep_name` | `CharField` | Maximum length 100 |
| `dep_description` | `TextField` | Department description |

The string representation returns the department name.

### `doctors`

Stores doctor information and associates each doctor with a department.

| Field | Type | Details |
|---|---|---|
| `id` | Auto-created primary key | Added by Django |
| `doc_name` | `CharField` | Maximum length 255 |
| `doc_spec` | `CharField` | Maximum length 50 in the latest migration |
| `dep_name` | Foreign key | References `departments`; cascade delete |
| `doc_image` | `ImageField` | Uploads to `uploads/doctor/` |

Allowed specializations are:

- Dermatologist
- Cardiologist
- Neurologist
- Psychologist
- Paediatrician

The string representation formats a doctor as `Dr.<name> -(<specialization>)`.

### `booking`

Stores patient appointment requests.

| Field | Type | Details |
|---|---|---|
| `id` | Auto-created primary key | Added by Django |
| `p_name` | `CharField` | Patient name, maximum length 255 |
| `p_phone` | `CharField` | Patient phone number, maximum length 10 |
| `p_email` | `EmailField` | Patient email address |
| `doc_name` | Foreign key | References `doctors`; cascade delete |
| `booking_date` | `DateField` | Requested appointment date |
| `booked_on` | `DateField` | Automatically set to the current date on save |

## 7. URL and View Reference

The project-level URL configuration is in `django_tutorial/urls.py`. It includes the `home` application URLs at the site root and exposes the admin site at `/admin/`.

The application URL configuration is in `home/urls.py`.

| URL | Name | View | Template or behavior |
|---|---|---|---|
| `/` | `home` | `index` | Renders `index.html` |
| `/about/` | `about` | `about` | Renders `about.html` |
| `/booking/` | `booking` | `booking` | Displays and processes the appointment form |
| `/doctors/` | `doctors` | `doctors` | Queries all doctors and renders `doctors.html` |
| `/department/` | `department` | `department` | Queries all departments and renders `department.html` |
| `/contacts/` | `contacts` | `contacts` | Renders `contacts.html` |
| `/admin/` | Django admin | Built-in admin | Provides model administration |

### Booking request flow

1. A user opens `/booking/` with a GET request.
2. The `booking` view creates an empty `bookingform`.
3. `booking.html` renders the form with Crispy Forms and a CSRF token.
4. The user submits the form with a POST request.
5. The form validates the submitted data.
6. If valid, the booking is saved to SQLite.
7. The user sees `confirmation.html`.
8. If invalid, the current view code falls through and creates a new empty form instead of redisplaying the submitted invalid form. This is a behavior to improve if field-level validation feedback is required.

## 8. Template Reference

### `base.html`

Shared layout for all pages. It contains:

- The City Hospital navigation bar.
- Links generated with Django's `{% url %}` tag.
- Bootstrap and Font Awesome CDN references.
- The project stylesheet.
- The emergency contact footer.

### `index.html`

The home page contains:

- A three-image Bootstrap carousel using `car1.jpg`, `car2.jpg`, and `car3.jpg`.
- A City Hospital introduction section.
- A link to the About page.

### `about.html`

Displays the hospital mission, a booking call-to-action, and static hospital statistics such as years of excellence, doctors, beds, and patients.

### `doctors.html`

Loops through the `doctors` context variable and displays each doctor's image, name, specialization, and department.

### `department.html`

Loops through the `dept` context variable and displays each department's name and description.

### `booking.html`

Displays the `bookingform` using `{{ form|crispy }}`. The form includes a date picker for `booking_date` and submits via POST.

### `confirmation.html`

Displays a confirmation message after a booking is saved successfully.

### `contacts.html`

Displays static contact details, an emergency call-to-action, and a contact form layout. The contact form currently has no Django view, action URL, model, or persistence logic, so submitting it does not process a message on the server.

## 9. Admin Site

The models are registered in `home/admin.py`:

- `departments`
- `doctors`
- `booking`

Bookings use a custom `BookingAdmin` configuration with this list display:

- ID
- Patient name
- Patient phone
- Patient email
- Doctor
- Booking date
- Booked date

Recommended content-management workflow:

1. Log in at `/admin/`.
2. Create departments first.
3. Create doctors and assign each doctor to a department.
4. Upload a doctor image when creating a doctor.
5. Review appointment requests under bookings.

## 10. Migrations

The `home` app has four migrations:

1. `0001_initial.py` creates the `departments` model.
2. `0002_doctors.py` creates the `doctors` model.
3. `0003_alter_doctors_doc_spec.py` adds specialization choices.
4. `0004_alter_doctors_doc_spec_booking.py` changes the specialization length and creates the `booking` model.

After changing models, generate and apply new migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 11. Testing and Diagnostics

The current `home/tests.py` file contains no automated tests yet.

Useful commands:

```powershell
python manage.py check
python manage.py test
python manage.py showmigrations
```

`check` validates Django configuration. `test` runs the project test suite. `showmigrations` displays migration status.

Recommended future tests include:

- Status-code tests for each public URL.
- Tests confirming departments and doctors appear in their pages.
- Valid and invalid booking form tests.
- A test confirming a valid booking is saved.
- A test confirming successful booking renders the confirmation page.
- Admin registration and uploaded-image behavior where appropriate.

## 12. Development Notes and Known Limitations

- `DEBUG = True`; this must be disabled in production.
- `ALLOWED_HOSTS` is empty and must be configured for deployed hostnames.
- The secret key is currently hard-coded in `settings.py`; move it to an environment variable before deployment and rotate the exposed development key.
- SQLite is suitable for development and small demos, but a production deployment may need PostgreSQL or another managed database.
- Static and media files are configured for development. Production should use a proper static collection and media-storage strategy.
- The contact form is currently visual only and does not send or store messages.
- The About page uses a hard-coded absolute local URL for its booking link; a Django URL tag would be more portable.
- The booking view should preserve and redisplay invalid submitted forms instead of replacing them with a blank form.
- Phone validation currently limits the field to ten characters but does not enforce a numeric format.
- There are no project-level automated tests yet.
- The model class names use lowercase names (`departments`, `doctors`, and `booking`). This works, but conventional Django projects normally use singular PascalCase names such as `Department`, `Doctor`, and `Booking`.
- Some templates reference Bootstrap Icons classes, but Bootstrap Icons are not explicitly loaded in `base.html`; those icons may not display unless another stylesheet provides them.

## 13. Typical Developer Workflow

```powershell
.\djvenv\Scripts\Activate.ps1
cd .\django_tutorial
python manage.py check
python manage.py migrate
python manage.py runserver
```

For model changes:

```powershell
python manage.py makemigrations home
python manage.py migrate
```

For a new administrator:

```powershell
python manage.py createsuperuser
```

For verification before sharing changes:

```powershell
python manage.py check
python manage.py test
```

## 14. Deployment Checklist

Before deploying this project:

- Set `DEBUG = False`.
- Store `SECRET_KEY` outside source control.
- Configure `ALLOWED_HOSTS`.
- Configure CSRF trusted origins where needed.
- Use a production database.
- Run `python manage.py collectstatic`.
- Configure a production web server and WSGI or ASGI service.
- Configure persistent media storage for doctor images.
- Add server-side handling for the contact form if it is needed.
- Add validation and tests for appointment dates, phone numbers, and duplicate or unavailable appointments.
- Review access control for patient booking data and admin accounts.

## 15. Project Entry Points

- Application command entry point: `manage.py`
- Django settings: `django_tutorial/settings.py`
- Root URL configuration: `django_tutorial/urls.py`
- WSGI entry point: `django_tutorial/wsgi.py`
- ASGI entry point: `django_tutorial/asgi.py`
- Main application: `home/`
- Shared templates: `templates/base.html`
- Main stylesheet: `static/css/style.css`
- Database: `db.sqlite3`
