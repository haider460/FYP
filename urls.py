from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #  Student register
    path('student_register/', views.StudentRegister, name="student_register")

]