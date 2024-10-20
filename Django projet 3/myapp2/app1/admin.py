from django.contrib import admin
from .models import Register
from .models import Reservation
from .forms import ReservationForm

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ('user', 'check_in', 'check_out', 'room_number', 'created_at')  # user alanını ekle
    search_fields = ('user__username', 'room_number')  # Kullanıcı adı üzerinden arama yapabilmek için

admin.site.register(Reservation, ReservationAdmin)

admin.site.register(Register)
# Register your models here.
# Register your models here.

