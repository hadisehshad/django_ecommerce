# ?? Django Ecommerce Platform

![Ecommerce Dashboard](https://miro.medium.com/max/1400/1*ZdpddX3zJhL6h4v4Z4S1jw.png)

A modern, full-featured ecommerce solution built with Django and DRF, featuring JWT authentication, product management, and shopping cart functionality.

---

## ? Key Features

<div align="center">

| Feature Category | Icon | Description |
|------------------|------|-------------|
| **Authentication** | ?? | JWT-based secure user authentication |
| **Product Management** | ?? | Full CRUD operations for products |
| **Category System** | ??? | Hierarchical product categorization |
| **Shopping Cart** | ?? | Persistent cart functionality |
| **Analytics** | ?? | Sales and user statistics |
| **Reviews** | ? | Product testimonials system |

</div>

---

## ?? Technology Stack

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="60" title="Django"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" title="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="60" title="PostgreSQL"/>
  <img src="https://jwt.io/img/pic_logo.svg" width="60" title="JWT"/>
  <img src="https://www.django-rest-framework.org/img/logo.png" width="120" title="DRF"/>
</div>

---

## ?? Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver

Access the application at: http://localhost:8000
Admin panel: http://localhost:8000/admin

?? API Documentation
Authentication Endpoints
Method	Endpoint	Description
POST	/api/auth/register/	User registration
POST	/api/auth/login/	User login
POST	/api/auth/token/refresh/	Refresh JWT token
Product Endpoints
Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Create new product
GET	/api/products/{id}/	Product details
Cart Endpoints
Method	Endpoint	Description
GET	/api/cart/	View cart contents
POST	/api/cart/add/	Add item to cart
DELETE	/api/cart/remove/	Remove item from cart

?? Interactive API docs available at:

Swagger UI: /swagger/

ReDoc: /redoc/

?? Project Structure
django-ecommerce/
??? accounts/            # Authentication app
??? products/            # Product management
??? cart/                # Shopping cart logic
??? static/              # Static files
??? templates/           # HTML templates
??? manage.py            # Django CLI
??? requirements.txt     # Dependencies


?? Screenshots
<div align="center"> <img src="https://via.placeholder.com/400x225/3d5a80/ffffff?text=Product+Page" width="45%"> <img src="https://via.placeholder.com/400x225/3d5a80/ffffff?text=Shopping+Cart" width="45%"> </div>
?? License
This project is licensed under the MIT License - see the LICENSE.md file for details.

?? Contact
For questions or support, please contact:

?? Email: your.email@example.com
?? Website: https://yourwebsite.com
?? LinkedIn: Your Name

<div align="center"> <img src="https://img.icons8.com/fluency/96/000000/shopping-cart.png" alt="Cart Icon"> <img src="https://img.icons8.com/color/96/000000/django.png" alt="Django Icon"> </div> ```

