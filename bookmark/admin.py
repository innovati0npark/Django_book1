from django.contrib import admin
from bookmark.models import Bookmark


# Register your models here.
# admin.site.register(Bookmark)
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'url')         #관리자 페이지서 보여주는 형태 변경



