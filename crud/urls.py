from django.urls import path
from crud.views import index,add,edit,update,delete

urlpatterns = [
    path('index/',index,name='index'),  
    path('add/',add,name='add'),
    path('edit/',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]
