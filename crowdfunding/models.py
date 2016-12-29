from django.db import models
from django.utils import timezone
# from vote.managers import VotableManager

class CrowdFundingPostProposal(models.Model):

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