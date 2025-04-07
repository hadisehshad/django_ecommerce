# Django Ecommerce Project

A fully-featured ecommerce platform built using **Django** and **Django Rest Framework (DRF)**, designed to handle product management, user authentication, and shopping cart functionalities.

![django_ecommerce_logo](https://img.icons8.com/ios/452/shopping-cart.png)

---

## Features

- **JWT-based user authentication:** Login, registration, and token-based authentication.
- **Product Management:** Add, update, delete, and view products.
- **Categories Management:** Organize products into categories.
- **Shopping Cart:** Add and remove products, view cart, and checkout.
- **Best-selling products:** Display top-selling products.
- **User Statistics:** View total users and paid carts.
- **Testimonials:** Add and manage user testimonials.
  
---

## Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
</p>

---

## Installation & Setup

Follow the steps below to set up the project locally:

### 1. Clone the repository
```bash
git clone git@github.com:hadisehshad/django_ecommerce.git
cd django_ecommerce


2. Create a virtual environment
It’s recommended to use a virtual environment to isolate dependencies.

# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install project dependencies
pip install --upgrade pip
pip install -r requirements.txt

4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (for accessing the Django admin panel)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver

Visit the app at http://127.0.0.1:8000

Visit the admin panel at http://127.0.0.1:8000/admin

---

API Endpoints
Authentication
POST /account/api/token: Obtain JWT access and refresh tokens.

POST /account/api/token/refresh: Refresh the JWT access token.

POST /account/api/v1/register_or_login/: Register a new user or login.

POST /account/api/v1/send_code/: Send a verification code.

Shop
GET /shop/api/v1/manage_categories: Show, add, and delete categories.

POST /shop/api/v1/manage_products: Create, update, and delete products.

GET /shop/api/v1/product_list: Display a list of all products.

GET /shop/api/v1/product_detail/<product_id>: Get product details by ID.

POST /shop/api/v1/add_to_cart: Add a product to the cart.

GET /shop/api/v1/show_cart: View the contents of the user's cart.

POST /shop/api/v1/checkout: Checkout and process the payment.

Home
GET /home/api/v2/testimonials: Get and create testimonials.

GET /home/api/v2/testimonials/<id>: Retrieve or update a testimonial by ID.

DELETE /home/api/v2/testimonials/delete/<id>: Delete a testimonial.
---

Swagger UI & Redoc
API Documentation is available at:

Swagger UI

Redoc
---

## ðŸ“œ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

Mockup Demo Sketch


+--------------------------------------------------------------+
|                         Django Ecommerce                     |
|           A Modular Ecommerce Platform with JWT Auth         |
+-------------------+        DRF        +----------------------+
|                   |------------------>|                      |
|   Account App     |                   |      Shop App        |
|-------------------|                   |----------------------|
|   Register        |                   |   Manage Products    |
|   Login           |                   |   Add to Cart        |
|   Logout          |                   |   Show Cart          |
|   Send Reset Code |                   |   Checkout           |
+-------------------+        JWT Token  +----------------------+
                        Access + Refresh Tokens