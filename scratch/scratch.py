import os
from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailAttachment, EmailMessage, \
    EmailRecipients

base_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

sender_address = 'DoNotReply@0a0b7e14-c239-412c-a2e8-8c9ecfc22804.azurecomm.net'

# file ignored in gitignore
with open(f'{base_dir}/scratch/connection.txt', 'r') as f:
    conn_str = f.read()

# authenticate with connection string
client = EmailClient.from_connection_string(conn_str)

content = EmailContent(
    subject="This is the subject",
    plain_text="This is the body",
    html="<html><h1>This is the body</h1></html>",
)

# address = EmailAddress(email="customer@domain.com", display_name="Customer Name")
address = EmailAddress(email="ryanpfalz@microsoft.com", display_name="Customer Name")

message = EmailMessage(
    sender=sender_address,
    content=content,
    recipients=EmailRecipients(to=[address])
)

response = client.send(message)
