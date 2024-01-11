from django import forms

class HeartRateForm(forms.Form):
    heart_rate = forms.FloatField(label='Enter Heart Rate (bpm)')
