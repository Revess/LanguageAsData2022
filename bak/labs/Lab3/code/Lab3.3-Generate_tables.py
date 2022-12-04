import pandas as pd

# Different ways to output a table
confusionmatrix = {"positive": [11,12,10], "negative": [ 6,11,3], "neutral": [14,8,15]}

pandas_table = pd.DataFrame(confusionmatrix, index=["positive", "negative", "neutral"])
print(pandas_table)

markdown_table = pandas_table.to_markdown()
print(markdown_table)

latex_table = pandas_table.to_latex(caption="Confusion matrix for annotator a1 and a2 for the term \emph{meat}")
print(latex_table)