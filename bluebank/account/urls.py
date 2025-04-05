from django.urls import path
from .views import display_home, create_account, display_account, remove_account

urlpatterns = [
    path("", display_home, name="display-home"),
    path("create-account", create_account, name="create-account"),
    path("display-account/<int:account_id>", display_account, name="display-account"),
    path("remove-account/<int:account_id>", remove_account, name="remove-account"),
]
