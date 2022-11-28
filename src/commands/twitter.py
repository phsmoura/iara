import click
from src.commands._twitter_modules import check_tweet_url, get_posts_url, get_accounts_interacted, write_database, write_report


DEFAULT_NUMBER = 10

@click.command()
@click.argument("username")
@click.option(
    "-t", "--tweet", required=False, help="Url of a single tweet.\nNot using this option will make it check target's media posts"
)
@click.option(
    "-nt", "--number-tweets", required=False, default=DEFAULT_NUMBER, help="How many media tweets will be checked.\nDefault is 10"
)
@click.option(
    "-it", "--interactions", required=False, default=DEFAULT_NUMBER, help="Number of accounts that liked or retweeted (without quoting) the post and will be checked.\nDefault is 10"
)
@click.option(
    "-o", "--out", required=False, default='iara_report', help="Output the report in a file"
)
def cli(username,tweet,number_tweets,interactions,out):
    """Check Twitter account or single post"""
    # TODO: Grab 1st number_tweets media posts -> get_posts_url()
    # TODO: Check image in tweet url -> check_tweet_url()
    # TODO: Grab accounts that interacted with the post -> get_accounts_interacted()
    # TODO: Write data in DB -> write_database()
    # TODO: Output report file -> write_report()
    # TODO: Get rid of repeating code lines

    if not tweet:
        # check first number_tweets user's media posts
        posts = get_posts_url(username,number_tweets)

        # Go through posts and check if AI detects object in image
        for post in posts:
            object_detected = check_tweet_url(post)
            if object_detected:
                accounts = get_accounts_interacted(interactions)
                write_database(username,tweet,accounts)
    else:
        object_detected = check_tweet_url(tweet)
        if object_detected:
            accounts = get_accounts_interacted(interactions)
            write_database(username,tweet,accounts)

    if out:
        write_report(username,tweet,out)
