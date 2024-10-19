from django.contrib import admin


class InterestCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title'
    )

    search_fields = ('id', 'title')
    ordering = ('-id',)
