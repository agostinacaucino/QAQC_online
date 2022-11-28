from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, CheckboxButtonGroup, CustomJS
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.models.widgets import Button, RadioButtonGroup

"""def get_data():
    df = #archivo .csv cargado por el usuario
    return df"""

def charts(request):
    plot=figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")
    script, div = components(plot)

    return render(request, "core/charts.html", {"script": script, "div":div})

def data(request):
    plot=figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="red")
    script, div = components(plot)

    return render(request, "core/data.html", {"script": script, "div":div})

def health(request):
    return render(request, "core/health.html")

def statistics(request):
    return render(request, "core/statistics.html")

def select_button(request):
    radio_button = RadioButtonGroup(labels = ["Apple", "Mango", "Orange"],active = 0)
    return render(request, "core/base.html")
 

