from django.db import models
from django.utils import timezone


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