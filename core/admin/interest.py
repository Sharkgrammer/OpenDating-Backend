from django.contrib import admin


class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'category'
    )

    search_fields = ('id', 'title')
    ordering = ('-id',)
