from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serialiser import UserSerializer, UserSerialiserWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.conf import settings
import http.client
from rest_framework.response import Response
from .models import CustomUser, TeacherUser, AdminUser, StudentUser, Classes

# Create your views here.


#  user Login with Jwt authentications
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerialiserWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# studnet Register 

@api_view(['POST'])
def StudentRegister(request):

    image = request.FILES['image']
    password = request.data['password']
    lastName = request.data['lastName']
    firstName = request.data['firstName']
    email = request.data['email']
    phoneNumber = request.data['phoneNumber']
    semester = request.data['semester']
    roll_no = request.data['roll_no']
    gender = request.data['gender']

    print(password)
   
    # try :
    #     user = CustomUser.objects.create_user(image = email=email, gender=gender, username=username, user_type='Student', first_name=firstName, last_name=lastName, password=password)
    #     user.studentuser.roll_no = values['roll_no']
    #     semesterName = Classes.objects.get(class_name=semester)
    #     user.studentuser.class_name = semesterName
    #     user.save()
    #     return Response('studnet Register successfully ')
    # except :
    #     return Response('studnet Register error accurd')


    return Response('Helo from studnet Register')