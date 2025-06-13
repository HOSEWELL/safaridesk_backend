# 🧾 Ticket Booking API

A simple, RESTful Ticket Booking System built with Django and Django REST Framework. Users can register, log in, view available tickets, and book them. The system ensures only registered users can book a ticket.

## 🚀 Features

### 🧑‍💻 Accounts
- User registration (first name, last name, gender, date of birth, email, password)
- User login using email and password
- Authentication with token (DRF Token Auth)

### 🎫 Tickets
- Create and list available travel tickets (departure, destination, and date of departure)

### 🧾 Booking
- Book a ticket by providing your email, name, and phone
- Validates whether the email exists in the user database before allowing booking
- View all bookings
- Search and view bookings made by email

---

## 🛠 Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (default) / any other relational DB
- Token Authentication

---

## 📁 Project Structure

project/
│
├── accounts/ # User registration and login
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── tickets/ # Ticket creation and booking
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── ticketing/ # Django project configuration
│ ├── settings.py
│ └── urls.py
│
├── db.sqlite3
└── manage.py



## 🔑 API Endpoints

### Auth
| Method | Endpoint             | Description          |
|--------|----------------------|----------------------|
| POST   | `/api/accounts/register/` | Register a new user |
| POST   | `/api/accounts/login/`    | Login with email and password |

### Tickets
| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| GET    | `/api/tickets/`          | List all tickets available      |
| POST   | `/api/tickets/`          | Create a new ticket for booking    |

### Bookings
| Method | Endpoint                    | Description                       |
|--------|-----------------------------|-----------------------------------|
| POST   | `/api/book/`                | Book a ticket                     |
| GET    | `/api/bookings/`            | View all booked tickets                |
| GET    | `/api/bookings/<email>/`    | View bookings by user email       |


