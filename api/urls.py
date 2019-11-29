from django.urls import path

from api.views import PageList

urlpatterns = [
    path('pages/', PageList.as_view(), name='page_list')
]