from django.shortcuts import get_object_or_404, redirect, render
from .models import Event

# Create your views here.
def home(req):
    if req.method=="POST":
        event_name=req.POST.get("EVENT")
        desc=req.POST.get("Description")
        date = req.POST.get('date')
        location=req.POST.get("location")
        print(event_name, desc, date, location)
        data=Event.objects.create(title=event_name,description=desc, date=date, location=location)
        data.save()
        return redirect('show_events')
    return render(req,"main_page.html")

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'event_list.html', {'events': events})

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        # event.title = request.POST.get("EVENT")
        # event.description = request.POST.get("Description")
        # event.date = request.POST.get("date")
        # event.location = request.POST.get("location")
        # event.data=Event.objects.update(title=title,description=description, date=date, location=location)
        # data.save()
        if request.method == "POST":
            title = request.POST.get("EVENT")
            description = request.POST.get("Description")
            date = request.POST.get("date")
            location = request.POST.get("location")
        
        # ✅ Update the specific record
            event.title = title
            event.description = description
            event.date = date
            event.location = location
            event.save()
            return redirect('show_events')
    return render(request, 'edit_feedback.html', {'event': event})

#  if request.method == "POST":
#         title = request.POST.get("EVENT")
#         event.description = request.POST.get("Description")
#         event.date = request.POST.get("date")
#         event.location = request.POST.get("location")
#         event.save()
#         return redirect('show_events')


def delete_event(req,id):
    event= get_object_or_404(Event,id=id)
    if req.method == "POST":
        event.delete()
        return redirect('show_events')
    return render(req, 'delete_confirm.html', {'event': event})