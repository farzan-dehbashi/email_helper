from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pandas as pd
import csv

embassies = list(csv.reader(open('tests.csv')))

for embassy_string in embassies[1:]:

    country = str(embassy_string[0])
    emails = embassy_string[1:]

    print('Sending > ',country, '-----------------', emails)

    message = Mail(
        from_email='farzan.dehbashi@gmail.com',
        to_emails=emails,
        subject='Learning more about the culture of '+str(country),
        html_content='Dear representatives of '+country+' in Ottawa, <br/><br/> I am a junior enthusiast who collects flags, stamps and tiny pins from all over the globe. But I do not have any item to represent '+country+' in my collection event though I find it to be super cool. <br/> I wanted to ask you if possible, to send any item to me to represent your culture or country, anything like a small flag, pin or … <br/> <br/> My address is unit 801, 225 Village Green Square, Scarborough, Ontario, Canada. M1S0N4 <br/> I wish you all the best! <br/> <br/> Farzan')
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.message)
