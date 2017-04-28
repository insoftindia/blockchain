from django import forms
from .models import CrowdFundingPostProposal, Comment
from django.contrib.auth.models import User

class CrowdFundingPostProposalForm(forms.ModelForm):

    class Meta:
        model = CrowdFundingPostProposal
        fields = ('title', 'text','amount', 'end_date')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']