from django.contrib import admin


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id', "sent_user", 'received_user', "created_date"
    )

    ordering = ('-id',)
