import time
import praw
import config
from italianize_text import italianize_text

reddit = praw.Reddit(
    client_id=config.CLIENT_ID,
    client_secret=config.CLIENT_SECRET,
    password=config.PASSWORD,
    username=config.USERNAME,
    user_agent="python:reddit_italianizer_bot:v1.0.0 (by /u/ChickenNuggets6827)"
)


def check_mentions():
    for mention in reddit.inbox.mentions(limit=5):  # Adjust limit as needed
        # Skip already read mentions
        if mention.new:
            print(f"Mention from: {mention.author} - {mention.body}")

            # Get the parent of the comment where the bot was mentioned
            parent_comment = mention.parent()

            # Check if the parent is a comment and not a post (sometimes the parent can be a submission)
            if isinstance(parent_comment, praw.models.Comment):
                reply_text = italianize_text(parent_comment.body)
                parent_comment.reply(reply_text)
            else:
                print(f"Parent is not a comment, it's a submission: {parent_comment.id}")

            mention.mark_read()  # Mark the mention as read after responding


def run_bot():
    while True:
        try:
            check_mentions()
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait before checking again (30 seconds delay)
        time.sleep(60)


# Run the bot continuously
if __name__ == "__main__":
    run_bot()
