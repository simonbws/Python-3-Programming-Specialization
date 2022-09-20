#!/usr/bin/env python
# coding: utf-8

# # Python Programming 3 - Course 2 : Project Part 1: Sentiment Classifier

#  To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

# In[ ]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
       for ch in punctuation_chars:
            word=word.replace(ch,"").lower()
            return word
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(sentence):
    sent_lst = sentence.split(" ")
    new_lst_sent = []
    for word in sent_lst:
        word = strip_punctuation(word).lower()
        new_lst_sent.append(word)
    pos_count = 0
    for word in positive_words:
        if word in new_lst_sent:
            pos_count = pos_count + 1

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(sentence):
    sent_lst = sentence.split(" ")
    new_lst_sent = []
    for word in sent_lst:
        word = strip_punctuation(word).lower()
        new_lst_sent.append(word)
    neg_count = 0
    for word in negative_words:
        if word in new_lst_sent:
            neg_count = neg_count + 1
    return neg_count

outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score,Negative Score, Net Score')
outfile.write('\n')

myfile = open('project_twitter_data.csv', 'r')
rows = myfile.readlines()[1:]
for line in rows:
    words = line.split()
    numbers = words[-1]
    twrt = numbers.split(',')
    print ('retweets: ', twrt[1], 'replies, times : ', twrt[2])
    pos_sco = 0
    neg_sco = 0
    for word in words:
        if word in positive_words:
            pos_sco = pos_sco + 1
        if word in negative_words:
            neg_sco = neg_sco + 1
    net_sco = pos_sco - neg_sco
    print ('Here are positive words: ', pos_sco, 'Here are negative words: ', neg_sco, 'Net score: ', net_sco )
    row_string = '{}, {}, {}, {}, {}'.format(twrt[1], twrt[2], pos_sco, neg_sco, net_sco)
    outfile.write(row_string)
    outfile.write('\n')


# In[ ]:




