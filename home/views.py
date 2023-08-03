from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Sum, F
from .models import *
from django.db.models import Max
from .seed import *

# Create your views here.

def home(request):

    queryset = SubjectMarks.objects.all()

    if request.GET.get('Search'):
        search = request.GET.get('Search')
        queryset = queryset.filter(
            Q(student__student_name__icontains=search)|
            Q(student__department__department__icontains=search)|
            Q(student__student_id__student_id__icontains=search)|
            Q(subject__subject_name__icontains=search)

        )
    

    latest_ids = SubjectMarks.objects.values('student_id').annotate(max_id=Max('id'))

# Get the unique SubjectMarks objects using the latest_ids
    s = SubjectMarks.objects.filter(id__in=[item['max_id'] for item in latest_ids])
    # s = SubjectMarks.objects.distinct('student__student_id')
    s= s[0].student.department
    contact_list = queryset
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    queryset2 = SubjectMarks.objects.all()
    # s = set([])
    # for query in queryset2:
    #     s.add(query)


    context ={
        'queryset' : page_obj,
        's' : s,
    }
    return render(request,'index.html',context)


def getMarks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id__icontains=student_id)
    l= student_id
    name = queryset[0].student.student_name
    total_marks = queryset.aggregate(Sum('marks'))
  
    queryset2 = studentCard.objects.filter(student__student_id__student_id__icontains = student_id)
    queryset2 = queryset2[0]
    context ={
        'queryset' : queryset,
        'queryset2' : queryset2,
        'l' : l,
        'name' : name,
        'total_marks' : total_marks,
    }

    return render(request,'marks.html',context)

def send_email(request):
    send_email_to_client()
    return redirect('/')