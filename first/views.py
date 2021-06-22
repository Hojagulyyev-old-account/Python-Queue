from django.shortcuts import render, redirect
from .transfer import create_time
import json
from django.http import HttpResponse
from .models import Cell
from .forms import CellForm
from datetime import timedelta
# Create your views here.
def index(request):
    x = create_time(start=7, end=14, step=20)
    cells = Cell.objects.all()
    form = CellForm()
    if request.method == 'POST':
        form = CellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = CellForm()

    context = {
        'x':x,
        'cells':cells,
        'form':form
    }
    # json.dumps(x)
    return render(request, 'first/index.html', context)

def change_queue(request, *args, **kwargs):
    try:
        cell = Cell.objects.get(id=kwargs['id'])
    except Cell.DoesNotExist:
        return HttpResponse("<h1>Cell . DoesNotExist</h1>")

    x = create_time(start=7, end=14, step=20)
    try:
        next_index = (x.index(kwargs['time'])+1)
        next_cell = x[next_index]
    except IndexError:
        next_cell = x[0]

    try:
        has_next_cell = Cell.objects.get(time=next_cell, date=kwargs['date'])
        if x.index(next_cell) != 0:
            cell.time = next_cell
            cell.save()
        else:
            cell.time = next_cell
            cell.date = cell.date+timedelta(days=1)
            cell.save()
        return redirect('change_queue', time=has_next_cell.time, id=has_next_cell.id, date=has_next_cell.date)
    except:
        if x.index(next_cell) != 0:
            cell.time = next_cell
            cell.save()
        else:
            cell.time = next_cell
            cell.date = cell.date+timedelta(days=1)
            cell.save()

    print('============> ', kwargs['date'])

    return redirect('index')
