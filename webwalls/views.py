from django.shortcuts import render_to_response
from django.template import RequestContext
from webwalls.models import Message
import datetime
# Create your views here.

def index(request):
    all_message_list = Message.objects.order_by("-create_time")

    return render_to_response('index.html', {'all_message_list' : all_message_list}, context_instance = RequestContext(request))

def add(request):
    message = request.POST['input_message']
    submit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entity = Message(body = message, create_time = submit_time)
    entity.save()

    return render_to_response('result.html', {'' : ''} , context_instance = RequestContext(request))