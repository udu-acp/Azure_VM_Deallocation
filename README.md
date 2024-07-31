# Azure_VM_Deallocation

## In this repo, you will find a snippet that sets up Azure Credentials and then deallocates a VM. This can be useful when scheduling Matillion ETL jobs in an Azure VM while trying to keep your costs as low as possible.

Ensure to add all environment variables to a .env file and include .env in your .gitignore file to keep it from being tracked. Below are the variables used in the snippet.

```
SUBSCRIPTION_ID=
RESOURCE_GROUP=
VM_NAME=
AZURE_APP_TENANT_ID=
AZURE_APP_CLIENT_ID=
AZURE_APP_CLIENT_SECRET=
```
