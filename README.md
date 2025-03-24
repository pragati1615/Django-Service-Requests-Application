# Django Service Requests Application

## Project Description
This Django application is built for a gas utility company to handle customer service requests efficiently. The application enables customers to submit service requests online, track the status of their requests, and view their account information. It also provides customer support representatives with tools to manage and resolve customer requests.

## Features
- **Service Requests:** Customers can submit service requests, select the type of request, provide details, and attach files.
- **Request Tracking:** Customers can track the status of their service requests, including submission time and resolution time.
- **Admin Dashboard:** Customer support representatives can manage and resolve requests.
- **Authentication & Authorization:** Users can log in and access their service requests securely.

## Technologies Used
- **Backend:** Django (Python)
- **Database:** SQLite/PostgreSQL (configurable in `settings.py`)
- **API:** Django REST Framework (DRF)
- **Authentication:** Token-based authentication using DRF
- **Frontend (Optional):** Django Templates / React (if applicable)

## Installation & Setup
### Prerequisites
Ensure you have Python installed (Python 3.x recommended). Install `pip` and `virtualenv` if not installed.

### Steps to Install
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/django-service-requests.git
   cd django-service-requests
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations and start the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

## API Endpoints
### Authentication
- **Login:** `POST /api/auth/login/` (username, password required)
- **Logout:** `POST /api/auth/logout/`

### Service Requests
- **Create Request:** `POST /api/service-requests/` (requires authentication)
- **View Requests:** `GET /api/service-requests/` (returns a list of service requests)
- **Get Specific Request:** `GET /api/service-requests/{id}/`
- **Update Request:** `PUT /api/service-requests/{id}/`
- **Delete Request:** `DELETE /api/service-requests/{id}/`

## Project Structure
```
.
├── service_requests/         # Main Django app for handling service requests
│   ├── models.py            # Database models
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # URL configurations
│   ├── tests.py             # Unit tests
│
├── users/                   # Authentication app
│   ├── models.py            # User models
│   ├── views.py             # Auth API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # URL configurations
│
├── config/                  # Project-wide configurations
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL configuration
│   ├── wsgi.py              # WSGI entry point
│
├── db.sqlite3               # SQLite database (if used)
├── manage.py                # Django management script
└── requirements.txt         # Project dependencies
```

## How to Contribute
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to GitHub: `git push origin feature-name`
5. Create a pull request.

## License
This project is licensed under the MIT License.


