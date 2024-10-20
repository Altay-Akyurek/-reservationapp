from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=['check_in','check_out','room_number']