from django.shortcuts import render, redirect
from .forms import MymodelForm

def myModel(request):
    if request.method == "POST":
        form = MymodelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(myModel)
    else:
        form = MymodelForm()
    return render(request, 'form.html', {'form': form})
