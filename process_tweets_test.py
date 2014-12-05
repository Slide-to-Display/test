import process_tweets
import Tweet

# Test Individual feature of the function process_raw_tweet


def test_process_raw_tweets():
    # expecting all the return-value to be in lower case and trimmed
    # the following test casese focus on getting rid of unncessary symbols or
    # strings

    # testing simple cases (switching to lower case)
    assert process_tweets.process_raw_tweet('Best DJ, W&W') == 'best dj, w&w'

    # testing the implementations dealing with "@"
    assert process_tweets.process_raw_tweet("@LitieDaZhu") == ''
    assert process_tweets.process_raw_tweet(
        "don't you like @Kinagrannis's music") == "don't you like music"
    assert process_tweets.process_raw_tweet(
        "i am just super confused right now @@, aren't you") == "i am just super confused right now aren't you"
    assert process_tweets.process_raw_tweet(
        "hello world @LitieDaZhu") == 'hello world '
    # testing the implementations dealing with hashtags
    assert process_tweets.process_raw_tweet("#LOL!") == "lol,"
    assert process_tweets.process_raw_tweet(
        "#i can graduate this semester woohoo#") == "i can graduate this semester woohoo#"
    assert process_tweets.process_raw_tweet(
        "i think the best #csclass I've taken at #rpi is possibly #sdd") == "i think the best csclass i've taken at rpi is possibly sdd"
    assert process_tweets.process_raw_tweet(
        "this is the best place ever www.rpi.edu") == 'this is the best place ever '
    # testing the implemntaitions dealing with websites/http related
    assert process_tweets.process_raw_tweet(
        'wanna check out this site later https://www.ohbay.com please?') == "wanna check out this site later please,"
    assert process_tweets.process_raw_tweet(
        "what is that site again i forgot http://wwww.ratemyprofe, what's next?") == "what is that site again i forgot what's next,"

    # testing the remove-white-space feature
    assert process_tweets.process_raw_tweet(
        "heyo              boi!") == "heyo boi,"
    assert process_tweets.process_raw_tweet(
        "i just wanna use                  to troll, white space that is!") == "i just wanna use to troll, white space that is,"

    # testing punctuations
    assert process_tweets.process_raw_tweet(
        "so.....what's next ,,,???!!!!") == "so,,,,,what's next ,,,,,,,,,,"
    assert process_tweets.process_raw_tweet(
        "why can't school be less depressing?!") == "why can't school be less depressing,,"

# Test the function of creating Tweet object from processing the raw-data/json data
# Becuase this function is essentially processing raw tweets and apply process_raw_tweets(tweet) function to process these raw tweets
# we are focusing on testing on encapsulating raw data into Tweet object


def test_extract_fetched_tweets():
    tweets, processed_tweets = process_tweets.extract_fetched_tweets(
        "raw_twitter_input.json")
    expected = ["text: I love John. | sentiment:",
                "text: In China, a man divorced and sued his wife for about $120,000 for being ugly and won the case. | sentiment:",
                "text: Things China Has Banned - http://t.co/JOpIWNte5W http://t.co/ygseYfwwaG | sentiment:",
                "text: Chancellor George Osborne: Direct flight from Manchester to mainland China is a step closer #Manchester http://t.co/M9BCZLNCFb | sentiment:"]
    #assert tweets.__str__() in expected.__str__()
    for i in range(0, len(tweets)):
        assert expected[i] in str(tweets[i])

    process_tweets.analyse_tweets(tweets, processed_tweets)
    for i in range(0, len(tweets)):
        assert (tweets[i].sentiment == '')

# Test the function of analyzing the sentiment of each tweet
# Because the accuracy is not really under our control
# It depends on the coreNLP, which's developed by Stanford NLP lab
# Therefore, we just need to ensure there's no syntactic erros
# Moreover, the sentiment analyzer should ideally generate a sentiment for
# each tweet (no empty string)


def test_analyse_tweets():
    tweets, processed_tweets = process_tweets.extract_fetched_tweets(
        "raw_twitter_input.json")
    process_tweets.analyse_tweets(tweets, processed_tweets)
    for i in range(0, len(tweets)):
        assert not(tweets[i].sentiment == '')
