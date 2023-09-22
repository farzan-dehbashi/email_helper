# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='farzan.dehbashi@gmail.com',
    to_emails='farzan.dehbashi95@gmail.com',
    subject='Salam',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
