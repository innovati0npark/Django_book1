from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model=Bookmark

    # template_name="bookmark/bookmark_list.html" #appname/model_name_list.html  이게 제네릭 디폴트
    # context_object_name = "object_list" # object_list 

class BookmarkDV(DetailView):
    # 직접
    model=Bookmark
    # template_name = "bookmark/bookmark_detail.html" #appname/model_name_detail.html
    # context_object_name = "object"
    
    
    # def get_object(self):
    #generic view는 기본으로 설정된게 있어서 urls.py 만들때 규칙 따라야함.
        





    