from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from course.models import Course

from .filters import StudentFilter
from .forms import (
    GradeForm,
    StudentForm,
    StudentSelectForm,
)
from .models import (
    Grade,
    Student,
    installment,
)

user = get_user_model()


class StudentListView(ListView):
    template_name = 'student/list.html'
    context_object_name = 'filter'

    def get_queryset(self):
        student_list = StudentFilter(
            self.request.GET, queryset=Student.objects.all()
        )
        return student_list


class StudentDetailView(DetailView):
    model = Student
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'student/detail.html'

    def get_context_data(self, **kwargs):
        context_data = super(StudentDetailView, self).get_context_data(**kwargs)
        context_data['course_list'] = Course.objects.all()
        return context_data


class StudentDeleteView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('')


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('')
    template_name = 'student/create.html'

    def form_valid(self, form):
        new_form = form.save(commit=False)
        cd = form.cleaned_data
        user_obj = user.objects.create_user(
            national_code=cd['national_code'],
            first_name=cd['first_name'],
            last_name=cd['last_name'],
            phone_number=cd['phone_number'],
        )
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, '', 'btn btn-success')
        return super(StudentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', 'btn btn-danger')
        return super(StudentCreateView, self).form_invalid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('')
    template_name = 'student/update.html'
    id_field = 'id'
    id_url_kwarg = 'id'

    def form_invalid(self, form):
        new_form = form.save(commit=False)
        user_obj = get_object_or_404(user, id=self.kwargs.get('id'))
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, '', 'btn btn-success')
        return super(StudentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        messages.success()
        return super(StudentUpdateView, self).form_valid(form)


class GradeListView(ListView):
    model = Grade
    template_name = 'student/grade_list.html'


class GradeCreateView(CreateView):
    form_class = GradeForm
    template_name = 'student/grade_create.html'
    success_url = reverse_lazy('Student:grade_list')

    def form_valid(self, form):
        messages.success(
            self.request, 'پایه با موفقیت اضافه شد', 'btn btn-success'
        )
        return super(GradeCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(
            self.request, 'خطلا دز اقزودن پایه', 'btn btn-danger'
        )
        return super(GradeCreateView, self).form_invalid(form)


class GradeUpdateView(UpdateView):
    form_class = GradeForm
    template_name = 'student/grade_update.html'
    success_url = reverse_lazy('Student:grade_list')
    id_field = 'id'
    id_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(
            self.request, 'به روزرسانی با موفقیت انجام شد', 'btn btn-success'
        )
        return super(GradeUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'خطلا دز به روزرسانی', 'btn btn-danger'
        )
        return super(GradeUpdateView, self).form_invalid(form)


class GradeDeleteView(View):
    def get(self, request, grade_id):
        grade = get_object_or_404(Grade, id=grade_id)
        grade.delete()
        messages.success(
            request, 'پایه با موفقیت حذف شد', 'btn btn-success'
        )
        return redirect('Student:grade_list')


class InstallmentCreateView(View):
    template_name = ''
    form_class = ''

    def setup(self, request, *args, **kwargs):
        self.student = get_object_or_404(
            Student, id=self.kwargs.get('student_id')
        )
        super(InstallmentCreateView, self).setup(request, *args, **kwargs)

    def get(self, request, student_id):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, student_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            installment_count = self.student.total_pay() // cd['installment']
            installment_list = []
            for i in range(cd['count']):
                installment_list.append(
                    installment(student=self.student, amount=installment_count)
                )
            installment.objects.bulk_create(installment_list)
            messages.success(
                request, 'قسط بندی با موفقیت انجام شد', 'btn btn-success'
            )
            return redirect('')
        messages.error(
            request, 'خطا در انجام عملیات', 'btn btn-danger'
        )


class StudentSelectView(View):
    form_class = StudentSelectForm
    template_name = 'account/select.html'

    def get(self, request):
        return render(request, self.template_name, {'form': StudentSelectForm})

    def post(self, request):
        cd = self.form_class(request.POST)
        student_list = []
        model_qs = cd['student']
        for obj in model_qs:
            model_obj = Student.objects.get(id=obj.id)
            model_obj.grade = cd['grade']
            student_list.append(model_obj)
        Student.objects.bulk_update(student_list, ['grade'])
        messages.success(
            request, 'به روزرسانی با موفقیت انجام شد', 'btn btn-success'
        )
        return redirect('Student:list')
