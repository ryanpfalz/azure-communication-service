import os
from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage, EmailRecipients

base_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

# Get MailFrom display name and address in AzureManagedDomain resource
sender_address = '<MailFrom Display Name>@<MailFrom Address>'

# connection.txt file is ignored in gitignore and needs to be created locally in the
with open(f'{base_dir}/email/connection.txt', 'r') as f:
    conn_str = f.read()

# authenticate with connection string
client = EmailClient.from_connection_string(conn_str)

# prepare message body and recipients
content = EmailContent(
    subject="This is the subject",
    plain_text="This is the body",
    html="<html><h1>This is the body</h1></html>",
)

recipient_address = "customer@domain.com"

address = EmailAddress(email=recipient_address,
                       display_name="Customer Name")

message = EmailMessage(
    sender=sender_address,
    content=content,
    recipients=EmailRecipients(to=[address])
)

# send message
response = client.send(message)
