# Azure Communication Service Demos

---

| Page Type | Languages              | Key Services                       | Tools |
| --------- | ---------------------- | ---------------------------------- | ----- |
| Sample    | Python <br> PowerShell | Azure Communication Services (ACS) |       |

---

## Introduction

This is a work-in-progress repository to demonstrate how to use the features of [Azure Communication Services](https://learn.microsoft.com/en-us/azure/communication-services/overview).

## Prerequisites

-   [An Azure Subscription](https://azure.microsoft.com/en-us/free/) - for hosting cloud infrastructure
-   [Az CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) - for deploying Azure infrastructure as code
-   [Python](https://www.python.org/downloads/) - for Python development

---

## Email

This section uses [this guide](https://learn.microsoft.com/en-us/python/api/overview/azure/communication-email-readme?view=azure-python-preview) as a basis to demonstrate how to use Python to send emails with Azure Communication Services' [email-as-a-service solution](https://learn.microsoft.com/en-us/azure/communication-services/concepts/email/email-overview).

The steps to set up and send emails are as follows:

#### Set up the infrastructure

1. In the `infra/acs.ps1` file:

    - _Note: Ensure you run_ `az login` _prior to running any other Az CLI commands._
    - Update the variable names to the resource names you'd like to use.
    - Run the `az group create` command to create a resource group.
    - Run the `az communication create` command to create an Azure Communication Services resource ([doc](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource?tabs=linux&pivots=platform-azcli)).

2. Get the connection string by navigating to the ACS resource that was created and go to the 'Keys' blade.

3. Create an Email Communication Service (via Azure Portal):

    - Follow the steps laid out in [this guide](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/create-email-communication-resource).
        - Note: Ensure that the Email Communication Service is created with the same Data Location as the Azure Communication Services resource set up in the previous step.
    - Go to the 'Provision domains' blade of the newly created Email Communication Service and either add a free Azure subdomain or set up a custom domain. This will create an Email Communication Services Domain resource.

4. In Azure Communication Service resource, connect the domain you just created:

    - Follow the steps laid out in [this guide](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/connect-email-communication-resource).

#### Configure & run the code

1. Install the dependencies listed in the `email/requirements.txt` file.
2. In the `email/` folder, create a file called `connection.txt`. Paste the connection string from Step 2 above into the file.
3. Update the `sender_address` variable in `email/send-email.py`:
    - Go to the Email Communication Services Domain resource created in Step 3 above. You may edit and retrieve the 'MailFrom' value from here.
    - Update the `sender_address` variable with the 'MailFrom' value.
4. Update the `recipient_address` variable in `email/send-email.py` with your desired recipient email address.
5. Run the code in `email/send-email.py`.
