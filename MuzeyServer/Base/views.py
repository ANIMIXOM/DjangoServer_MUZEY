from django.shortcuts import render
from .forms import VisitorForm


def register_visitor(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            context = {
                    'title': 'None',
                    'message': '200',
                }
            form.save()
            return render(request, 'index.html', context)
    else:
        form = VisitorForm()

    return render(request, 'register_visitor.html', {'form': form})
