from django.contrib import admin
from testapp.models import MessageModel

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display=['message','user_name','time']
admin.site.register(MessageModel,MessageAdmin)
