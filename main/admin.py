from django.contrib import admin
from .models import Book, User, Like, Report


# Register your models here.


@admin.action(description="Mark selected reports as resolved")
def mark_as_resolved(modeladmin, request, queryset):
    queryset.update(resolved=True, action_taken="ignored")

@admin.action(description="Delete reported book and mark as resolved")
def delete_book_and_resolve(modeladmin, request, queryset):
    for report in queryset:
        if report.book:
            report.book.delete()
            report.resolved = True
            report.action_taken = "book_deleted"
            report.save()

class ReportAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "book", "resolved", "action_taken")
    list_filter = ("resolved", "action_taken")
    actions = [mark_as_resolved, delete_book_and_resolve]


admin.site.register(Book)
admin.site.register(Like)
admin.site.register(User)
admin.site.register(Report, ReportAdmin)
