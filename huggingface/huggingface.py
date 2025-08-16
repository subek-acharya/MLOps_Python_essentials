from transformers import pipeline

generator = pipeline("text2text-generation", model = "t5-base")

#Summarize
output = generator("summarize: For example, if a newspaper wanted to print an image in the 1870s, they had to commission an engraver to etch a copy of the photograph onto a steel plate by hand. These plates were used to press the image onto the page, but they often broke after just a few uses. This process of photoengraving, you can imagine, was remarkably time consuming and expensive.")

print(output)