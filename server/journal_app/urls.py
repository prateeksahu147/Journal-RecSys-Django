from django.urls import path
from .views.home import * 

urlpatterns = [
    path('',get_latest_jounal, name='home-view'),
    #path('<str:model>/<str:feature>', select_model, name='select-model'),
    #path('detail/<str:journal_id>', get_journal , name='journal-detail'),
    #path('<str:model>/<str:feature>/', get_latest_jounal , name='journal')
    path('detail/<str:model>/<str:feature>/<str:journal_id>', get_journal, name='detail-view')
    ]

