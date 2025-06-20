from django.shortcuts import render
from overlap_app.overlap_hours.funcs import overlapping


def home(request):
    if request.method == 'POST':
        day1 = request.POST.get('day1')
        start1 = request.POST.get('start1')
        end1 = request.POST.get('end1')

        day2 = request.POST.get('day2')
        start2 = request.POST.get('start2')
        end2 = request.POST.get('end2')

        data = [
            {"Day": day1, "Start": start1, "End": end1},
            {"Day": day2, "Start": start2, "End": end2}
        ]

        result = overlapping(data)
        return render(request, 'overlap_app/home.html', {'result': result})
    return render(request, 'overlap_app/home.html')