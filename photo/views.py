from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Photo
# Create your views here.




class AlbumLV(ListView):
    model = Album
    
    # context_object_name = 'object_list' 이것도 기본값. 보낼 값 지정할 수도 있음. lion_object_name처럼
    # template_name = 'photo/album_list.html' #이게 기본값.
    
    #listview의 기본 템플릿 : 앱이름/모델이름_list.html
    # context = {'object_list': ~~~}
    #listview는 그냥 다가져옴

    # def get_queryset(self) -> QuerySet[Any]:
    #     return self.model.objects.all()

    # def get_object(self): #DETAIL에서 씀

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)

class AlbumDV(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'
    # pk를 통해서 특정 앨범만 가져온다. 
    # detailview는 특정한 그 값들가져옴.


class PhotoDV(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'