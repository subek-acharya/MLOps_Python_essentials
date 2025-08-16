from datasets import load_dataset

dataset = load_dataset("cornell-movie-review-data/rotten_tomatoes")

# print(dataset)

# Slect the "train" dataset and then import it to pandas
train = dataset["train"]

# print(train)

df = train.to_pandas()

print(df.describe())

print(df.head(20))