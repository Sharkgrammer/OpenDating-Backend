from django.contrib import admin


class UserImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'date_upload'
    )

    search_fields = ('id', 'user')
    ordering = ('-id', 'user', 'date_upload')
