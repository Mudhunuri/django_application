from django.shortcuts import render, redirect
from .forms import Projectform
from .models import db
from django.http import HttpResponse
from .resources import MemberResource 
from django.contrib.auth.models import User
from django.db.models import Q
# from .filters import UserFilter
 
# def search(request):
#     user_list = db.objects.all()
#     print(user_list)
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, 'project_list.html', {'filter': user_filter})

# Create your views here.
def export(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="COOP Records.xlsx"'
    return response

def project_list(request):
    if 'q' in request.GET:
        q=request.GET['q']
        #data=db.objects.filter(WO__icontains=q)
        multiple_q=Q(Q(WO__icontains=q)| Q(CUName__icontains=q) | Q(Status__icontains=q))
        data=db.objects.filter(multiple_q)
    else:
        data=db.objects.all()
    context={'project_list':data}
    #context = {'employee_list': Cooprequest.objects.all()}
    return render(request, 'project_list.html',context)


def request_form(request,id=0):
    if request.method =='GET':
        if id==0:
            form=Projectform()
        else:
            project=db.objects.get(pk=id)
            form=Projectform(instance=project)
        return render(request, 'project_form.html',{'form':form})
    else:
        if id==0:
            form=Projectform(request.POST)#,request.FILES)
        else:
            project=db.objects.get(pk=id)
            form=Projectform(request.POST,instance=project)
        if form.is_valid():
            form.save()
        return redirect('/list')
            

def project_delete(request,id):
    project=db.objects.get(pk=id)
    project.delete()
    return redirect('/list')
