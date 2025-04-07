from django.shortcuts import render
from django.template.defaultfilters import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTPCode, Person
from .utils import send_sms
import random
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta, datetime
from django.utils import timezone
from .serializers import PersonSerializer


# Create your views here.


class SendCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "phone number is requaired"}, status=status.HTTP_400_BAD_REQUEST)
        # حذف کدهای قدیمی‌تر از 3 دقیقه
        OTPCode.objects.filter(created_at__lt=datetime.now() - timedelta(minutes=3)).delete()
        otp_code, created = OTPCode.objects.get_or_create(phone_number=phone_number)
        code = str(random.randint(10000, 99999))
        otp_code.code = code
        otp_code.created_at = timezone.now()  # به‌روزرسانی زمان ایجاد
        otp_code.save()
        send_sms(phone_number=phone_number, code=code)
        return Response({'message': 'code sent'}, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        code = request.data.get("code")
        if not phone_number:
            return Response({"error": "phone number is requaired"}, status=status.HTTP_400_BAD_REQUEST)
        if not code:
            return Response({"error": "code is requaired"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            otp_code = OTPCode.objects.get(phone_number=phone_number, code=code)
            if not otp_code:
                return Response({"error": "otp code is not valid"})
            user, created = User.objects.get_or_create(phone_number=phone_number)
            otp_code.delete()
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)
        except OTPCode.DoesNotExist:
            return Response({"error": "otp code does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):
    #  دریافت اطلاعات پروفایل کاربر
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            person = Person.objects.get(user=request.user)
            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response({"error": "profile not found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data.copy()
        data["user"] = request.user.phone_number
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            person = Person.objects.get(user=request.user)
            serializer = PersonSerializer(person, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
