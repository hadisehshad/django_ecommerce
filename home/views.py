from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


# Create your views here.


class TestimonialListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت‌شده می‌توانند ایجاد کنند
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TestimonialDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]  # فقط کاربران احراز هویت‌شده می‌توانند مشاهده، ویرایش  کنند
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class TestimonialDeleteView(APIView):
    """
    این ویو فقط به ادمین‌ها اجازه حذف نظرات را می‌دهد
    """
    permission_classes = [IsAdminUser]

    def delete(self, request, pk, *args, **kwargs):
        try:
            testimonial = Testimonial.objects.get(pk=pk)
            testimonial.delete()
            return Response({"message": "Testimonial deleted successfully"}, status=status.HTTP_200_OK)
        except Testimonial.DoesNotExist:
            return Response({"error": "Testimonial not found"}, status=status.HTTP_404_NOT_FOUND)
