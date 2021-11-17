# importing library to remove punctuations from a word
import re

# reading file 
file1=open("tweet.txt",'r+')

# reading all the tweets,each line is a tweet
tweets=file1.readlines()

# dictionary storing the racial slur words along with their values(impact of the word)
racial_slurs= {'word1':2, 'word2':4, 'word3':5, 'word4':6, 'word5':9}


# count_slur_words : reports count of slur words in each tweet
# current_impact : reports the summation impact of all slur words in each tweet
# res : reports the total effect of slur words in each tweet
for i in range(len(tweets)):
  count_slur_words,current_impact=0,0;
  single_tweet=tweets[i].split()
  for j in range(len(single_tweet)):
    search_word=single_tweet[j].lower()
    search_word=re.sub(r'[^\w\s]', '', search_word)
    if search_word in racial_slurs.keys():
      current_impact+=racial_slurs[search_word]
      count_slur_words+=1
  res=current_impact*count_slur_words
  print("Tweet",i+1," :",res)
