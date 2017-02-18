from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'content')

    def has_add_permission(self, request, obj = None):
        return False

    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Message, MessageAdmin)
