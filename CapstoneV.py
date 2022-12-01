'''
Task 1:
=======
Categorise which type of NLP application applies for each of
the following use-cases:
(Use the categories we have discussed on this bootcamp so far)

a. A model that allocates which mail folder an email should be sent to
(work, friends, promotions, important), like Gmail’s inbox tabs.

b. A model that helps decide what grade to award to an essay question.
This can be used by a university professor who grades a lot of classes
or essay competitions.

c. A model that provides assistive technology for doctors to provide
their diagnosis. Remember, doctors ask questions, so the model will
use the patients’ answers to provide probable diagnosis for the
doctor to weigh and make decisions.

My Answers:
===========
(I got some help here as well: https://research.aimultiple.com/nlp-use-cases/)

a. Text Classification

b. Automatic Summarization
More specifically: Extractive summary

c. Question Answering
More specifically: (Artificial Intelligence, Recurrent Neural Network)
(https://www.techtarget.com/searchenterpriseai/definition/recurrent-neural-networks)

**I don't know if I need to explain why or not. If that is necessary, I will happily resubmit the assignment.

======================================================================================================
Task 2:
=======
Think about your environment — school, work or home — and think of a
problem you face that can be solved by Natural Language Processing. Be as
descriptive as possible and show what value it will add to the environment
in question.

For example, if you are a stand-up comedian, you can come up with a
model that analyses the topics and areas your audience responds to the
most. This can be done by, say, identifying tweets (or Facebook posts) that
have the most ‘retweets’ (or ‘likes’). The tweets or posts will then be
categorised into topics and if you want to create a new comic routine, you
can stick to the topics mined using your followers’ reactions! So, think of a
scenario that applies to your life/work/school and how you can apply NLP to
your environment, and save that as nlp.txt

My Answer:
==========

I will be starting a job soon working within a search engine. I will have to search and analyze sensitive information then choose if this needs to be removed from the search engine or websites (violating community guidelines). I'm sure that a great deal of machine learning is already used in this process, but if not, it would be interesting to use nlp text classification to flag sensitive content once it is posted, automatic summarisation for finding emotional meaning and relevant flagged information within a large file of information, Sentiment analysis when looking at political/geopolitical tensions to predict if an influx of sensitive information may be coming, or even AI Language processing to see if the human moderator is biased in their assumation of the information being sensitive or not. 

At the end of the day, human error is so common within our increasingly complex world, that we cannot continue to rely on single people to make judgements based on the fate of all people. Hopefully, technology will continue to be that needed moderator.

========================================================================================================
Task 3:
=======
Read up on any innovative technology using NLP (by companies such as
Google or IBM, for instance) and write a brief summary about the
technology, what it achieves/does, and an overview of how it works.
To take an example, you may have noticed Gmail’s auto-response
suggestions on your incoming emails. If I send an email to your Gmail
address asking for an appointment, on opening the mail you would notice
Gmail’s automatically suggested response options such as “Yes, that works
for me” and “Sorry, I’m not available at that time.”

My Answer:
==========

(I researched here: https://intellipaat.com/community/883/how-does-the-google-did-you-mean-algorithm-work#:~:text=Many%20search%20engines%20use%20this,modified%20query%20to%20the%20user.)

(I researched here: http://www.norvig.com/spell-correct.html)

I researched Google's ‘spell-checking’ algorithm which is most commonly seen during a google search as "Did you mean: {word}?" Many companies currently use this as well in almost any search bar within their website. It is accomplished by using masses of nlp data and a spelling correction nlp application. The algorithm analyzes the most used words and counts occurrences for each word. It finds words through edit distance. Edit distance is based on the evaluation of the amount of words, their popularity, and how they related to the search. We can also work within probability and Bayes' Theorem to find likely solutions to our search errors.




I'm not sure if there is a word count of how much to write. Please let me know if this is sufficient or if more information is needed.
'''