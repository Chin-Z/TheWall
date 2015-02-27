from django.contrib import admin
from webwalls.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ['body', 'create_time']

admin.site.register(Message, MessageAdmin)