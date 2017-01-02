from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CrowdFundingMemberGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserExtendedForFunding(models.Model):

    USER_TYPE = [('FR', "Facilitator"), ('MR', "Member"),]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    funding_amout = models.DecimalField(max_digits=5, decimal_places=2)
    group_type = models.ForeignKey(CrowdFundingMemberGroup)
    user_type = models.CharField(max_length=2,
        choices=USER_TYPE, blank=True
    )

class CrowdFundingProposalSettings(models.Model):
    proposal_success_perc = models.IntegerField()

class CrowdFundingPostProposal(models.Model):

    STATE = [('DT', "Draft"), ('CD', "Closed"),]
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_datetime = models.DateTimeField(
            default=timezone.now)
    published_datetime = models.DateTimeField(
            blank=True, null=True)
    end_date = models.DateField(
            blank=True, null=True)
    state = models.CharField(max_length=2,
        choices=STATE, default='DT'
    )

    def publish(self):
        self.published_datetime = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CrowdFundingProposalVoting(models.Model):
    UP = 'UP'
    DOWN = 'DN'
    VOTE_TYPE = [(UP, "Upvote"), (DOWN, "DownVote")]
    author = models.ForeignKey('auth.User')
    created_datetime = models.DateTimeField(
            default=timezone.now)
    vote_type = models.CharField(max_length=2,
        choices=VOTE_TYPE, blank=True

    )
    proposal_id = models.ForeignKey(CrowdFundingPostProposal, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.proposal_id