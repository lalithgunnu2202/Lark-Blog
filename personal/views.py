from django.shortcuts import render , redirect ,get_object_or_404
from .models import *
from django.contrib import messages
from datetime import date, timedelta

# Create your views here.
def dashboard_view(request):
    return render(request,"personal/home.html")

def journals_view(request):
    journals = Journal.objects.all()
    today = date.today()
    return render(request,'personal/all_journals.html',{'journals':journals,'today':today})

def add_journal(request):
    if request.method == 'POST':
        learnt = request.POST.get('learnt')
        built = request.POST.get('built')
        thoughts = request.POST.get('thoughts')
        tomorrow = request.POST.get('tomorrow')
        if not learnt or not built or not thoughts or not tomorrow :
            messages.error(request,"Add valid details")
            return redirect('journal_dashboard')
        Journal.objects.create(learnt=learnt, built=built,thoughts=thoughts,tomorrow=tomorrow)
        messages.info(request,"Journal Created Successfully")
        return redirect('journal_dashboard')
    return redirect('journal_dashboard')
    
def delete_journal(request, id):
    journal = get_object_or_404(Journal,id=id)
    Journal.delete(journal)
    messages.info(request,f"{id}th journal deleted succesfully")
    return redirect('journal_dashboard')

def view_journal(request,id):
    journal = get_object_or_404(Journal,id =id)
    today = journal.date
    return render(request,'personal/details.html',{'journal':journal,'today':today})