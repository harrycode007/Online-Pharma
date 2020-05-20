from django.shortcuts import render
from django.contrib import messages
from medicine.models import Registration
from medicine.models import Contact, MedicineOrdered, Contactlogin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from datetime import date
from datetime import datetime
from datetime import timedelta

"""We import all the models here and write functions which compute various kinds of data upon
'request' and render it into the HTML. This file contains the main logic of the 
application/software."""

def index(request):
    params = {'name': 'medicine', 'place': 'iit'}
    return render(request, 'index.html', params)

def signup(request): # This function helps to signup/register in the store
        if request.method == "POST":
            print(request)
            fname = request.POST.get('fname', '')
            mname = request.POST.get('mname', '')
            lname = request.POST.get('lname', '')
            email = request.POST.get('email', '')
            gender = request.POST.get('gender', '')
            selphone = request.POST.get('selphone', '')
            contactnumber = request.POST.get('contactnumber', '')
            password = request.POST.get('password', '')
            cpassword = request.POST.get('cpassword', '')
            address = request.POST.get('address', '')

            if password == cpassword:
                signup = Registration(fname=fname,mname=mname,lname=lname, email=email, gender=gender,
                                      selphone=selphone,contactnumber=contactnumber,password=password,
                                      cpassword=cpassword,address=address
                                    )
                signup.save()
                messages.success(request, 'Your account has been created successfully!')
            else:
                messages.success(request, 'Password doesnt matches')
                return redirect('/signup/')

        return render(request, 'signup.html')

globalemail= " "
context={
    'gemail':globalemail,
}
def on(emaiil):
    global globalemail
    globalemail = emaiil
    print(globalemail)

def login(request): # This function evaluates the login request.
    if request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = Registration()
        on(email)
        context1={
            'email':email,
        }
        if Registration.objects.filter(email = email, password=password).all():
            user = Registration.objects.filter(email = email, password=password).all()
            return redirect('/store/')
        else:
            messages.info(request,"Invalid email or password")
            return redirect('/login/')
    else:
        return render(request,'login.html')

def contactus(request):
   if request.method == "POST":
       print(request)
       name= request.POST.get('name','')
       email= request.POST.get('email','')
       message = request.POST.get('message', '')
       contactus = Contact(name=name ,email=email, message=message)
       contactus.save()
       messages.success(request, 'Your message has been send!!')
   return render(request , 'contactus.html')

def store(request): # This is the main body or the computational part of the store.html file.
    if request.method == "POST":
        number1 = int(request.POST.get('number1', ''))
        number2 = int(request.POST.get('number2', ''))
        number3 = int(request.POST.get('number3', ''))
        number4 = int(request.POST.get('number4', ''))
        number5 = int(request.POST.get('number5', ''))
        number6 = int(request.POST.get('number6', ''))
        number7 = int(request.POST.get('number7', ''))
        number8 = int(request.POST.get('number8', ''))
        number9 = int(request.POST.get('number9', ''))
        number10 = int(request.POST.get('number10', ''))
        number11 = int(request.POST.get('number11', ''))
        number12 = int(request.POST.get('number12', ''))
        number13 = int(request.POST.get('number13', ''))
        number14 = int(request.POST.get('number14', ''))
        number15 = int(request.POST.get('number15', ''))
        number16 = int(request.POST.get('number16', ''))
        storeemail = globalemail
        Combiflam = number1 * 28 # This expr evaluates the number of medicine ordered multiplied by the cost of each medicine.
        Paracetamol = number2 * 30
        Cofsils =  number3 * 30
        DigeneTablet = number4 * 17
        DigeneGel = number5 * 100
        Hajmola = number6 * 32
        Seacod = number7 * 272
        Shelcal = number8 * 86
        Crocin = number9 * 15
        Lubrifresh = number10 * 99
        Dettol = number11 * 266
        Ashwagandha = number12 * 296
        Moov = number13 * 160
        Zandu = number14 * 40
        Vicks = number15 * 124
        Chyawanprash = number16 * 309

        totalSum = (number1 * 28) + (number2 * 30) + (number3 * 30) + (number4 * 17) + (number5 * 100) + \
               (number6 * 32) + (number7 * 272) + (number8 * 86) + (number9 * 15) + (number10 * 99) + \
               (number11 * 266) + (number12 * 296) + (number13 * 160) + (number14 * 40) + (number15 * 124) +\
               (number16 * 309) # Total sum of the prices of all the items in the cart.

        store = MedicineOrdered(Combiflam=Combiflam,Paracetamol=Paracetamol,Cofsils=Cofsils,
                                DigeneTablet=DigeneTablet,DigeneGel=DigeneGel,Hajmola=Hajmola,
                                Seacod=Seacod, Shelcal=Shelcal, Crocin=Crocin, Lubrifresh=Lubrifresh,
                                Dettol=Dettol, Ashwagandha=Ashwagandha, Moov=Moov, Zandu=Zandu,Vicks=Vicks,
                                Chyawanprash=Chyawanprash,totalSum=totalSum,storeemail=storeemail)
        store.save()
    return render(request, 'store.html')

def contactuslogin(request): # This function is the backend of the contactus.html file.
   if request.method == "POST":
       print(request)
       name= request.POST.get('name','')
       email= request.POST.get('email','')
       message = request.POST.get('message', '')
       contactuslogin = Contactlogin(name=name ,email=email, message=message)
       contactuslogin.save()
       messages.success(request, 'Your message has been send!!')
   return render(request , 'contactuslogin.html')

def cart(request):
    obj1 = MedicineOrdered.objects.filter().last()
    if globalemail == obj1.storeemail:
         obj = MedicineOrdered.objects.filter().last()
         return render(request, 'cart.html', {'obj':obj})
    else:
        return redirect('/store/')

def renderobject():
    obj1 = MedicineOrdered.objects.filter().last()
    output = ' '
    if globalemail == obj1.storeemail:
        if(obj1.Combiflam > 0):
            output = 'Combiflam:            ₹ ' + str(obj1.Combiflam) + '\n'
        if(obj1.Paracetamol > 0):
            output += 'Paracetamol:         ₹ ' + str(obj1.Paracetamol) + '\n'
        if (obj1.Cofsils > 0):
            output += 'Cofsils:                   ₹ ' + str(obj1.Cofsils) + '\n'
        if (obj1.DigeneTablet > 0):
            output += 'Digene Tablet:        ₹ ' + str(obj1.DigeneTablet) + '\n'
        if (obj1.DigeneGel > 0):
            output += 'Digene Gel:             ₹ ' + str(obj1.DigeneGel) + '\n'
        if (obj1.Hajmola > 0):
            output += 'Hajmola:                 ₹ ' + str(obj1.Hajmola) + '\n'
        if (obj1.Seacod > 0):
            output += 'Seacod:                   ₹ ' + str(obj1.Seacod) + '\n'
        if (obj1.Shelcal > 0):
            output += 'Shelcal:                   ₹ ' + str(obj1.Shelcal) + '\n'
        if (obj1.Crocin > 0):
            output += 'Crocin:                    ₹ ' + str(obj1.Crocin) + '\n'
        if (obj1.Lubrifresh > 0):
            output += 'Lubrifresh:              ₹ ' + str(obj1.Lubrifresh) + '\n'
        if (obj1.Dettol > 0):
            output += 'Dettol:                      ₹ ' + str(obj1.Dettol) + '\n'
        if (obj1.Ashwagandha > 0):
            output += 'Ashwagandha:       ₹ ' + str(obj1.Ashwagandha) + '\n'
        if (obj1.Moov > 0):
            output += 'Moov:                      ₹ ' + str(obj1.Moov) + '\n'
        if (obj1.Zandu > 0):
            output += 'Zandu:                     ₹ ' + str(obj1.Zandu) + '\n'
        if (obj1.Vicks > 0):
            output += 'Vicks:                       ₹ ' + str(obj1.Vicks) + '\n'
        if (obj1.Chyawanprash > 0):
            output += 'Chyawanprash:      ₹ ' + str(obj1.Chyawanprash) + '\n'
        if (obj1.totalSum > 0):
            output += '\nYour net payable amount is ₹'+' ' + str(obj1.totalSum) + '\n'
    return output

def orderplace(request):
    obj1 = MedicineOrdered.objects.filter().last()
    obj2 = Registration.objects.filter().last()
    delidate = date.today() + timedelta(days=3)
    return render(request, 'orderplace.html')