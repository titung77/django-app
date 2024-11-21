from django.shortcuts import render, redirect

# Create your views here.
from .models import Question, Subject
from .forms import QuestionForm
# Thêm câu hỏi mới
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_questions')
    else:
        form = QuestionForm()
        return render(request, 'questions/add_question.html', {'form': form})
# Hiển thị danh sách câu hỏi
def list_questions(request):
    questions = Question.objects.all()
    return render(request, 'questions/list_questions.html', {'questions': questions})
# Chỉnh sửa câu hỏi
def edit_question(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('list_questions')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'questions/edit_question.html', {'form': form})
# Xóa câu hỏi
def delete_question(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('list_questions')
    return render(request, 'questions/confirm_delete.html', {'question': question})