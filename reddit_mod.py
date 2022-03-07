import praw
import pandas as pd
from datetime import datetime, timedelta


def main(search_subred, search_str, search_sort_str, search_time, result_limit):

    reddit_read = praw.Reddit('title_search')


    print('---------------------------')
    print('reddit post keyword search:')
    print('---------------------------')


    if search_subred == '':
        search_subred = 'all'


    while search_str == '':
        print('error: you must enter a keyword to search')
        search_str = input('keyword?: ')


##define search time 
    time_now = datetime.utcnow()
    hour_result = datetime.utcnow() - timedelta(hours=1)
    day_result = datetime.utcnow() - timedelta(days=1)
    week_result = datetime.utcnow() - timedelta(days=7)
    month_result = datetime.utcnow() - timedelta(weeks=4)
    year_result = datetime.utcnow() - timedelta(days=365)
    all_result = datetime.utcnow() - timedelta(weeks=260)
    

    time_dic = {'hour':hour_result, 'day':day_result, 'week':week_result, 'month':month_result, 'year':year_result, 'all':all_result}

    if search_time == 'hour':
        search_time = time_dic.get('hour')

    elif search_time == 'day':
        search_time = time_dic.get('day')

    elif search_time == 'week':
        search_time = time_dic.get('week')

    elif search_time == 'month':
        search_time = time_dic.get('month')

    elif search_time == 'year':
        search_time = time_dic.get('year')

    else:
        search_time = time_dic.get('all') 

##result limit

    result_limit_int = int(result_limit)



    top_post_df = pd.DataFrame(data=[], columns=['Title', 'score', 'subred', 'text', 'created on'])


    subred_relevance = reddit_read.subreddit(search_subred).search(search_str)
    subred_sorted = reddit_read.subreddit(search_subred).search(search_str, sort=search_sort_str)

    if search_sort_str == 'top' or 'hot' or 'new':
        search_sort = subred_sorted

    else:
        search_sort = subred_relevance


#run and print results
    print('with credentials:', reddit_read.user.me(), ':')

    #main loop
    x = 1

    for post in search_sort:


            p_title = post.title
            p_score = post.score
            p_subred = post.subreddit
            p_data = post.selftext
            p_time = post.created
            p_date_post =datetime.utcfromtimestamp(p_time)

            #date time loop 
            date_search = datetime.date(search_time)
            date_post = datetime.date(p_date_post)

    

            if date_post > date_search and x <= result_limit_int:

                post_info =[p_title, p_score, p_subred, p_data, p_date_post]

            

                with open('redditinfo.csv', 'w'):

                        top_post_df.loc[len(top_post_df.index)] = post_info
                        top_post_df.to_csv('redditinfo.csv')

                        title_char_limit = p_title[:50]

                        print(x, '!', p_date_post, ':', p_subred, '::', title_char_limit, '...')
                        x = x + 1

                        
                        
    print('', x-1, 'posts found with title containing search: ', search_str, '. In subreddit:', search_subred, 'sorted by: ', search_sort_str,  'In timeframe: from', search_time, 'to', time_now)
