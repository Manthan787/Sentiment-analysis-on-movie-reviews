from __future__ import division
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from math import log
import os
import re

"""
The data used by this script is now owned by me. It was collected by Bo Pang, Lillian Lee, and Shivakumar Vaithyanathan
for their research paper.
More about data and how it was collected: http://www.cs.cornell.edu/people/pabo/movie-review-data/
This script was written to process the polarity_dataset v1.0
"""


def collect_reviews(reviewClass):
    """ Returns the reviews of the given reviewClass from the dataset as a huge string"""
    files = os.listdir(reviewClass)
    entire_text = ""
    i = 0
    for file in files:
        i += 1
        f = open(reviewClass+'/'+file, "r")
        entire_text += f.read().lower()
    return entire_text


def get_count(text):
    """ Calculates the count of each word in the given text, ignores stopwords and punctuation symbols"""
    ignore = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    word_list = tokenizer.tokenize(text.lower())
    words = Counter(word for word in word_list if word not in ignore)
    return words


def calculate_likelihood(text, counts):
    """ Calculates the likelihood of the given text being in a particular reviewclass, based on the counts provided """
    prediction = 1
    text_count = get_count(text.lower())
    print text_count
    for word in text_count:
        term1 = text_count.get(word) * (counts.get(word, 0) + 1)
        term2 = sum(counts.values()) + len(counts)
        product = log(term1 / term2)
        prediction *= product
    return prediction


def predict(text):
    """ Predicts whether the given text belongs to Positive Class or Negative Class """
    pos_likelihood = calculate_likelihood(text, positive_count)
    neg_likelihood = calculate_likelihood(text, negative_count)

    if pos_likelihood > neg_likelihood:
        print "The review is positive"
    else:
        print "The review is negative"


# get positive text from the dataset
positive_text = collect_reviews('pos')
# get negative text from the dataset
negative_text = collect_reviews('neg')

# Get the word frequencies for the positive text
positive_count = get_count(positive_text)
# Get the word frequencies for the negative text
negative_count = get_count(negative_text)

# print positive_count.most_common(n=20)
# print negative_count.most_common(n=20)

pos_test = r"""I don't know how to start a movie review off, seeing as I've never written one. I feel my meager rating out-of-ten is enough information to tell those interested what I think of a particular movie. Birdman, however, is the exception.

I understand I'm an absolute stranger. Who gives a damn about what I have to think? My only hope is that after reading one fan's fanatic praise for Birdman, you will go and see it. In the interest of not over-hyping this movie (which many will feel I'm about to do), I will say it's nothing short of utterly amazing. Every aspect of the film is masterfully crafted and executed. Emmanuel Lubezki's cinematography only exemplifies this. The brilliant choice of always having the camera rolling lets the viewer see what happens before and after any given event. This added information creates a realism unknown to nearly every other movie ever made. What better way to capture the raw emotion and awkward stumbling of an angry outburst at your father than to show the immediate reaction of the ranter following her outburst; you get to see the anger slowly fade from her face as the reality of what she said sets in. Details like this are so often lost and these often- lost, immersive subtleties are what make Birdman the gargantuan triumph it is. Not to mention some of the transitions and dolly shots are just damn impressive.

Even though many movies are yet to come out this pre-Oscar season, I feel it is safe to say no other casting ensemble will come close to the performances given in Birdman. Michael Keaton, Zach Galifianakis, Emma Stone, Ed Norton, Amy Ryan, and every single other actor in the production execute their roles with professionalism that most movies are lucky to see in just one of their actors. Each actor didn't wait for their time to shine to pull out the big guns; every moment of screen time was utilized to its full potential. There isn't a second where the audience's immersion is broken by an awkwardly delivered line or a slightly out-of-place facial expressions or emotion.

The only criticism I have about the film is that more aren't like it. A smart, satirical movie that is capable of criticizing without being hypocritical is unfortunately rare. However, it's rather nice to have movies like this stand out from the crowd instead of being the norm, because the relative quality only makes them that much better.

So, in short, I implore you. I beg you. If you step into a movie theater once this year, let it be to watch this film. It deserves your attention."""

print "Likelihood for pos class"
neg_test1 = r""" For me, a complete and total waste of money and time. My friend fell asleep about 20 minutes into this self-indulgent piece of tripe.

This movie strains so hard to make itself 'important' and 'groundbreaking' that it never stops to see that it has been done before by Masters such as Woody Allen, Hitchcock and any late night black/white '40s movie.

The 'plot' is as old as the hills. Man is successful but inwardly unrewarded. He has also rejected his family in search of California movie gold. So, he wants to redeem himself and try his hand at serious theater. Throw in a disturbed and rehabbed daughter, a long-suffering but understanding wife, and a producer pulling his hair out because the 'play' isn't a success and you've got all you need to know.

The rest is a montage of suspected hallucinations, maybe suicides "who knows?" and you're left feeling empty, cheated and angry because you know somebody's trying to be nouveau and special but simply missed it completely by being too insider and artsy about the whole thing.

Do not waste your time. If you want to see what theater and Broadway are all about and need a laugh, watch The Producers with Zero Mostel instead. If you want deep, head scratching drama that goes nowhere, go ahead, pay up and watch this nonsense.

And, I might add, Michael Keaton, to me, was trying too hard, had few acting chops and it was embarrassing to watch him in this. He, like the character he played, was trying way too hard."""

neg_test2 = r"""I created this account for the sole purpose of reviewing this piece of junk. Coming in to this movie, I had heard bad things from people who had seen it but great things from critics. After leaving, the only good thing about it was the acting. This movie definitely was different and unique, but there's a difference from being different and making art and being different and making a piece of crap. The fact that this movie was nominated for best picture above a piece of art, such as Interstellar, is appalling. I do applaud the director for taking a risk and trying to make an unconventional movie, but he needed to first develop a plot in order to make a good movie. I strongly discourage anyone from wasting their time and money seeing this. If you want to watch a movie that is different and considered art, watch any Christopher Nolan, Stanley Kubrick, or Quentin Tarantino movie, not this pathetic excuse for entertainment. And to critics, please learn the difference between unconventional artistic movies and this bloody rubbish."""

predict(neg_test1)
predict(pos_test)