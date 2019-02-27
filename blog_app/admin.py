from django.contrib import admin

# imports data from the models page
from .models import BlogPost

# Register your models here.

admin.site.register(BlogPost)


# username: admin
# password: test4321