from django.contrib import admin
from . models import Student, Admin, Schedule, User, MealStatus
# Register your models here.
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Schedule)
admin.site.register(User)
admin.site.register(MealStatus)