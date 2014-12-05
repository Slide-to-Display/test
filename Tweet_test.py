import Tweet
def test_TweetClass_single_tweet():
	tweet1="Xiaoman is smart."
	tweet_object1=Tweet.Tweet(tweet1,'','')
	assert tweet_object1.__str__() in "text: Xiaoman is smart. | sentiment: "

	tweet2="Litie is looking fly."
	tweet_object2=Tweet.Tweet(tweet2,'','')
	assert tweet_object2.__str__() in "text: Litie is looking fly. | sentiment: "
	
	tweet3="Mike is happy to be in slide-to-display."
	tweet_object3=Tweet.Tweet(tweet3,'','positive')
	assert tweet_object3.__str__() in "text: Mike is happy to be in slide-to-display. | sentiment: positive"
	
	tweet4="Rachel fails to handle her stress."
	tweet_object4=Tweet.Tweet(tweet4, '', 'negative')
	assert tweet_object4.__str__() in "text: Rachel fails to handle her stress. | sentiment: negative"
	

def test_TweetClass_tweets():

	
	tweets=["I love John.", 
		"Torturing amp; Eating dogs in China or raping dogs in Denmark? which is worse?", 
		"lmao my brother said that if china gets together for a war they legit would win bc the population of people",
		"In China, a man divorced and sued his wife for about $120,000 for being ugly and won the case.",
		"Things China Has Banned",
		"Chancellor George Osborne: Direct flight from Manchester to mainland China is a step closer."]
	
	Tweet_objects=[];
	for i in range (len (tweets)):
		Tweet_objects.append(Tweet.Tweet(tweets[i],'',''))
	for i in range (len(Tweet_objects)):
		assert tweets[i] in Tweet_objects[i].__str__()
		
