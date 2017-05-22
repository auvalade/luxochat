from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def check_bad_words_async(message_pk, message_content):
    from chatbox.alerts import check_bad_words
    check_bad_words(message_pk, message_content)