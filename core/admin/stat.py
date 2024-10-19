from django.contrib import admin


class StatAdmin(admin.ModelAdmin):
    list_display = (
        'id', "user", 'likes', 'dislikes', "days_on", "top_interests"
    )

    ordering = ('-id',)
