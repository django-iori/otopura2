from django.contrib import admin
from django.db.models.fields.files import ImageField
from .models import *
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(HostModel)
admin.site.register(BandModel)
admin.site.register(GoodModel)
admin.site.register(CommentModel)
