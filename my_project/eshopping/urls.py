from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop, name = 'shop'),
    path('demo',views.demo, name = 'demo'),
    path('create_profile/', views.createUser, name = 'create_profile'),
    path('create_author/',views.author_profile, name='create_author' ),
    path('create_publisher/',views.publisher_profile, name='create_publisher' ),
    path('create_book/',views.books_profile, name='create_book' ),
    path('book_info/',views.books_info, name='book_info' ),
    path('', views.main, name='main'),
]