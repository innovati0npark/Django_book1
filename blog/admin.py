from django.contrib import admin
from blog.models import Post


# Register your models here.
# admin.site.register(Bookmark)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'modify_dt', 'tag_list')         #관리자 페이지서 보여주는 형태 변경
    list_filter = ('modify_dt', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':("title", )} #관리자에서 slug가 title내용 그대로 받아옴.

    # 추가
    def get_queryset(self, request):                
        return super().get_queryset(request).prefetch_related('tags')       #오버라이딩
    
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())