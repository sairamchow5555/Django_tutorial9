from django.shortcuts import render,redirect
from .models import Question,Answer,Like
from .forms import QuestionForm,AnswerForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    question = Question.objects.all()
    return render(request,'quora_app/home.html',{'question':question})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'quora_app/question_detail.html', {'question': question, 'answers': answers})

#@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'quora_app/post_question.html', {'form':form})

#@login_required
def answer_question(request,question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        answer.user = request.user
        answer.question = question
        answer.save()
        return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'quora_app/answer_question.html', {'form':form})

#@login_required
def like_answer(request, answer_id):
    answer = Answer.Objects.get(id=answer_id)
    Like.objects.create(user=request.user,answer=answer)
    return redirect('home')
