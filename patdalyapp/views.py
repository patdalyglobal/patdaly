from .forms import ContactMessageForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Contractor, Supervisor
from .forms import ProjectForm, ContractorForm, SupervisorForm


def index(request):
    return render(request, 'patdalyapp/index.html')

def about(request):
    return render(request, 'patdalyapp/about.html')

def services(request):
    return render(request, 'patdalyapp/services.html')

def web(request):
    return render(request, 'patdalyapp/web-app.html')

def team(request):
    return render(request, 'patdalyapp/team.html')

def contact(request):
    return render(request, 'patdalyapp/contact.html')

def pricing(request):
    return render(request, 'patdalyapp/pricing.html')



def contact_us(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, such as sending email notifications.
            return redirect('contact_success')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact_us.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/contact_success.html')


# ------------------------------ Plateau State Budget and Planning -------------------------- #
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'pms/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'pms/project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'pms/project_form.html', {'form': form, 'title': 'Create Project'})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'pms/project_form.html', {'form': form, 'title': 'Edit Project'})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'pms/project_confirm_delete.html', {'project': project})

def contractor_list(request):
    contractors = Contractor.objects.all()
    return render(request, 'pms/contractor_list.html', {'contractors': contractors})

def contractor_detail(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    return render(request, 'pms/contractor_detail.html', {'contractor': contractor})

def contractor_create(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm()
    return render(request, 'pms/contractor_form.html', {'form': form, 'title': 'Create Contractor'})

def contractor_edit(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'pms/contractor_form.html', {'form': form, 'title': 'Edit Contractor'})

def contractor_delete(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        contractor.delete()
        return redirect('contractor_list')
    return render(request, 'pms/contractor_confirm_delete.html', {'contractor': contractor})


def supervisor_list(request):
    supervisors = Supervisor.objects.all()
    return render(request, 'pms/supervisor_list.html', {'supervisors': supervisors})

def supervisor_detail(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    return render(request, 'pms/supervisor_detail.html', {'supervisor': supervisor})

def supervisor_create(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm()
    return render(request, 'pms/supervisor_form.html', {'form': form, 'title': 'Create Supervisor'})

def supervisor_edit(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm(instance=supervisor)
    return render(request, 'pms/supervisor_form.html', {'form': form, 'title': 'Edit Supervisor'})

def supervisor_delete(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'POST':
        supervisor.delete()
        return redirect('supervisor_list')
    return render(request, 'pms/supervisor_confirm_delete.html', {'supervisor': supervisor})
