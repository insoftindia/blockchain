from django import forms
from .models import CrowdFundingPostProposal, Comment

class CrowdFundingPostProposalForm(forms.ModelForm):

    class Meta:
        model = CrowdFundingPostProposal
        fields = ('title', 'text','amount', 'end_date')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)