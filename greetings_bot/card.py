import yaml
import random
from typing import List


class GreetingCard:
    """Handles messages and images."""

    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_messages(self) -> List[str]:
        with open(self.config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)["messages"]

    def random_wish(self) -> str:
        messages = self.load_messages()
        return random.choice(messages)

    def random_image_url(self) -> str:
        with open(self.config_file, "r", encoding="utf-8") as f:
            images = yaml.safe_load(f)["cards"]

        if not images:
            raise RuntimeError("No images found in cards YAML")

        return random.choice(images)
