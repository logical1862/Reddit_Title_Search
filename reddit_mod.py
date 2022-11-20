from datetime import datetime, timedelta
import praw
import pandas as pd


# reddit api auth
reddit_read = praw.Reddit('title_search')


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

def save_to_csv(dataframe: pd.DataFrame):
    """
    Saves a given pandas DataFrame object to a .csv file in the cwd with title 'redditinfo.csv'
    """
    path='redditinfo.csv'
    with open(path, 'w', encoding='utf-8') as f:              
        dataframe.to_csv(f, index=False, line_terminator='\n')
        f.close()

def get_results(subreddit_to_search, search_str, search_sort_str, search_time, result_limit):
    """Given search parameters, returns pandas df with query results and data"""
    top_post_df = pd.DataFrame(
        data=[],
        columns=['title', 'subreddit', 'score', 'text', 'created on']
        )

    result_count = 0
    api_results = reddit_read.subreddit(subreddit_to_search).search(search_str, sort=search_sort_str)


    for post in api_results:

        title = post.title
        title_char_limit = title[:50]
        subreddit = post.subreddit
        post_date = datetime.fromtimestamp(post.created)
        score = post.score


        # if post date is within parameters
        if post_date > search_time:
            # append dataframe
            last_position = (len(top_post_df.index) - 1)
            top_post_df.loc[last_position] = [title, subreddit, score, post.selftext, post_date]

            print(f'{result_count+1}.) {post_date} : {subreddit} :: {title_char_limit}...')

            # break loop if query limit reached
            result_count += 1
            if result_count == result_limit:
                continue
    return (top_post_df, result_count)

def intro_text():
    """Prints intro text body to screen, no return"""
    print(
        """
        ---------------------------
        Reddit Post Keyword Search:
        ---------------------------
        """
        )
    print(f'With user credentials: {reddit_read.user.me()} :\n')
    print('<Result#>.) <Datetime posted> : <Subreddit posted in> :: <Title of post>\n\n')

def display_results(subreddit_to_search, search_str, search_sort_str, search_time, num_results):
    """Prints total results and search parameters to screen, no return"""
    print(f"\n--> {num_results} posts found with title matching search query: '{search_str}'.")
    print(f"In subreddit: '{subreddit_to_search}'.")
    print(f"Sorted by: '{search_sort_str}'")
    print(f"In the past '{search_time}'.")

def main(subreddit_to_search, search_str = 'apple', search_sort_str = 'relevant', search_time = 'day', result_limit:int = 50):

    if not subreddit_to_search:
        subreddit_to_search = 'all'
    timeframe = search_timeframe(search_time)

    intro_text()

    results_df, num_of_results = get_results(
        subreddit_to_search,
        search_str,
        search_sort_str,
        timeframe,
        result_limit
        )

    display_results(subreddit_to_search, search_str, search_sort_str, search_time, num_of_results)

    # open/append csv file with post data
    save_to_csv(results_df)
