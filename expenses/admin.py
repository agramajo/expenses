from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'source')
    list_filter = ('author', 'publish', 'source')
    search_fields = ('title',)
    date_hierarchy = 'publish'
    ordering = ('publish','source')

#admin.site.register(Expense)

