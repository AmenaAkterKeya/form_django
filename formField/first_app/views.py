from django.shortcuts import render, redirect
from .forms import MyForm

def myForm(request):
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
           
           print(form.cleaned_data)
           return redirect(myForm)
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})
