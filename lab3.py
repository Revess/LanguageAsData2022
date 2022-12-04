import pandas as pd
import stanza
from googletrans import Translator

translator = Translator()

# Read in the data
language = "nl"
article_file = "./data/"+language+"Dataset.csv"
content = pd.read_csv(article_file)

# Make sure to be very clear on how you determined the annotation terms.
# You can also use ngrams, e.g. "vegan diet" instead of "diet"
terms = ["Trump", "trump", "Donald", "waarheid", "haat"]

# Prepare the nlp pipeline
stanza.download(language)
nlp = stanza.Pipeline(language,  processors='tokenize,pos,lemma')

# Get all instances.
# Here, we do a simple string comparison.
# You might want to check for the lemma instead (depending on your research question)
annotation_instances = {}
for article in content["text"]:
    # Filter out empty articles
    if len(article.strip())>0:
        processed_article = nlp(article)
        for sentence in processed_article.sentences:
            for term in terms:
                if term in sentence.text:
                    # Save all instances for each term
                    # This is a condensed way of updating a dictionary. Make sure you understand what is happening
                    annotation_instances[term] = annotation_instances.get(term, []) + [sentence.text.strip()]

num_annotators = 2
for i in range(1, num_annotators + 1):
    for term in terms:
        df = {"Term":[],"Instance":[],"Annotation":[]}
        for instance in annotation_instances[term]:
                instance = translator.translate(instance, src=language, dest="en").text
                df["Term"].append(term)
                df["Instance"].append(instance)
                df["Annotation"].append("x")