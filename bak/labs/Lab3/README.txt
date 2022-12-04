This is the code for Lab 3 of the course Language as Data 2020, Vrije Universiteit Amsterdam. 
It should only be used for the purpose of the course and not be re-distributed. 

Author: Lisa Beinborn

Annotation:
In this lab, you will setup an annotation task for your dataset.

1) Determine the interesting terms for your dataset. These terms can be derived based on the statistics you analyzed in Lab2. For deeper insights, it makes sense to additionally consider insights from a qualitative analysis of the dataset.

2) Determine the annotation categories for your annotation task. Do this very carefully! Sometimes, it is easier to annotate 5 categories than 2 categories.

3) Write down the annotation guidelines in annotation_guidelines.txt. Get feedback from other students on your annotation guidelines.

4) Modify Lab3.1-Create_annotation_sheets.py and create the annotation sheets for your dataset.

5) Annotate the instances separately. Do not discuss the annotations with your partner and do not modify the annotation guidelines after you started.

Evaluation:
In order to evaluate your annotation, please install the module sklearn into your LaD environment:
conda install -c intel scikit-learn

1) Modify 3.2_Evaluate_annotations.py and evaluate your annotations.

2) Discuss the quality of your annotations. If the quality is worse than expected, discuss potential reasons and how the annotation setup could be improved


Generating Tables:
We have already seen how we can save data in a csv or tsv file, to generate a table.
In Lab3.3, you find two other methods to generate tables.

Please install the module tabulate into your LaD environment:
conda install tabulate

1) Generate latex tables

2) Generate markdown tables
