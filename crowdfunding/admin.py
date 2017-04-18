from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CrowdFundingMemberGroup, UserExtendedForFunding, CrowdFundingProposalSettings, CrowdFundingPostProposal, CrowdFundingProposalVoting, Comment

class UserExtendedForFundingInline(admin.StackedInline):
    model = UserExtendedForFunding
    can_delete = False
    verbose_name_plural = 'userextending'

class UserAdmin(BaseUserAdmin):
    inlines = (UserExtendedForFundingInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(CrowdFundingProposalSettings)
admin.site.register(CrowdFundingPostProposal)
admin.site.register(CrowdFundingProposalVoting)
admin.site.register(CrowdFundingMemberGroup)
admin.site.register(Comment)