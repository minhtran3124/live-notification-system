"""The api access form and send messages"""

import time
import datetime

from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .forms import MessageForm


def send_msg(request):
    """

    @param request:
    @return:
    """
    if request.method == 'GET':
        return render(request, 'sms/send_msg.html', {'form': MessageForm()})
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            print('Sending sms ...')
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)('new message', {
                'type': 'notify client',
                'message': f'email is sent {datetime.datetime.now()}'
            })
            print('message is sent')
        else:
            print('Something went wrong')
            print(form.errors)
        return render(request, 'sms/send_msg.html', {'form': MessageForm()})
    else:
        return HttpResponse('Wrong method')


def notification(request):
    """

    @param request:
    @return:
    """
    return render(request, 'sms/notification.html', {'unread_count': 9})
