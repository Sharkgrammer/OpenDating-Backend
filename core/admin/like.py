from django.contrib import admin


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', "created_user", 'liked_user', 'liked_returned', "created_date", "deleted"
    )

    ordering = ('-id',)
