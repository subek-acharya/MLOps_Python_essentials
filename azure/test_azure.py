from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication, InteractiveLoginAuthentication

workspace_name = "demo-try-azureml"
subscription_id = "" # Add your subscription Id by logging to your account
resource_group = "demo-try-azureml"
tenant_id = "" # Add your tenant id # Only needed for interactive login if required
workspace_region = "" # Add your workspace region


try:
    # Try to load the workspace using service principal authentication
    workspace = Workspace.get(name=workspace_name,
                              subscription_id=subscription_id,
                              resource_group=resource_group,
                              auth=service_principal)
    print("Workspace loaded successfully")
except Exception as e:
    print(f"Failed to load workspace with service principal: {e}")
    
    try:
        # Try interactive authentication if service principal fails
        interactive_auth = InteractiveLoginAuthentication(tenant_id=tenant_id)
        workspace = Workspace.get(name=workspace_name,
                                  subscription_id=subscription_id,
                                  resource_group=resource_group,
                                  auth=interactive_auth)
        print("Workspace loaded successfully with interactive login")
    except Exception as interactive_exception
        print(f"Failed to load workspace with interactive login: {interactive_exception}")
        # If the workspace does not exist, create it
        try:
            workspace = Workspace.create(name=workspace_name,
                                         subscription_id=subscription_id,
                                         resource_group=resource_group,
                                         location=workspace_region,
                                         auth=interactive_auth,
                                         create_resource_group=True,
                                         exist_ok=True)
            print("Workspace created successfully")
        except Exception as creation_exception:
            print(f"Failed to create workspace: {creation_exception}")


# Azure Virtual Desktop                                    9cdead84-a844-4324-93f2-b2e6bb768d07