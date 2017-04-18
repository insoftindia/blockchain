from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class CrowdFundingMemberGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserExtendedForFunding(models.Model):

    USER_TYPE = [('FR', "Facilitator"), ('MR', "Member"),]
    FUNDING_TYPE =[('MR',"MemberFunding"),('GR',"GroupFunding"),]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_extented')
    funding_amout = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    group_type = models.ForeignKey(CrowdFundingMemberGroup, blank=True, null=True)
    user_type = models.CharField(max_length=2,
        choices=USER_TYPE, blank=True
    )
    user_image = models.ImageField(upload_to = 'image/', blank=True)
    funding_type = models.CharField(max_length=2,
        choices=FUNDING_TYPE, blank=True
        )
    ether_account_private_key = models.CharField(max_length=200, blank=True, null=True)
    history = HistoricalRecords()

class CrowdFundingProposalSettings(models.Model):
    proposal_success_perc = models.IntegerField()
    history = HistoricalRecords()

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
    group_type = models.ForeignKey(CrowdFundingMemberGroup, blank=True, null=True)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)
    history = HistoricalRecords()

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
    history = HistoricalRecords()

    def __str__(self):
        return 'Proposal={0}: Auther={1}'.format(self.proposal_id, self.author)

class Comment(models.Model):
    proposal_id = models.ForeignKey(CrowdFundingPostProposal, models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords()

    def __str__(self):
        return self.text
