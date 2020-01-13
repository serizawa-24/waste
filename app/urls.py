from django.urls import path,include

from .models import Item,F_Item
from .views import sendmail,C_View,F_View,ItemFilterView,F_ItemCreateView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

# アプリケーションのルーティング設定

urlpatterns = [
    path('sendmail/', sendmail, name='sendmail'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('C_View/',C_View,name = 'C_View'),
    path('F_View/',F_View,name = 'F_View'),
    path('f_create/', F_ItemCreateView.as_view(template_name='app/item_form.html'), name='F_create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('', ItemFilterView.as_view(), name='index'),
    
]
