from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import *
from django.shortcuts import get_object_or_404
from account.models import User, ShoppingCart, CartItems
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from django.db.models import Sum


# Create your views here.


class ManageCategoryView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        if not name:
            return Response({'error': 'field name is required'}, status=status.HTTP_400_BAD_REQUEST)
        category = Category.objects.create(name=name)
        return Response({'message': 'successfully'}, status=status.HTTP_200_OK)

    # {'id': 2}
    def delete(self, request):
        id = request.data.get('id')
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response({'message': 'successfully'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


class ManageProductView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        return Response({'error': 'your data is not valid'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'error': 'product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'fail'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'error': 'product id is required'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, id=product_id)
        if 'category' in request.data:
            product.category = request.data['category']
        if 'name' in request.data:
            product.name = request.data['name']
        if 'description' in request.data:
            product.description = request.data['description']
        if 'stock' in request.data:
            product.stock = request.data['stock']
        if 'price' in request.data:
            product.price = request.data['price']
        if 'image' in request.data:
            product.image = request.data['image']
        if 'specification' in request.data:
            product.specification = request.data['specification']
        product.save()
        serializer = ProductSerializer(product)
        return Response({'message': 'product updated successfully', 'product': serializer.data},
                        status=status.HTTP_200_OK)


class ManageCartsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        user_carts = []

        for user in users:
            carts = ShoppingCart.objects.filter(user=user)
            user_carts_data = {
                'user': {
                    'phone_number': user.phone_number,
                    'carts': []
                }
            }
            for cart in carts:
                cart_items = CartItems.objects.filter(cart=cart)
                cart_items_data = CartItemSerializer(cart_items, many=True).data
                cart_data = {
                    'created_at': cart.created_at,
                    'is_paid': cart.is_paid,
                    'items': cart_items_data,
                }
                user_carts_data['user']['carts'].append(cart_data)
            user_carts.append(user_carts_data)
        return Response(user_carts, status=status.HTTP_200_OK)


class Users_Statistic(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.count()
        total_is_paid = ShoppingCart.objects.filter(is_paid=True).count()
        total_revenue = 0
        paid_carts = ShoppingCart.objects.filter(is_paid=True)
        for cart in paid_carts:
            cart_items = CartItems.objects.filter(cart=cart)
            for item in cart_items:
                total_revenue += item.product.price * item.quantity

        data = {
            "total_users": total_users,
            "total_is_paid": total_is_paid,
            "total_revenue": total_revenue
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, product_id):
        products = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        product = get_object_or_404(Product, id=product_id)

        cart, created = ShoppingCart.objects.get_or_create(user=request.user, is_paid=False)
        cart_items, created = CartItems.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_items.quantity += int(quantity)
        else:
            cart_items.quantity = int(quantity)

        cart_items.save()

        return Response({'message': 'product added to cart'}, status=status.HTTP_200_OK)


class ShowCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = get_object_or_404(ShoppingCart, user=request.user, is_paid=False)
        cart_items = CartItems.objects.filter(cart=cart)
        cart_items_data = CartItemSerializer(cart_items, many=True).data

        cart_data = {
            'created_at': cart.created_at,
            'is_paid': cart.is_paid,
            'items': cart_items_data
        }
        return Response(cart_data, status=status.HTTP_200_OK)


class DeleteFromCart(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        item_id = request.data.get('item_id')
        cart_item = get_object_or_404(CartItems, id=item_id, cart__user=request.user, cart__is_paid=False)
        cart_item.delete()
        return Response({'message': 'item removed from cart'}, status=status.HTTP_200_OK)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = get_object_or_404(ShoppingCart, user=request.user, is_paid=False)
        if cart.cartitems_set.count() == 0:
            return Response({'error': 'your cart is empty'})

        cart.is_paid = True
        cart.save()
        return Response({'message': 'Checkout successful'}, status=status.HTTP_200_OK)


class ProductFilterView(APIView):
    def get(self, request):
        filter_backends = [DjangoFilterBackend]
        filterset = ProductFilter(request.GET, queryset=Product.objects.all())

        if filterset.is_valid():
            serializer = ProductSerializer(filterset.qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return render({'error': 'not valid'}, status=status.HTTP_400_BAD_REQUEST)


class BestSellingProductsView(APIView):
    def get(self, request):
        best_selling_products = Product.objects.annotate(
            total_sales=Sum('cartitems__quantity')
        ).order_by('-total_sales')[:10]

        serializer = ProductSerializer(best_selling_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
        return Response({'notifications': notifications.values()}, status=status.HTTP_200_OK)
