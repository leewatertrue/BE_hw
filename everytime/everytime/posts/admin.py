from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Scrap)
admin.site.register(Like)