from django.urls import path
from wishlist.views import (show_wishlist_html, show_wishlist_xml, show_wishlist_json,
                            show_wishlist_json_by_id, show_wishlist_xml_by_id,
                            register, login_user, logout_user, show_wishlist_ajax,
                            create_wishlist_ajax)

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist_html, name='show_wishlist_html'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', show_wishlist_json_by_id, name='show_wishlist_json_by_id'),
    path('xml/<int:id>', show_wishlist_xml_by_id, name='show_wishlist_xml_by_id'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/logout/', logout_user, name='logout_ajax'),
    path('ajax/submit', create_wishlist_ajax, name='create_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]