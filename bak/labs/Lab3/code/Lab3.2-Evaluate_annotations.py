import pandas as pd
import glob
import os.path
import random
from itertools import combinations
from sklearn.metrics import cohen_kappa_score, confusion_matrix
terms = ["meat", "protein", "diet"]
categories = ["positive", "negative", "neutral"]

# When we use the random function, we should set a fixed seed, if our results should be reproducible
random.seed(733)

for term in terms:
    print(term)
    annotations = {}

    # Read in the data
    for sheet in glob.glob("../data/annotations/annotationsheet_" + term +"*.tsv"):
        filename, extension = os.path.basename(sheet).split(".")
        prefix, term, annotator = filename.split("_")

        # Read in annotations
        annotation_data = pd.read_csv(sheet, sep="\t", header=0, keep_default_na=False)
        annotations[annotator] = annotation_data["Annotation"]

        # The example sheets are not annotated. I am using random annotations here. Make sure to comment this part out.
        annotations[annotator] = random.choices(categories, k=len(annotation_data))

    annotators = annotations.keys()
    # Calculate agreement between pairs of annotators. The order of the pair does not matter (a1,a2) is the same as a2,a1)
    # With two annotators, you only have a single pair.
    # If you have three annotators, you need to compare (a1,a2) (a1,a3) (a2,a3)

    for annotator_a, annotator_b in combinations(annotators, 2):
        agreement = [anno1 == anno2 for anno1, anno2 in  zip(annotations[annotator_a], annotations[annotator_b])]
        percentage = sum(agreement)/len(agreement)
        print(annotator_a, annotator_b)
        print("Percentage Agreement: %.2f" %percentage)
        kappa = cohen_kappa_score(annotations[annotator_a], annotations[annotator_b], labels=categories)
        print("Cohen's Kappa: %.2f" %kappa)
        confusions = confusion_matrix(annotations[annotator_a], annotations[annotator_b], labels=categories)
        print(confusions)
        print

