from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz)  # admin page에서 Quiz 모델을 CRUD할 수 있다.