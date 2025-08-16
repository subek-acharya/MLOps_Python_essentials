from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication

# Initialize interactive login authentication
interactive_auth = InteractiveLoginAuthentication()

# Connect to the workspace
workspace = Workspace(
    subscription_id="ec5fcd7c-27be-4f68-9e3e-521b665faa5d",
    resource_group="demo-try-azureml",
    workspace_name="demo-try-azureml",
    auth=interactive_auth
)

print("Workspace details:")
print(f"Name: {workspace.name}")
print(f"Location: {workspace.location}")
print(f"Resource Group: {workspace.resource_group}")


# Create the workspace using the specified parameters
ws = Workspace.create(
    name="demo2",
    subscription_id="ec5fcd7c-27be-4f68-9e3e-521b665faa5d",
    resource_group="demo2",
    location="eastus",
    auth=interactive_auth,
    create_resource_group=True,
    exist_ok=True
)

# Get workspace details
ws.get_details()

# Write the details of the workspace to a configuration file
ws.write_config()

##################
