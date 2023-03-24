from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib import messages

from django.http import HttpResponse

#from ressources import AdminMamadouNotes


from ConApp.models import MyUser, MamadouNotes, SamedNotes
from pathlib import Path
import datetime

# Create your views here.
class UserPersonnaliser(UserCreationForm):
    class Meta:
        model = MyUser
        fields = UserCreationForm.Meta.fields

def accueil(request):

    return render(request, 'accueil.html', context={'date':datetime.datetime.today})

def subcription(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        mail = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        #On recuperer le username et on regarde si ce nom correspond aux gabarits HTMl autorisée
        template_entree = f"{username.lower()}.html"
        templates_existant = Path(__file__).resolve().parent
        templates_dirs = templates_existant / 'templates'
        temp_dirs = [temp.name for temp in templates_dirs.rglob('*.html')]

        #On compare les passwords
        if password1 != password2:
            return render(request, 'app.html', {'error':'The Passwords does not Match, please try again.'})

        #On s'assure que la personne inscrit est autorisée à le faire
        elif template_entree not in temp_dirs:
            return render(request, 'app.html', {'error':'Sorry, you are not allowed to acceded in this Page.'})

        #On s'assure qu'un nom d'utilisateur ne peut être utilisé qu'un fois
        elif MyUser.objects.filter(username=username).exists():
            return render(request, 'app.html', {'error':"Username already exist, please try with another Username. "})

        MyUser.objects.create_superuser(username=username, email=mail, password=password1)
        user = f"Welcome {username}, You have ben filnalized your account."
        return render(request, f'{username.lower()}.html', {'user':user})
    return render(request, 'app.html', {'user':'Inscription effectuer avec succés.'})


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            #Cette fonction permet de connecter la personne à la page d'admin de Django.
            login(request, user)
            data = MamadouNotes.objects.all().order_by('-id').values()
            data2 = SamedNotes.objects.all().order_by('-id').values()
            username = username.lower()
            if username == 'mamadou':
                return render(request, f"{username}.html", {'data': data})
            elif username == 'samed':
                return render(request, f"{username}.html", {'data': data2})
        else:
            messages.success(request,('Username or Password falls. '))
            print('Your are not connected.')
            return redirect('login-user')
    else:

        return render(request, "authenticate/login.html")
    return render(request, "authenticate/login.html")

def user_logout(request):
        if request.user.is_authenticated == True:
            username = request.user.username
        else:
            username = None

        return username
def logout_view(request):
    username = user_logout(request)
    if username != None:
        print(f'{username} you are loged out. ')
        logout(request)
        return render(request, 'authenticate/login.html', {'ticks':'Please enter your Username end Password to reconnect. '})


def mamadou_notes(request):
    if request.method == 'POST':
        jours = request.POST.get('day')
        post = request.POST.get('notes')
        date = request.POST.get('date')
        usr = MamadouNotes(day=jours, notes=post, date=date)
        usr.save()
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    elif request.method == 'GET':
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    return render(request, 'mamadou.html', {'error':'No data to print. '})

def mamadou_items_del(request, id):
    items = MamadouNotes.objects.get(id=id)
    user = user_logout(request)
    items.delete()

    usr = user.lower()
    context = {'del':'You have delete this items', 'user':usr}
    return render(request, 'items_del.html', context)

def samed_notes(request):
    if request.method == 'POST':
        jours = request.POST.get('day')
        post = request.POST.get('notes')
        date = request.POST.get('date')
        usr = SamedNotes(day=jours, notes=post, date=date)
        usr.save()
        notes = SamedNotes.objects.all().order_by('-id').values()
        return render(request, 'samed.html', {'data':notes})
    elif request.method == 'GET':
        notes = MamadouNotes.objects.all().order_by('-id').values()
        return render(request, 'mamadou.html', {'data':notes})
    return render(request, 'samed.html', {'error':'No data to print. '})

def samed_items_del(request, id):
    items = SamedNotes.objects.get(id=id)
    user = user_logout(request)
    items.delete()

    usr = user.lower()
    context = {'del':'You have delete this items', 'user':usr}

    return render(request, 'items_del.html', context)

#def export_data(request):
   # dataset = AdminMamadouNotes().export()
   # response = HttpResponse(dataset.csv, content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="mymodel.csv"'
    #return response
