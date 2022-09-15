from django.urls import path
from wishlist.views import (show_wishlist_html, show_wishlist_xml, show_wishlist_json,
                            show_wishlist_json_by_id, show_wishlist_xml_by_id )

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist_html, name='show_wishlist_html'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', show_wishlist_json_by_id, name='show_wishlist_json_by_id'),
    path('xml/<int:id>', show_wishlist_xml_by_id, name='show_wishlist_xml_by_id'),
]