from django.urls import path
from .views import MemberListView, MemberDetailView

urlpatterns = [
    path('', MemberListView.as_view(), name='member_list'),
    path('<int:member_id>/', MemberDetailView.as_view(), name='member_detail'),
]