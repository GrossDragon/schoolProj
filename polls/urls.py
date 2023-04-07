from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info,name='info'),
    path('book/<int:book_id>/<int:to_buy>', views.book, name='book'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('publisher/<int:publisher_id>/', views.publisher, name='publisher'),
    path('basket',views.basket ,name='basket' ),
    path('buy',views.buy,name='buy')

    
    
]