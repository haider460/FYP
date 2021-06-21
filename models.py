from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.



class CustomUser(AbstractUser):
    user_type_data = (('Admin','Admin'),('Teacher','Teacher'),('Student','Student'))
    user_type = models.CharField(max_length=50, choices=user_type_data, default='Teacher')
    gender = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)


class AdminUser(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class TeacherUser(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



class TeacherSubjects(models.Model):
    teacher = models.ForeignKey(TeacherUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True, null=True)



class Classes(models.Model):
    class_name = models.CharField(max_length=255, blank=True, null=True)


class StudentUser(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.OneToOneField(Classes, on_delete=models.CASCADE, blank=True, null=True)


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    classes= ForeignKey(Classes, on_delete=models.CASCADE)




class Exams(models.Model):
    exam_name = models.CharField(max_length=255, null=True, blank=True)
    total_questions = models.CharField(max_length=255, null=True, blank=True)
    total_marks = models.CharField(max_length=255, null=True, blank=True)
    passing_marks = models.CharField(max_length=255, null=True)
    exam_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherUser, on_delete=models.CASCADE)




class Questions(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)



class Correct_options(models.Model):
    correct_option = models.CharField(max_length=255, null=True, blank=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)




class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=255, null=True, blank=True)
    option2 = models.CharField(max_length=255, null=True, blank=True)
    option3 = models.CharField(max_length=255, null=True, blank=True)
    option4 = models.CharField(max_length=255, null=True, blank=True)


   

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Admin':
            AdminUser.objects.create(admin=instance, profile_pic='')
        if instance.user_type == "Teacher":
            TeacherUser.objects.create(teacher=instance, profile_pic='')
        if instance.user_type == 'Student':
            StudentUser.objects.create(student=instance, profile_pic="", roll_no="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'Admin' :
        instance.adminuser.save()
    if instance.user_type == "Teacher" :
        instance.teacheruser.save()
    if instance.user_type == 'Student' :
        instance.studentuser.save()
