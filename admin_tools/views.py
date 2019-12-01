from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from .models import Semester, Department, AcademicSession, SemesterCombination
from .forms import SemesterForm, DepartmentForm, AcademicSessionForm


# LIST VIEWS
@login_required
def semesters(request):
    '''
    Shows semester list and 
    contains semester create form
    '''
    all_sems = Semester.objects.all()
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tools:all_semester')
    form = SemesterForm()
    ctx = {
        'all_sems': all_sems,
        'form': form,
    }
    return render(request, 'admin_tools/all_semester.html', ctx)


@login_required
def academic_session(request):
    '''
    Responsible for academic session list view
    and academic session create view.
    '''
    if request.method == 'POST':
        form = AcademicSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tools:academic_sessions')
    else:
        form = AcademicSessionForm()
    all_academic_session = AcademicSession.objects.all()
    ctx = {
        'form': form,
        'academic_sessions': all_academic_session,
    }
    return render(request, 'admin_tools/academic_sessions.html', ctx)


@login_required
def departments(request):
    '''
    Responsible for department list view
    and department create view.
    '''
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tools:departments')
    else:
        form = DepartmentForm()
    all_department = Department.objects.all()
    ctx = {
        'form': form,
        'departments': all_department,
    }
    return render(request, 'admin_tools/departments.html', ctx)


class combination_list(LoginRequiredMixin, ListView):
    model = SemesterCombination
    context_object_name = 'combination'
    template_name = 'admin_tools/combinations.html'


class create_combination(LoginRequiredMixin, CreateView):
    model = SemesterCombination
    fields = '__all__'
    template_name = 'admin_tools/create_combination.html'
    success_url = reverse_lazy('admin_tools:combinations')
