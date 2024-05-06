from django.urls import path
from .views import MyDataView

urlpatterns = [
    path('my-data/', MyDataView.as_view(), name='my-data'),
]