from django.shortcuts import render, redirect

# Create your views here.


from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')  # success message dekhate chaile alada handle kora jabe
    else:
        form = ContactForm()
    return render(request, 'contact/contact_page.html', {'form': form})


