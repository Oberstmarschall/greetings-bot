import logging
from greetings_bot.card import GreetingCard
from greetings_bot.vcs_client.base import VCSClient


class GreetingBot:
    """Coordinates checking and posting greetings."""

    def __init__(self, client: VCSClient, card: GreetingCard, mr_iid: str):
        self.client = client
        self.card = card
        self.mr_iid = mr_iid

    def already_posted(self, username: str) -> bool:
        notes = self.client.get_mr_notes(self.mr_iid)
        return any(note.get("author", {}).get("username") == username for note in notes)

    def run(self) -> None:
        username = self.client.get_token_username()
        if self.already_posted(username):
            logging.info(f"Greeting already posted by {username}, skipping.")
            return

        wish = self.card.random_wish()
        image_url = self.card.random_image_url()
        message = f"{wish}\n\n<img src='{image_url}' width='100'>"

        self.client.post_mr_note(self.mr_iid, message)
        logging.info("Message posted to MR!")
