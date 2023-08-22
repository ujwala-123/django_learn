from django.contrib import admin
from .models import Course
from .models import Student
from .models import Author
from .models import Publisher
from .models import User
from .models import Books

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "enrolled_courses")
admin.site.register(Student,StudentAdmin)
admin.site.register(Course)

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Books)

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
admin.site.register(User, UserAdmin)


