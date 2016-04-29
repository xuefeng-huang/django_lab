from django.shortcuts import render
from forms import SignUpForm, ContactForm

# Create your views here.
def index(req):
    form = SignUpForm(req.POST or None)
    
    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'new name'
        form.full_name = full_name
        form.save()
        
    return render(req, 'index.html', {'form':form})


def contact(req):
    form = ContactForm(req.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value
    
    context = {
        'form' : form,
    }
    
    return render(req, 'forms.html', context)