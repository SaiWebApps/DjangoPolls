from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from polls.models import Poll, Choice
from polls.forms import PollForm, ChoiceForm

#Show all polls that have been created thus far.
def index(request):
    poll_list = Poll.objects.all()
    return render(request, 'polls/index.html', {'poll_list' : poll_list})
 
#Create a Poll.
def createPoll(request):
    form = PollForm(request.POST or None)
    if not form.is_valid():
        context = {}
        poll_list = Poll.objects.all()
        context['poll_list'] = poll_list
        context['form'] = form
        return render(request, 'polls/index.html', context)
    else:
        form.save()
        return HttpResponseRedirect('/polls')
  
#Fetch a specific poll.
def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll' : poll})

#Create Choices.
def createChoice(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    form = ChoiceForm(request.POST or None)
    if not form.is_valid():
        context = {}
        poll = get_object_or_404(Poll, pk=poll_id)
        context['form'] = form
        context['poll'] = poll
        return render(request, 'polls/detail.html', context)
    else:
        obj = form.save(commit=False)
        obj.poll = poll
        obj.votes = 0
        obj.save()
        return HttpResponseRedirect('/polls/'+poll_id+'/')

#Increment the # of votes for a choice.
def upVote(request, poll_id, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    Choice.objects.filter(pk=choice_id).update(votes=choice.votes+1)
    return HttpResponseRedirect('/polls/'+poll_id+'/')