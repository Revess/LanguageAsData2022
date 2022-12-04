Bas Maat - 2749086
Elpida Krili - 2735820

The purpose of the corpus is to analyze the distribution of 500 tweets based on Dutch (ISO-639-3: nl) and 
Spanish (ISO-639-3: es) concerning the topic of U.S politics, more particularly Donald Trump. 
This comparison will be based on the extraction and comparison with lemmas, tokens, stop words and 
pos tags between these two languages. 

The dataset has been collected using the Tweepy API, with the search_tweets method. Since this method
has limitations in the download size (only 100 tweets) it was combined with the Cursor object which allowed
to scrape up to 500 Tweets. We noticed that there is a great lack in the Twitter language detection engine 
and thus kept it to 500 Tweets, if the max_tweets would be set to 1000 Tweets for instance the API would only
return about 550 Tweets. This Twitter data is then parsed into a Pandas DataFrame (one for each langauge).
These dataframes can be found in ./data/[LANG].csv.
The used search query is:
"(#trump OR #trump2022 OR #Trump OR #Trump2022 OR #Trump2020 OR #trump2020) AND (lang:nl)-filter:retweets"
and for Spanish:
"(#trump OR #trump2022 OR #Trump OR #Trump2022 OR #Trump2020 OR #trump2020) AND (lang:es)-filter:retweets"

Through the corpus, we want to detect the feelings and attitudes of the Spanish and Dutch target groups by 
retrieving data from Twitter and understand how differently each target group perceives this particular topic. 
For this reason we use n-grams to illustrate the distirbution of the Dutch and Spanish tweets where we can 
observe that the Spanish dataset displays longer tweets meaning that the Spanish speakers are using more tokens 
to describe their attitudes towards Donald Trump. 

Furthermore, the n-grams show that the Dutch pos-tags are more equally distributed than the Spanish pos-tags. 
For instance, the n-gram of the spanish dataset accumulates the pos-tags in proper nouns showing that the parts 
of speech displayed in the dutch ngram are more frequent than the spanish.

When it comes to the top n-grams it is obvious that the named entity Trump is mostly used by both target groups 
of the Twitter users than the rest of the tokens which indicates that the person Trump is widely debated by both parties. 
Moreover, the n-gram displaying the Dutch and spanish number of tweets per token shows that stopwords such as articles are used in a 
greater extent than the other parts of speech as well as the personal pronouns, such as 'I' and 'all' which 
give a more personal tone in the expression of the attitude towards the topic.

Furthermore, the Tweets of both Spanish and Dutch users show some interesting facts about their attitude and 
the way they express their opinion through them. For instance, the choice of the emojis and the use of sarcasm 
and irony in the dutch twitter shows that dutch users use an indirect way of expressing their support or opposition 
agains Donald Trump while the Spanish users express their negative or positive attitude in a more straightforward 
way by using more explicit words. For example:

"Trump is een dood spoor.",Twitter for iPhone,143402128,EMN,EMN_51314,Netherlands,-koffie-🏹-niet links niet rechts maar wel rechtshandig-Dordogne -⚽-trance-iPhone 14-F1-podcasts-Houten-nieuwsnieuwsgierig- getrouwd op 210522 - groen/blauw".

In this tweet the user expresses his/her opposition to Trump by making a reference to football so his/her opinion is less explicit and indirect.

"El tema de #Trump2024 y #DeSantis2024 es promovido por los #RINO y #Democratas para dividir a los conservadores, sa… https://t.co/q1gv3zr2bu",Twitter for Android,1531734912830685185,CONSERVATIVE CORNER,conservcorner1,,"Defender los principios conservadores Paleo liberales/ Paleo Conservadores. Politicamente Incorrectos. Cuenta manejada por varios CM. Agenda Guatemala 🇬🇹"

Links: 
Use of Twitter API:
    https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
Tweepy API:
    https://docs.tweepy.org/en/stable/api.html
Spanish Stopword list: 
    https://github.com/Alir3z4/stop-words/blob/master/spanish.txt
Dutch Stopword list:
    https://github.com/stopwords-iso/stopwords-nl/blob/master/stopwords-nl.txt
Twitter license:
    https://developer.twitter.com/en/developer-terms/agreement-and-policy