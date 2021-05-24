from django.shortcuts import render
from .forms import CreateForm
from .ico_validation import ico_exists


def post_form(request):
    if request.method == 'POST':
        filled_form = CreateForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Form was created."
            new_form = CreateForm()
            return render(request, 'webform/create_form.html', {'form': new_form, 'note': note})
        else:
            return render(request, 'webform/create_form.html', {'form': filled_form})
    else:
        note = "Please, fill out a form."
        form = CreateForm()
        return render(request, 'webform/create_form.html', {'form': form, 'note': note})
