from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = patterns('',
#     url(r'^/add/?$', SlideAssetAddView.as_view(), name='slide_asset_add'),
    url(r'', include('umanage.change_email.urls')),
    url(r'', include('umanage.change_password.urls')),
#     url(r'^/(?P<slide_asset_id>\d+)/?$', SlideAssetView.as_view(), name='slide_asset_view'),
#     url(r'^/(?P<slide_asset_id>\d+)/edit/?$', SlideAssetEditView.as_view(), name='slide_asset_edit'),
)
