from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):
    # Custom validation for the mobile_number field
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if mobile_number:
            # Check if the mobile number is in a valid format (e.g., 123-456-7890)
            if not re.match(r'^\d{3}-\d{3}-\d{4}$', mobile_number):
                raise forms.ValidationError('Invalid mobile number format. Use XXX-XXX-XXXX.')
        return mobile_number

    # Custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Check if the email address is in a valid format
            if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                raise forms.ValidationError('Invalid email address format.')
        return email

    class Meta:
        model = Student
        fields = "__all__"
