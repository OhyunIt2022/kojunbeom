

from django.contrib import admin

from bookmarkapp.models import Bookmark
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')
