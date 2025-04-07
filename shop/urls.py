from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('api/v1/manage_categories', ManageCategoryView.as_view()),  # show and add and delete categories
    path('api/v1/manage_products', ManageProductView.as_view()),
    # show - create - delete - update Product model objects
    path('api/v1/manage_carts', ManageCartsView.as_view()),  # Manage carts: Show all carts for users
    path('api/v1/users_statistic', Users_Statistic.as_view()),
    # Users statistics: Show total users and paid carts statistics
    path('api/v1/product_list', ProductListView.as_view()),  # Product list: Show all products
    path('api/v1/product_detail/<int:product_id>', ProductDetailView.as_view()),
    # Product detail: Show details of a specific product by product_id
    path('api/v1/add_to_cart', AddToCartView.as_view()),  # Add to cart: Add a product to the user's shopping cart
    path('api/v1/show_cart', ShowCartView.as_view()),  # Show cart: Show the content of the user's shopping cart
    path('api/v1/delete_from_cart', DeleteFromCart.as_view()),
    # Delete from cart: Remove an item from the user's shopping cart
    path('api/v1/show_categories', CategoryListView.as_view()),  # Show categories: Display all product categories
    path('api/v1/checkout', CheckoutView.as_view()),  # Checkout: Process the payment and mark the cart as paid
    path('api/v1/filter/', ProductFilterView.as_view()),  # Product filter: Filter products based on various criteria
    # START V2-------------------------------------------------------------------------------------------------------
    path('api/v2/best_selling', BestSellingProductsView.as_view()),
    # best-selling products: Show the top-selling products
    path('api/v2/notifications', NotificationView.as_view()),  # Notifications: Show notifications for the user

]
