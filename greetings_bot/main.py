import argparse
import logging
from pathlib import Path
from greetings_bot.bot import GreetingBot
from greetings_bot.card import GreetingCard
from greetings_bot.vcs_client.factory import VCSFactory

logging.basicConfig(level=logging.INFO)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=False, help="VCS type", choices=["gitlab"], default="gitlab")
    parser.add_argument("--api-url", required=True, help="VCS API URL (e.g. https://gitlab.com/api/v4)")
    parser.add_argument("--project-id", required=True, help="VCS project ID")
    parser.add_argument("--mr-iid", required=True, help="Merge Request IID")
    parser.add_argument("--token", required=True, help="Access Token")
    parser.add_argument("--config_file", default="config.yml", type=Path, help="Path to config file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    logging.info("hello")

    client = VCSFactory.create(args)
    card = GreetingCard(args.config_file)
    bot = GreetingBot(client, card, args.mr_iid)
    bot.run()
