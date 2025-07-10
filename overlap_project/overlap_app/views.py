from django.views import View
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from overlap_app.overlap_hours.funcs import overlapping
from .forms import WorkingHoursForm
from .models import WorkingHours


class Home(View):
    template = 'overlap_app/home.html'
    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        days = request.POST.getlist('day')
        starts = request.POST.getlist('start')
        ends = request.POST.getlist('end')

        data = []

        for day, start, end in zip(days, starts, ends):
            if day and start and end:
                WorkingHours.objects.create(day=day, start=start, end=end)

                data.append({'Day': day, 'Start': start, 'End': end})

        return redirect("edit")



class Edit(View):
    template = 'overlap_app/edit.html'

    def get(self, request):
        WorkingHoursFormSet = modelformset_factory(
            WorkingHours, form=WorkingHoursForm, extra=0, can_delete=True
        )
        formset = WorkingHoursFormSet(queryset=WorkingHours.objects.all())
        return render(request, self.template, {"formset": formset})

    def post(self, request):
        WorkingHoursFormSet = modelformset_factory(
            WorkingHours, form=WorkingHoursForm, extra=0, can_delete=True
        )
        formset = WorkingHoursFormSet(request.POST)
        action = request.POST.get("action")

        if formset.is_valid():
            formset.save()
            if action == "check":
                slots = WorkingHours.objects.all()
                data = [{"Day": s.day, "Start": s.start, "End": s.end} for s in slots]
                result = overlapping(data)
                return render(
                    request,
                    self.template,
                    {"formset": formset, "result": result},
                )
            return redirect("home")

        return render(request, self.template, {"formset": formset})
