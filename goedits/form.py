from django import forms
import json
import django.core
class MailForm(forms.Form):
	cname_mail = forms.CharField(
									label='companyname',
									max_length=100,
									widget=forms.TextInput(
															attrs = {'class': 'form-control', 'placeholder': 'Company Name'}),
															error_messages={'required': "'Comapany Name' field is required"})
	to_mail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),error_messages={'required': "'To' field is required"})
	content_mail = forms.CharField(widget=forms.Textarea(attrs={'cols': 54, 'rows': 10,'class': 'form-control', 'placeholder': 'Your Message'}), error_messages = {'required': "'Content' field is required"})
	mail_subject = forms.CharField(label='subject',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))