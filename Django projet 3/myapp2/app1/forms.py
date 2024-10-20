from django import forms
from .models import Reservation
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'check_in', 'check_out', 'room_number']  # user alanını ekle
