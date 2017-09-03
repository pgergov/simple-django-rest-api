from django.conf.urls import url

from .views import GoodsListApi


urlpatterns = [
    url(
        regex=r'^list/$',
        view=GoodsListApi.as_view(),
        name='list'
    )
]
