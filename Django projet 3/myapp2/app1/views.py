from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")
def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login (request,user)
            return render(request,"index.html")
        else:
            return render(request,"login.html",{"error":"username ya da parola yanlış girilmiştir"})
    else:
        return render(request,"login.html")
    
        
def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"login.html",{"error":"usermaöe kullanılıyor.."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"login.html",{"error":"bu email adresinden önceden kayıt yapılmıştır.."})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return render(request,"login.html") #bu yönlendirme değiştirilmiştir
        else:
            return render(request,"login.html",{"error":"parolayı yanlış ya da eksik tuşladınız"})
    else:
        return render(request,"login.html")
def create_reservation(request):
    if request.method=='POST':
        form=ReservationForm(request.POST)
        if form.is_valid():
            reservation=form.save(commit=False)
            reservation.user=request.user
            reservation.save()
            messages.success(request, 'Rezervasyon başarıyla oluşturuldu.')
            return redirect('reservation_list.html')
    else:
        form=ReservationForm()
    return render(request,'reservation_list.html')
            
def reservation_list(request):
    reservations=Reservation.objects.filter(user=request.user)
    return render(request,'reservation_list.html',{'reservations':reservations})

def cancel_reservation(request, reservation_id):
    reservation=Reservation.objects.get(id=reservation_id,user=request.user)
    if reservation:
        reservation.delete()
        messages.success(request,'Rezarvosyonunuz Başarılı Bir Şekilde İptal Edildi..')

    else:
        messages.error(request,'Rezervasyonununuz Bulunmadı..')
    return redirect('reservation_list')
    