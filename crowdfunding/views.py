from django.contrib.auth.decorators import login_required
from .models import CrowdFundingPostProposal, CrowdFundingProposalVoting
from .forms import CrowdFundingPostProposalForm
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.db.models import Count

# Create your views here.

@login_required(login_url='/')
def crowdfunding(request):
    posts = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now()).order_by('published_datetime')
    return render(request, 'crowdfunding/crowdfunding_lists.html', {'posts':posts})

@login_required(login_url='/')
def create_crowdfunding(request):
    print "-----------------------> ", request.POST
    if request.method == "POST":
        form = CrowdFundingPostProposalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_datetime = timezone.now()
            post.save()
        return redirect('/')
    else:
        form = CrowdFundingPostProposalForm()
    return redirect('/')

def crowdfunding_detail(request, pk):
    post = get_object_or_404(CrowdFundingPostProposal, pk=pk)
    upvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='UP', pk=pk).count()
    downvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='DN', pk=pk).count()
    if CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__author=request.user, pk=pk).exists():
        hidden = True
    return render(request, 'crowdfunding/post.html', {'post': post, 'upvote':upvote, 'downvote':downvote, 'hidden':True})

@login_required(login_url='/')
def crowdfunding_vote(request):
    post_id = request.GET.get('post_id', None)
    vote_type = request.GET.get('vote_type', None)
    print request.user, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    proposal = CrowdFundingPostProposal.objects.get(pk=post_id)
    if not CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__author=request.user, pk=post_id).exists():
        proposal.crowdfundingproposalvoting_set.create(
                        author=request.user,
                        vote_type=vote_type
                    )
    data = {
        'success': True
    }

    if vote_type == 'UP':
        data['upvote'] = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='UP', pk=post_id).count()
    else:
        data['downvote'] = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='DN', pk=post_id).count()
    return JsonResponse(data)
