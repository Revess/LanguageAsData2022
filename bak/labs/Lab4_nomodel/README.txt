This is the code for Lab 4 of the course Language as Data 2020, Vrije Universiteit Amsterdam. 
It should only be used for the purpose of the course and not be re-distributed. 


Author: Lisa Beinborn

Requirements: 
Please add the following to your LaD environment.

pip install gensim
conda install networkx
conda install matplotlib
conda install seaborn

In Lab 4.1., you will learn how to query the lexical resource Babelnet. You need to obtain an API key first: https://babelnet.org/register. Please use your student e-mail address.

In Lab 4.2, you learn how to use pre-trained word representations from fasttext. For the example, you need to save the model wiki-news-300d-1M.vec.zip from https://fasttext.cc/docs/en/english-vectors.html in your data folder. Fasttext also provides models for many other languages. Note that jupyter notebook might crash if you run dimensionality reduction on the full model. In this case, either use a reduced vocabulary or run the code directly in Python (without jupyter notebook in between). 

In Lab 4.3, you learn to cluster documents using different document representations. 