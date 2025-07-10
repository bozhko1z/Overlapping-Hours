from django.shortcuts import render
from overlap_app.overlap_hours.funcs import overlapping
from .models import WorkingHours


def home(request):

    if request.method == 'POST':
        days = request.POST.getlist('day')
        starts = request.POST.getlist('start')
        ends = request.POST.getlist('end')
        data = []

        for day, start, end in zip(days, starts, ends):
            if day and start and end:
                WorkingHours.objects.create(day=day, start=start, end=end)
                data.append({'Day': day, 'Start': start, 'End': end})

        result = overlapping(data)

        if result is not None:
            return render(request, 'static/overlap_app/home.html', {'result': result})

    return render(request, 'static/overlap_app/home.html')