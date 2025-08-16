
from azureml.core.compute import ComputeTarget, AmlCompute
from azure.az_setup import workspace, ws

# Define AML compute target(s) to create
amlcomputes = {
    "cpu-cluster": {
        "vm_size": "STANDARD_DS3_V2",
        "min_nodes": 0,
        "max_nodes": 3,
        "idle_seconds_before_scaledown": 240,
    }
}

# Create AML compute targets
for ct_name in amlcomputes:
    if ct_name not in ws.compute_targets:
        compute_config = AmlCompute.provisioning_configuration(**amlcomputes[ct_name])
        ct = ComputeTarget.create(ws, ct_name, compute_config)
        ct.wait_for_completion(show_output=True)


# Deleting the workspace
ws.delete(delete_dependent_resources=True, no_wait=False)

# Deleting the workspace
workspace.delete(delete_dependent_resources=True, no_wait=False)
