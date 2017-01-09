from django.contrib.auth.decorators import login_required
from .models import CrowdFundingMemberGroup, CrowdFundingMemberGroup, UserExtendedForFunding, CrowdFundingPostProposal, CrowdFundingProposalVoting
from .forms import CrowdFundingPostProposalForm
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from login.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/')
def crowdfunding(request):
    group_type = CrowdFundingMemberGroup.objects.all()
    latest_posts = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='DT').order_by('published_datetime')
    closed_posts = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='CD').order_by('published_datetime')
    return render(request, 'crowdfunding/crowdfunding_home.html', {'posts':latest_posts, 'closed_posts':closed_posts, 'group_type':group_type})

@login_required(login_url='/')
def latest_crowdfunding_proposals(request):
    group_type = CrowdFundingMemberGroup.objects.all()
    latest_posts_list = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='DT').order_by('published_datetime')
    latest_paginator = Paginator(latest_posts_list, 4)

    page = request.GET.get('page')
    try:
        latest_posts = latest_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_posts = latest_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_posts = latest_paginator.page(latest_paginator.num_pages)
    return render(request, 'crowdfunding/crowdfunding_proposals.html', {'posts':latest_posts, 'group_type':group_type, 'title':'Latest Proposals'})

@login_required(login_url='/')
def closed_crowdfunding_proposals(request):
    group_type = CrowdFundingMemberGroup.objects.all()
    closed_posts_list = CrowdFundingPostProposal.objects.filter(published_datetime__lte=timezone.now(), state='CD').order_by('published_datetime')
    closed_paginator = Paginator(closed_posts_list, 4)
    page = request.GET.get('page')
    try:
        closed_posts = closed_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        closed_posts = closed_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        closed_posts = closed_paginator.page(closed_paginator.num_pages)
    return render(request, 'crowdfunding/crowdfunding_proposals.html', {'posts':closed_posts, 'group_type':group_type, 'title':'Closed Proposals'})

@login_required(login_url='/')
def create_crowdfunding(request):
    # print "-----------------------> ", request.POST
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

@login_required(login_url='/')
def user_creation(request):
    if request.method == "POST":
        if request.POST.get('type') == 'create-user':
            request.POST = request.POST.copy()
            request.POST['repeat_password'] = request.POST.get('password')

            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                )
                user_type = 'FR' if request.POST.get('user_type')=='FR' else 'MR'
                funding_type = 'MR' if request.POST.get('funding_type')=='MR' else 'GR'
                u_extended = UserExtendedForFunding(user=user, user_type=user_type,funding_type=funding_type, user_image=request.FILES.get('user_image'), funding_amout=request.POST.get('funding_amout'))
                u_extended.save()
    return redirect('/')

@login_required(login_url='/')
def crowdfunding_detail(request, pk):
    post = get_object_or_404(CrowdFundingPostProposal, pk=pk)
    upvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='UP', pk=pk).count()
    downvote = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='DN', pk=pk).count()
    return render(request, 'crowdfunding/post.html', {'post': post, 'upvote':upvote, 'downvote':downvote})

@login_required(login_url='/')
def crowdfunding_vote(request):
    post_id = request.GET.get('post_id', None)
    vote_type = request.GET.get('vote_type', None)
    proposal = CrowdFundingPostProposal.objects.get(pk=post_id)
    success = False
    # self_user_proposal = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__author=request.user, pk=post_id)
    if request.user.user_extented.user_type == 'MR':
        self_user_voting = CrowdFundingProposalVoting.objects.filter(proposal_id__exact=post_id, author=request.user)
        if self_user_voting:
            if self_user_voting[0].vote_type == 'UP' and vote_type == 'DN':
                self_user_voting.update(vote_type='DN')
                success = True
            elif self_user_voting[0].vote_type == 'DN' and vote_type == 'UP':
                self_user_voting.update(vote_type='UP')
                success = True
        else:
            # if not self_user_voting.exists():
            proposal.crowdfundingproposalvoting_set.create(
                            author=request.user,
                            vote_type=vote_type
                        )
            success = True

    data = {'success': success}

    data['upvote'] = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='UP', pk=post_id).count()
    data['downvote'] = CrowdFundingPostProposal.objects.filter(crowdfundingproposalvoting__vote_type='DN', pk=post_id).count()
    return JsonResponse(data)

@login_required(login_url='/')
def get_group_total_amount(request):
    group_type = request.GET.get('group_type', None)
    # print group_type, " <--------------------------------"
    group_funding_amount_tot = UserExtendedForFunding.objects.filter(group_type__in=CrowdFundingMemberGroup.objects.filter(name=group_type)).aggregate(Sum('funding_amout'))
    data = {
        'total_amt': group_funding_amount_tot['funding_amout__sum']
    }
    return JsonResponse(data)

@login_required(login_url='/')
def close_proposal(request):
    post_id = request.GET.get('post_id', None)
    proposal = CrowdFundingPostProposal.objects.filter(pk=post_id)
    # print proposal, "FFFFFFFFFFFFFFF"
    proposal.update(state='CD')
    return JsonResponse({})