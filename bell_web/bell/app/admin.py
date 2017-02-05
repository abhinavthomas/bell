from django.contrib import admin

# Register your models here.
from .models import bell
from .models import current

admin.site.register(bell)
admin.site.register(current)