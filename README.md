# tweet-profanity
A small program which determines the degree of profanity  of tweets based on list of slur words.
I have used a dictionary to store the slur words along with its impact value on profanity.
for each tweet i have calculated the profanity by summing up the impact of tweets the multiplying the count of total slur words in the tweet.
why such assumptions :
->diiferent slur words have different magnitude of impact
->using more slur words increases the profaninty even more
however we can use some other functions instead of simply multiplying by the count.
