from datasets import load_dataset
from huggingface_hub import list_datasets

available = list_datasets()
# print(len(available))

# Iterate through Datasetinfo objects and get the 'id' attributes
dataset_name = [dataset.id for dataset in available]

#print dataset names that don't contain a '/'
print([i for i in dataset_name if '/' not in i])