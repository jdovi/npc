from django.conf import settings
from django.template import Context
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from dovimotors.settings import EMAIL_PROVIDER #CHANGE
from DoviMotorsApp.management.commands import SendEmail_Base #CHANGE

import pdb

#python manage.py   SendEmail     content_id    music_id_list                   Email address list
#                 (mgt command)   (various)     (a python list of integers)  (a python list of emails)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('content_id')
        parser.add_argument('music_id_list')
        parser.add_argument('to_email_list')
        
    def handle(self, *args, **options):
        
        #capture content_id which will indicate which piece of functionality we're after
        content_id = options['content_id']
         
        music_id_list = options['music_id_list']
        to_email_list = options['to_email_list']
        list_count = len(music_id_list)
        
        #add the email addresses to the To line
        to = to_email_list
        
        #create the subject line
        subject = 'New teaching is available'
        
        #create the context variable
        context = {'headline':subject
                }        
                   
        #set the provider and create the HTML body
        EMAIL_PROVIDER = 'sendgrid'
        html_body = render_to_string('mail/new_upload_renderer.html', context)
        
        
        #construct email and send
        SendEmail_Base.Send(to,
                            subject,
                            html_body,
                            EMAIL_PROVIDER)
        

