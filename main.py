# import azure libs to store credentials and manage VM
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
# import os for environment variables
import os
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

# Azure subscription ID
subscription_id = os.getenv("SUBSCRIPTION_ID")

# Resource group name and VM name
resource_group_name = os.getenv("RESOURCE_GROUP")
vm_name = os.getenv("VM_NAME")

# Initialize Azure credentials
credential = ClientSecretCredential(
    tenant_id=os.getenv('AZURE_APP_TENANT_ID'),
    client_id=os.getenv('AZURE_APP_CLIENT_ID'),
    client_secret=os.getenv('AZURE_APP_CLIENT_SECRET')
)


# Initialize ComputeManagementClient
compute_client = ComputeManagementClient(credential, subscription_id)

# Stop the VM
vm_stop = compute_client.virtual_machines.begin_deallocate(resource_group_name, vm_name)
vm_stop

## If you have a child process, you can use the wait function
# vm_stop.wait()

print(f"The VM {vm_name} has been stopped.")
