from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import CustomUser, AdminUser, TeacherUser, StudentUser
from .models import Classes, Subjects,Options,Correct_options, Exams, Questions, TeacherSubjects

class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(AdminUser)
admin.site.register(TeacherUser)
admin.site.register(StudentUser)
admin.site.register(Subjects)
admin.site.register(Correct_options)
admin.site.register(Classes)
admin.site.register(Exams)
admin.site.register(Options)
admin.site.register(Questions)
admin.site.register(TeacherSubjects)

