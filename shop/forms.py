from django import forms
from .models import Review, Inquiry

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'rate',)

class EditReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'rate',)
        
class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ('content',)

class EditInquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ('content',)
