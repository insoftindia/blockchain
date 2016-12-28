from django.contrib.auth.decorators import login_required
from .models import CrowdFundingPostProposal, CrowdFundingProposalLike
from .forms import CrowdFundingPostProposalForm
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponse

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
    post_id = post.pk
    liked = False
    if request.session.get('has_liked_'+str(post_id), liked):
        liked = True
        print("liked {}_{}".format(liked, post_id))
    return render(request, 'crowdfunding/post.html', {'post': post, 'liked': liked})
