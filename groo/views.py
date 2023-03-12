from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from .models import Question, Answer
from django.contrib.auth import authenticate
# import mysql.connector as conn

# db =conn.connect(user='sql6429261',passwd='Mf3Q6WaXqp',host='sql6.freemysqlhosting.net',db='sql6429261')
# curr=db.cursor(buffered=True)

loggedin=0
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    global loggedin
    loggedin=0
    return render(request,'index.html')

def formsignup(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
    
    return redirect('index')

def login(request):
    return render(request,'index.html')

def formlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            global loggedin
            loggedin=1
            return redirect('home')
        else:
            return redirect('signup')


def question(request):
    return render(request,'addQuestions.html')

def addquestion(request):
    if request.method == 'POST':
        question=request.POST.get('question')
        # my_query='''INSERT INTO questions(question)
        # VALUES(%s)'''
        # val=(question,)
        # curr.execute(my_query,val)
        question_obj=Question.objects.create(question=question)
        # db.commit()
        question_obj.save()

    return redirect('home')
    
def home(request):
    if loggedin==1:
        # curr.execute('''SELECT * FROM questions''')
        # parameters={'ques':curr}
        questions=Question.objects.all()
        parameters={'questions':questions}
        return render(request,'home.html',parameters)
    return HttpResponse('Kindly Login First')
    
def showanswers(request):
    if request.method == 'POST':
        ques_no=request.POST.get('ques_no')
        # my_query='''SELECT answer FROM answers WHERE ques_no=%s'''
        # val=(ques_no,)
        # curr.execute(my_query,val)
        # parameter={'answers':curr.fetchall()}
        # my_query='''SELECT question FROM questions WHERE ques_no=%s'''
        # val=(ques_no,)
        # curr.execute(my_query,val)
        # parameter['ques']=curr.fetchall()[0][0]
        # parameter['quesno']=ques_no
        ques_no = int(ques_no)
        parameter={
            'answers':Answer.objects.all().filter(question=Question.objects.get(id=ques_no)),
            'ques': Question.objects.get(id=ques_no).question,
            'ques_no': ques_no,
        }
        print(parameter)
        return render(request,'ShowAnswers.html',parameter)


def addans(request):
    ques_no=request.POST.get('ques_no')
    ques_no = int(ques_no)
    print(ques_no)
    # my_query='''SELECT question FROM questions WHERE ques_no=%s'''
    # val=(ques_no,)
    # curr.execute(my_query,val)
    # parameter={'ques':curr.fetchone()[0]}
    # parameter['ques_no']=ques_no
    parameter={
        'ques':Question.objects.get(id=ques_no).question,
        'ques_no': ques_no,
    }
    return render(request,'addAnswer.html',parameter)

def anssubmit(request):
    if request.method == 'POST':
        ques_no=request.POST.get('ques_no')
        answer=request.POST.get('answer')
        # my_query='''INSERT INTO answers (ques_no,answer) VALUES (%s,%s)'''
        # val=(ques_no,answer)
        # curr.execute(my_query,val)
        # db.commit()
        ques_no=int(ques_no)
        answer=str(answer)
        answer_obj=Answer.objects.create(question=Question.objects.get(id=ques_no),answer=answer)
        answer_obj.save()
        return redirect('home')