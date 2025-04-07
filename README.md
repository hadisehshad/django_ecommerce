# 🛍️ Django Ecommerce Platform

![Ecommerce Dashboard](https://miro.medium.com/max/1400/1*ZdpddX3zJhL6h4v4Z4S1jw.png)

A modern, full-featured ecommerce solution built with Django and DRF, featuring JWT authentication, product management, and shopping cart functionality.

---

## ✨ Key Features

<div align="center">

| 🧩 Feature | 🔍 Description |
|-----------|----------------|
| 🔐 **Authentication** | Secure JWT-based user login & registration |
| 📦 **Product Management** | Full CRUD for products |
| 🏷️ **Category System** | Organized product categorization |
| 🛒 **Shopping Cart** | Persistent and dynamic cart logic |
| 📈 **Analytics** | Real-time sales/user metrics |
| ⭐ **Reviews** | Customer feedback and ratings |

</div>

---

## 🛠 Technology Stack

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="60" title="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" title="Python"/>
  <img src="https://jwt.io/img/pic_logo.svg" width="60" title="JWT"/>
  <img src="https://www.django-rest-framework.org/img/logo.png" width="120" title="DRF"/>
</div>

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Virtualenv

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.
env\Scripts ctivate   # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Run database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Access: [http://localhost:8000](http://localhost:8000)  
Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔐 API Endpoints Overview

### 🔑 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login user |
| POST | `/api/auth/token/refresh/` | Refresh JWT token |

### 📦 Product
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List products |
| POST | `/api/products/` | Create new product |
| GET | `/api/products/{id}/` | Product details |

### 🛒 Cart
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/cart/` | View cart |
| POST | `/api/cart/add/` | Add to cart |
| DELETE | `/api/cart/remove/` | Remove from cart |

📚 API Docs:  
- Swagger: `/swagger/`  
- ReDoc: `/redoc/`

---

## 🗂 Project Structure

```
django-ecommerce/
├── accounts/            # User authentication
├── products/            # Product management
├── cart/                # Shopping cart
├── static/              # Static files
├── templates/           # HTML templates
├── manage.py            # Project CLI
└── requirements.txt     # Python dependencies
```

---

## 📸 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/400x225/3d5a80/ffffff?text=Product+Page" width="45%">
  <img src="https://via.placeholder.com/400x225/3d5a80/ffffff?text=Shopping+Cart" width="45%">
</div>

---

## 📜 License
MIT License - see `LICENSE.md`

---

## ✉️ Contact

- 📧 Email: your.email@example.com  
- 🌐 Website: https://yourwebsite.com  
- 💼 LinkedIn: Your Name

<div align="center">
  <img src="https://img.icons8.com/fluency/96/000000/shopping-cart.png" alt="Cart Icon">
  <img src="https://img.icons8.com/color/96/000000/django.png" alt="Django Icon">
</div>
