import redis
import datetime


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)

    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby(name='score:', value=article, amount=VOTE_SCORE)
            redis.hincrby(name=article, key='votes', amount=1)

def article_switch_vote(redis, user, from_article, to_article):
    # HOMEWORK 2 Part I
    
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEKIN_SECONDS)

    f_a_cut = datetime.datetime.fromtimestamp(redis.zscore('time:',from_article)) < cutoff
    
    t_a_cut = datetime.datetime.fromtimestamp(redis.zscore('time:',from_article)) < cutoff
    if (not f_a_cut) and (not t_a_cut):
        
        f_a_id = from_article.split(':')[-1]
        t_a_id = to_article.split(':')[-1]
        
        if redis.srem('voted:' + f_a_id, user) and redis.sadd('voted:' + f_a_id,user):
            
            #redis.zincrby(name='score:',value=from_article,amount= -VOTE_SCORE)
            redis.hincrby(name=from_article,key='votes:',amount= -1)
            
            #redis.zincrby(name='score:',value=to_article,amount=VOTE_SCORE)
            redis.hincrby(name=to_article,key='votes:',amount=1) 



redis = redis.StrictRedis(host='localhost', port=6379, db=0)
# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")
# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
# user:2 switches their vote from article:8 to article:1
article_switch_vote(redis, "user:2", "article:8", "article:1")

# Which article's score is between 10 and 20?
# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
article = redis.zrange(name='score:',start=10,end=20)
print redis.hget(name=article,key='link:')

