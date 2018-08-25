from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from filter.models import Questions, Player, NewQuestions
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def start(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/question")
    else:
        return render(request, 'login.html')

def signup_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/question")
    else:
        return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = User.objects.create_user(username = uname,password = pwd)
        a = authenticate(request, username=uname, password=pwd)
        login(request, user)

        cu = request.user.id
        print("Player id during creation of user : ",cu)
        sid = ((cu-1) * 100 - 99)
        cid = ((cu-1) * 100 - 99)
        eid = ((cu-1) * 100)
        user_object = Player.objects.create(pid = user, pname = uname, sid = sid, cid = cid, eid = eid)
        user_object.save()


        p = request.user.player
        return HttpResponseRedirect("/question")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/question")
        return render(request,'signup.html',)

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/question")
    else:
        return render(request,'login.html')

def login_func(request):
    uname = request.POST.get("uname")
    password = request.POST.get("pass")
    u2 = authenticate(request, username=uname, password=password)
    if u2 is not None:
        login(request, u2)
        return HttpResponseRedirect("/question")
    else:
        str = "login failed"
        context = {'str': str}
        return HttpResponse("Not Logged in!!!")

def filter(request):
    if request.user.is_authenticated:
        rb1 = request.POST.get("ranswer")
        #
        if rb1 is not None:
            u = request.user.player
            #u = u.player
            id = u.cid
            sid = u.sid
            if id < sid:
                id = id + 1
            #print("filter id of question is ",id,"   ",lpid)
            que = Questions.objects.get(id = id)
            qtext = request.POST.get('nqtext')
            opta = request.POST.get('nopa')
            optb = request.POST.get('nopb')
            optc = request.POST.get('nopc')
            optd = request.POST.get('nopd')
            ans = request.POST.get('ranswer')
            ans = int(ans)
            print(" qtext: ",qtext," op: ",opta," op: ",optb," op: ",optc," op: ",optd," answer: ",ans)
            #que.selected = 1
            rb2 = request.POST.get("rlvl")
            print("Value of rb2 is firstly : ", rb2)
            if rb2 is not None:
                if int(rb2) == 1:
                    lvl = False
                    que.selected = 1
                    print("Value of rb2 is : ",rb2)
                    nque = NewQuestions.objects.create(question = qtext, optiona = opta, optionb = optb, optionc = optc, optiond = optd, correctans = ans, level = lvl)
                    nque.save()
                    u1 = request.user.player
                    print("player id is : ", u.id)
                    u1.cid = u1.cid + 1
                    cid = u1.cid
                    sid = u1.sid
                    u1.save()
                    u.save()
                    return HttpResponseRedirect("/question")
                elif int(rb2) == 2:
                    lvl = True
                    que.selected = 1
                    print("Value of rb2 is : ", rb2)
                    nque = NewQuestions.objects.create(question = qtext, optiona = opta, optionb = optb, optionc = optc, optiond = optd, correctans = ans, level = lvl)
                    nque.save()
                    u1 = request.user.player
                    print("player id is : ", u.id)
                    u1.cid = u1.cid + 1
                    cid = u1.cid
                    sid = u1.sid
                    u1.save()
                    u.save()
                    return HttpResponseRedirect("/question")
                else:
                    u1 = request.user.player
                    print("player id is : ", u.id)
                    u1.cid = u1.cid + 1
                    cid = u1.cid
                    sid = u1.sid
                    u1.save()
                    u.save()
                    return HttpResponseRedirect("/question")
            else:
                u.cid = u.cid - 1
                u.save()
                return HttpResponseRedirect("/question")
        else:
            return HttpResponseRedirect("/question")
    else:
        return HttpResponseRedirect("/login")


def question(request):
    u = request.user.player
    print("player id is : ",u.id)
    # u.cid = u.cid + 1
    cid = u.cid
    sid = u.sid
    u.save()
    #cid = cid + 1
    if cid <= u.eid:
        print("players curent id : " ,cid)
        try:
            que = Questions.objects.get(id = cid)
        except:
            return HttpResponse("Questions Database Finished")
        qtext = que.question
        opta = que.optiona
        optb = que.optionb
        optc = que.optionc
        optd = que.optiond
        ans = que.correctans
        context = {'qtext':qtext, 'opa':opta, 'opb':optb, 'opc':optc, 'opd':optd, 'ans':ans}
        return render(request,'question.html',context)
    else:
        return HttpResponse("Questions Over")

def logoutfunc(request):
    logout(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect("/question")
    return HttpResponseRedirect("/")



def lb(request):
    u = User.objects.filter(is_staff=0)
    context = {'object':u}
    return render(request,'lb.html',context)


















