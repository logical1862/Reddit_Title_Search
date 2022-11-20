import praw
import pandas as pd
from datetime import datetime, timedelta


def search_timeframe(timeframe: str):
    """
    Returns a dictionary of timeframes to search by.   
    TODO: needs error checking
    """

    time_now = datetime.utcnow()
    time_dict = {
        'hour': time_now - timedelta(hours=1), 
        'day': time_now - timedelta(days=1),
        'week': time_now - timedelta(days=7),
        'month': time_now - timedelta(weeks=4),
        'year': time_now  - timedelta(weeks=52),
        'all': time_now - timedelta(weeks=260)
        }
    return time_dict.get(timeframe)

def post_data_list(post):
        """
        given a reddit post in the praw module format, returns a list of information about the post 
        [title, score, subreddit, text_content, date posted]
        """
        
        return [
            R'{}'.format(post.title), # format string for possible escape code 
            post.subreddit,
            post.score,            
            str(post.selftext),
            datetime.date(datetime.fromtimestamp(post.created))
            ]

def save_to_csv(df: pd.DataFrame):
    """
    saves a given pandas DataFrame object to a .csv file in the cwd with title 'redditinfo.csv'
    """
    path='redditinfo.csv'
    with open(path, 'w', encoding='utf-8') as f:              
        df.to_csv(f, index=False, line_terminator='\n')
        f.close()




def main(search_subred, search_str, search_sort_str, search_time, result_limit:int):
    # initialize praw instance with info in praw config file
    reddit_read = praw.Reddit('title_search')

    ## alert user to missing parameter and prompt for re-entry in terminal window
    while search_str == '':
        print('error: you must enter a keyword to search')
        search_str = input('keyword?: ')

    # set api call params based on input
    if search_subred == '':
        search_subred = 'all'
    

    search_time = search_timeframe(search_time)
    

    result_limit_int = int(result_limit)



    top_post_df = pd.DataFrame(data=[], columns=['Title', 'score', 'subred', 'text', 'created on'])


    subred_relevance = reddit_read.subreddit(search_subred).search(search_str)
    subred_sorted = reddit_read.subreddit(search_subred).search(search_str, sort=search_sort_str)

    if search_sort_str == 'top' or 'hot' or 'new':
        search_sort = reddit_read.subreddit(search_subred).search(search_str, sort=search_sort_str)

    else:
        search_sort = reddit_read.subreddit(search_subred).search(search_str)

    #run and print query results
    print(
        """ 
    ---------------------------
    reddit post keyword search:
    ---------------------------
            """
    )
    print(f'with credentials: {reddit_read.user.me()} :\n')
    print('result.) posted date : subreddit :: title\n')

    top_post_df = pd.DataFrame(data=[], columns=['title', 'subreddit', 'score', 'text', 'created on'])
    x = 0
    for post in search_sort:
        post_info = post_data_list(post)
        title = post_info[0]
        title_char_limit = title[:50]
        subreddit = post_info[1]
        post_date = post_info[4]

        #get timeframe for query
        
        search_date = datetime.date(search_time)
    
        # if post date is within parameters 
        if post_date > search_date:
            # append dataframe
            top_post_df.loc[(len(top_post_df.index) - 1)] = post_info

            print(f'{x+1}.) {post_date} : {subreddit} :: {title_char_limit}...')

            # break loop if query limit reached
            x += 1
            if x == int(result_limit):
                break

    # open/append csv file with post data
    save_to_csv(top_post_df)
                        
    print( f"\n--> {x} posts found with title matching search: '{search_str}'. \nIn subreddit: '{search_subred}'. \nSorted by: '{search_sort_str}' \nIn the past '{search_time}'.")

   
 