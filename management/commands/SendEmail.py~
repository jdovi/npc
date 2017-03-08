from django.conf import settings
from django.template import Context
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from drydenmusic.settings import EMAIL_PROVIDER
from DrydenMusicApp.management.commands import SendEmail_Base

from DrydenMusicApp.models import music, teaching_link
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
        
        if content_id == 'email_songs':
            #make a list of dictionaries of the title / link that needs to be sent
            link_list = []
            for music_id in music_id_list:
                for m in music.objects.filter(id=music_id):
                    link_list.append({'title':m.title,'url':m.music_file.url})
            
            
            #add the email addresses to the To line
            to = to_email_list
            
            #create the subject line
            subject = '%s New music files available for download' % list_count
            
            #create the context variable
            context = {'link_list':link_list,
                        'headline':subject
                    }
        
        if content_id == 'email_teachings':
            #make a list of dictionaries of the title / link that needs to be sent
            link_list = []
            for music_id in music_id_list:
                for m in teaching_link.objects.filter(id=music_id):
                    link_list.append({'title':m.title,'url':m.url})
            
            
            #add the email addresses to the To line
            to = to_email_list
            
            #create the subject line
            subject = '%s New teaching is available' % list_count
            
            #create the context variable
            context = {'link_list':link_list,
                        'headline':subject
                    }        
        
        elif content_id == 'email_registration':
            #add the email addresses to the To line
            to = to_email_list
            
            #create the subject line
            subject = 'Drydenmusic.com there is a new user request that needs approval'
            
            #create the context variable
            context = {'headline':subject,
                        'message':subject
                    }            
        #set the provider and create the HTML body
        EMAIL_PROVIDER = 'sendgrid'
        html_body = render_to_string('mail/new_upload_renderer.html', context)
        
        
        #construct email and send
        SendEmail_Base.Send(to,
                            subject,
                            html_body,
                            EMAIL_PROVIDER)
        

