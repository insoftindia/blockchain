from django.contrib import admin
from .models import CrowdFundingPostProposal, CrowdFundingProposalVoting

admin.site.register(CrowdFundingPostProposal)
admin.site.register(CrowdFundingProposalVoting)