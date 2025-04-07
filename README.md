# 🛍️ Django Ecommerce Platform


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


## 🚀 Features

- 🔐 JWT-based user authentication (Login & Register)  
- 🛒 Shopping cart with session-based persistence  
- 📦 Full CRUD for product listings  
- 🏷️ Product categories and tagging  
- 📈 Real-time analytics (sales, orders, users)  
- ⭐ Product reviews and ratings  
- 🛠️ Django Admin for managing products, orders, and users  
- 🔗 DRF-powered RESTful API

---


---

## 🛠 Technology Stack

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="60" title="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" title="Python"/>
  <img src="https://jwt.io/img/pic_logo.svg" width="60" title="JWT"/>
  <img src="https://www.django-rest-framework.org/img/logo.png" width="120" title="DRF"/>
</div>


---

## 🧪 Installation & Setup

Follow the steps below to run the project locally:

### 1. 📥 Clone the repository
```bash
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce
```

### 2. 🌀 Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### 4. 🔧 Environment setup
```bash
cp .env.example .env
```

### 5. 🛠️ Apply database migrations
```bash
python manage.py migrate
```

### 6. 👤 Create a superuser
```bash
python manage.py createsuperuser
```

### 7. 🚀 Run the server
```bash
python manage.py runserver
```

> Access App: [http://localhost:8000](http://localhost:8000)  
> Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔐 API Overview

Full interactive API docs available at:

- Swagger UI → `/swagger/`
- ReDoc → `/redoc/`

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---


<div align="center">
  <img src="https://img.icons8.com/fluency/96/000000/shopping-cart.png" alt="Cart Icon">
  <img src="https://img.icons8.com/color/96/000000/django.png" alt="Django Icon">
</div>
