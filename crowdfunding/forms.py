from django import forms
from .models import CrowdFundingPostProposal

class CrowdFundingPostProposalForm(forms.ModelForm):

    class Meta:
        model = CrowdFundingPostProposal
        fields = ('title', 'text','amount', 'end_date')