from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Member

class MemberListView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, 'members/member_list.html', {'members': members})

class MemberDetailView(View):
    def get(self, request, member_id):
        member = get_object_or_404(Member, id=member_id)
        return render(request, 'members/member_detail.html', {'member': member})