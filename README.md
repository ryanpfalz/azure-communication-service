# azure-communication-service

Python guide: https://learn.microsoft.com/en-us/python/api/overview/azure/communication-email-readme?view=azure-python-preview

1. Create communication service (via CLI)
    https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource?tabs=linux&pivots=platform-azcli

2. Create email communication service (via Portal)
    - https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/create-email-communication-resource
    - Provision domains (1 click azure subdomain works fine)

3. In communication service, connect the domain
    https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/connect-email-communication-resource

Note: ensure the communication resource and email comm resource are created in the same region

update sender_address variable in scratch/scratch.py