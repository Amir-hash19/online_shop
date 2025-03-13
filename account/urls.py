from django.urls import path
from account.views import show_landing

urlpatterns = [
    path("", show_landing),

]