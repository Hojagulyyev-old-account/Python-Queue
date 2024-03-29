from django.shortcuts import render, redirect
from .transfer import create_time
import json
from django.http import HttpResponse
from .models import Cell, Example
from .forms import CellForm
from datetime import timedelta
from django.views.generic import TemplateView
import urllib
from .post import machine
from .validation import lenghtV, genericV
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

            # Redirect back to the same page if the data
            # was invalid
            context = {
                'x':x,
                'cells':cells,
                'form':form
            }
            return render(request, "first/index.html", context)
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


class ExampleView(TemplateView):
    template_name = "first/example.html"

    # def get(self, request, *args, **kwargs):
    #     self.lang = request.session.get('locale', 'tm')
    #     return super().get(request, *args, **kwargs)

    def post(self, request):
        # title = request.POST.get('title', '')
        # content = request.POST.get('content', '')
        # price = request.POST.get('price', 0)
        # image = request.FILES.get('image', '')
        # in_stock = request.POST.get('in_stock', False)
        # if in_stock:
        #     in_stock = True
        mc = machine(rq_post=request.POST, rq_file=request.FILES)
        rs1 = lenghtV(request,
                      e=mc['title'],
                      l=6,
                      content='Max length must 5 letters',
                      name='title')

        rs2 = lenghtV(request,
                      e=mc['content'],
                      l=10,
                      content='Max length of content must 10 letters',
                      name='content')

        rs3 = lenghtV(request,
                      e=mc['price'],
                      l=2,
                      content='Max length of price must 2 numbers',
                      name='price')

        vc = genericV(request, rs1, rs2, rs3)
        if vc != None:
            return redirect('/example/?' + urllib.parse.urlencode(vc))

        try:
            if mc['in_stock']:
                mc['in_stock']=True
        except:
            mc['in_stock']=False

        # context = {'message':'Nädogry şahsyýetnamalar! Gaýtadan synanyşyň!'}
        # return redirect('/?' + urllib.parse.urlencode(context))

        example = Example.objects.create(
            title=mc['title'],
            content=mc['content'],
            price=mc['price'],
            image=mc['image'],
            in_stock=mc['in_stock'],
        )
        example.save()

        return redirect('example')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['examples'] = Example.objects.all()

        return context
