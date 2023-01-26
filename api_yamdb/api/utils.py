import string
from random import sample
from django.core.mail import send_mail

MAX_CODE_LENGTH = 20


def generate_confirmation_code():
    letters_and_digits = string.ascii_letters + string.digits
    confirmation_code = ''.join(sample(letters_and_digits, MAX_CODE_LENGTH))
    return confirmation_code


def send_email_with_code(data):
    username = data['username']
    recipients = [data['email'], ]
    mailer = 'from@yambd.ru'
    subject = 'Письмо подтверждения'
    confirmation_code = data['confirmation_code']
    message = f'{username} ваш код подтверждения: {confirmation_code}'
    send_mail(subject, message, mailer, recipients)
