from django.contrib import admin
from product.models import Book, User
from django.utils import timezone


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "auther", "is_draft", "day_since_creation")
    list_filter = ("is_draft", )
    search_fields = ("title", )
    prepopulated_fields = {"slug":("title",)}
    actions = ("set_book_to_published", )
    fields = (("title", "slug"), "body", "is_draft")
    list_per_page = 50


    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("title", "-date_created")
        return ("title", )
    

    def day_since_creation(self, book):
        diff = timezone.now() - book.date_created()
        return diff.days
    day_since_creation.short_description = "days active!"
    
    
    def set_book_to_published(self, request, queryset):
        count = queryset.update(is_draft=False)
        self.message_user(request, "{}the selected books have been published".format(count))

    set_book_to_published.short_description = "mark selected book as published"    

admin.site.register(Book, BookAdmin)
admin.site.register(User)