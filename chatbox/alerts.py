from .models import Message

BAD_WORDS = ['abc','def','ghi','klm']


def check_bad_words(message_pk, message_content):
    message = Message.objects.get(pk=message_pk)
    message_is_valid = True

    if any(word in message_content for word in BAD_WORDS):
        message.alert = True
        message.save(update_fields=["alert"])