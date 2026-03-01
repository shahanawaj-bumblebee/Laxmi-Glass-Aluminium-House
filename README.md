# 🏠 Laxmi Glass & Aluminium House — Business Website

A full-stack Django web application for **Laxmi Glass & Aluminium House**, a premium fabrication business offering aluminium, glass, ACP sheet, HPL sheet, UPVC, and interior design services located in Dadri, Uttar Pradesh, India.

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [Live Demo](#-live-demo)
3. [Features](#-features)
4. [Tech Stack](#-tech-stack)
5. [Project Structure](#-project-structure)
6. [Models & Database](#-models--database)
7. [URL Routes](#-url-routes)
8. [Installation & Setup](#-installation--setup)
9. [Running the Application](#-running-the-application)
10. [Admin Panel](#-admin-panel)
11. [Deployment (Heroku)](#-deployment-heroku)
12. [Environment Variables](#-environment-variables)
13. [Contributing](#-contributing)
14. [Contact](#-contact)

---

## 🏗 Project Overview

This project is the official business website for **Laxmi Glass & Aluminium House**. It serves as a digital showcase of the company's services, portfolio, and contact information. Customers can browse the company's offerings, view completed projects, submit enquiries, and request free quotes directly through the website.

---

## 🌐 Live Demo

> Deployed on **Heroku** via `Procfile` with `gunicorn`.
> The app runs in production using **WhiteNoise** for static file serving.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Hero Slider** | Auto-advancing image slider with manual prev/next navigation and dot indicators |
| **Portfolio Gallery** | Masonry-style grid showcasing completed projects |
| **Services Showcase** | Cards for Aluminium Windows, Glass Work, ACP Sheet, HPL Sheet, UPVC, and Interior Design |
| **Testimonials** | Dynamic customer reviews loaded from the database |
| **Contact Form** | Submissions are saved to the database and visible in the admin panel |
| **Get Free Quote** | Dedicated quote request form with service-type selection, stored in the database |
| **Google Maps Embed** | Embedded map showing the business location |
| **Floating WhatsApp Button** | One-click WhatsApp contact button on every page |
| **AOS Animations** | Scroll-triggered fade/slide animations powered by AOS.js |
| **Django Admin** | Full CRUD management for Services, Testimonials, Contact Messages, and Quote Requests |
| **Responsive Design** | Mobile-friendly layout using CSS Flexbox and Grid |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3 · Django 5.2 |
| **Database** | SQLite (development) |
| **Frontend** | HTML5 · CSS3 · Vanilla JavaScript |
| **CSS Animations** | AOS (Animate On Scroll) v2.3.4 |
| **Icons** | Font Awesome 6.5 |
| **Fonts** | Google Fonts — Montserrat |
| **Static Files** | WhiteNoise 6 |
| **Image Handling** | Pillow |
| **WSGI Server** | Gunicorn |
| **Deployment** | Heroku (Procfile) |

---

## 📁 Project Structure

```
Laxmi-Glass-Aluminium-House/
│
├── manage.py                     # Django management entry point
├── requirements.txt              # Python dependencies
├── Procfile                      # Heroku deployment config
├── db.sqlite3                    # SQLite database
│
├── laxmiglass_project/           # Django project settings package
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI entry point
│   └── asgi.py                   # ASGI entry point
│
├── website/                      # Main Django application
│   ├── models.py                 # Database models
│   ├── views.py                  # View logic
│   ├── urls.py                   # App URL patterns
│   ├── admin.py                  # Admin panel configuration
│   ├── apps.py                   # App configuration
│   ├── migrations/               # Database migration files
│   ├── static/
│   │   └── website/
│   │       ├── css/style.css     # Main stylesheet
│   │       ├── js/main.js        # Main JavaScript
│   │       └── images/           # Static images
│   └── templates/
│       └── website/
│           ├── base.html         # Base template (navbar + footer)
│           ├── index.html        # Home page
│           ├── about.html        # About page
│           ├── products.html     # Products page
│           ├── services.html     # Services page
│           ├── contact.html      # Contact page
│           ├── portfolio.html    # Portfolio page
│           └── get_quote.html    # Free quote request page
│
├── media/                        # User-uploaded media files
└── staticfiles/                  # Collected static files (production)
```

---

## 🗄 Models & Database

### `Service`
Stores the services offered by the business.

| Field | Type | Description |
|---|---|---|
| `name` | CharField | Service name |
| `image` | ImageField | Service image |
| `price` | DecimalField | Starting price |
| `description` | TextField | Detailed description |

### `Testimonial`
Stores customer reviews displayed on the home page.

| Field | Type | Description |
|---|---|---|
| `name` | CharField | Customer name |
| `review` | TextField | Review text |
| `rating` | IntegerField | Rating (1–5, default 5) |
| `image` | ImageField | Optional customer photo |

### `ContactMessage` *(New)*
Stores every contact form submission for admin review.

| Field | Type | Description |
|---|---|---|
| `name` | CharField | Sender's name |
| `email` | EmailField | Sender's email |
| `mobile` | CharField | Sender's phone number |
| `message` | TextField | Message body |
| `submitted_at` | DateTimeField | Auto-timestamp of submission |

### `QuoteRequest` *(New)*
Stores free quote requests submitted by potential customers.

| Field | Type | Description |
|---|---|---|
| `name` | CharField | Requester's name |
| `email` | EmailField | Requester's email |
| `mobile` | CharField | Requester's phone |
| `service_type` | CharField | Service required (choices) |
| `description` | TextField | Project details |
| `budget` | CharField | Optional budget range |
| `submitted_at` | DateTimeField | Auto-timestamp |
| `is_resolved` | BooleanField | Admin follow-up status |

---

## 🔗 URL Routes

| URL | View | Name | Description |
|---|---|---|---|
| `/` | `home` | `home` | Home page with slider, portfolio, services, contact form, and testimonials |
| `/about/` | `about` | `about_us` | About/Why Choose Us page |
| `/products/` | `products` | `products` | Products catalogue page |
| `/services/` | `services` | `services` | Services listing page |
| `/contact/` | `contact` | `contact_us` | Contact form (saves to DB) |
| `/portfolio/` | `portfolio` | `portfolio` | Portfolio gallery page |
| `/get-quote/` | `get_quote` | `get_quote` | Free quote request form |
| `/admin/` | Django Admin | — | Administration panel |

---

## ⚙ Installation & Setup

### Prerequisites

- Python 3.10+
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/shahanawaj-bumblebee/Laxmi-Glass-Aluminium-House.git
cd Laxmi-Glass-Aluminium-House
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files (for production)

```bash
python manage.py collectstatic
```

---

## ▶ Running the Application

### Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Production (Gunicorn)

```bash
gunicorn laxmiglass_project.wsgi
```

---

## 🔐 Admin Panel

Access the Django admin panel at `/admin/` after creating a superuser.

**Manageable models:**

- **Services** — Add/edit/delete services shown on the website
- **Testimonials** — Manage customer reviews
- **Contact Messages** — View all contact form submissions (read-only fields)
- **Quote Requests** — View and manage quote requests; toggle `is_resolved` directly from the list view

---

## 🚀 Deployment (Heroku)

The `Procfile` is already configured:

```
web: gunicorn laxmiglass_project.wsgi
```

**Deployment steps:**

```bash
# Login to Heroku
heroku login

# Create a Heroku app
heroku create your-app-name

# Push to Heroku
git push heroku main

# Run migrations on Heroku
heroku run python manage.py migrate

# Create superuser on Heroku
heroku run python manage.py createsuperuser
```

---

## 🔑 Environment Variables

> ⚠ For production, set the following environment variables instead of hardcoding them in `settings.py`.

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames |
| `DATABASE_URL` | PostgreSQL URL (for Heroku production DB) |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📞 Contact

**Laxmi Glass & Aluminium House**

- 📞 +91-8920912449
- 📞 +91-7906232665
- ✉️ laxmi2glass@gmail.com
- 📍 GGVR+758, Katheda Rd, Pink City Colony, Dadri, Uttar Pradesh 203207

---

*Built with ❤ using Django*
