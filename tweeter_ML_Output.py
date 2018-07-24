Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: C:\Users\dell\Desktop\MTA Training Python\tweeter_ML.py ======
>>> tweets
[(['love', 'this', 'car'], 'positive'), (['this', 'view', 'amazing'], 'positive'), (['feel', 'great', 'this', 'morning'], 'positive'), (['excited', 'about', 'the', 'concert'], 'positive'), (['best', 'friend'], 'positive'), (['not', 'like', 'this', 'car'], 'negative'), (['this', 'view', 'horrible'], 'negative'), (['feel', 'tired', 'this', 'morning'], 'negative'), (['not', 'looking', 'forward', 'the', 'concert'], 'negative'), (['enemy'], 'negative')]
>>> word_features
dict_keys(['love', 'this', 'car', 'view', 'amazing', 'feel', 'great', 'morning', 'excited', 'about', 'the', 'concert', 'best', 'friend', 'not', 'like', 'horrible', 'tired', 'looking', 'forward', 'enemy'])
>>> extract_features
<function extract_features at 0x0000000002B4E620>
>>> training_set
[({'contains(love)': True, 'contains(this)': True, 'contains(car)': True, 'contains(view)': False, 'contains(amazing)': False, 'contains(feel)': False, 'contains(great)': False, 'contains(morning)': False, 'contains(excited)': False, 'contains(about)': False, 'contains(the)': False, 'contains(concert)': False, 'contains(best)': False, 'contains(friend)': False, 'contains(not)': False, 'contains(like)': False, 'contains(horrible)': False, 'contains(tired)': False, 'contains(looking)': False, 'contains(forward)': False, 'contains(enemy)': False}, 'positive'), ({'contains(love)': False, 'contains(this)': True, 'contains(car)': False, 'contains(view)': True, 'contains(amazing)': True, 'contains(feel)': False, 'contains(great)': False, 'contains(morning)': False, 'contains(excited)': False, 'contains(about)': False, 'contains(the)': False, 'contains(concert)': False, 'contains(best)': False, 'contains(friend)': False, 'contains(not)': False, 'contains(like)': False, 'contains(horrible)': False, 'contains(tired)': False, 'contains(looking)': False, 'contains(forward)': False, 'contains(enemy)': False}, 'positive'), ...]
>>> tweet = 'Lary is my friend'
>>> classifier.classify(extract_features(tweet.split()))
'positive'
>>> tweet = 'Lary is not my friend'
>>> classifier.classify(extract_features(tweet.split()))
'negative'
>>> tweet = 'Lary is not my best friend'
>>> classifier.classify(extract_features(tweet.split()))
'positive'
>>> tweet = 'Lary is not my good friend'
>>> classifier.classify(extract_features(tweet.split()))
'negative'
>>> 
