import requests
from typing import List
from greetings_bot.vcs_client.base import VCSClient


class GitLabClient(VCSClient):
    """Wrapper around GitLab API for MR notes."""

    def __init__(self, api_url: str, project_id: str, token: str):
        self.api_url = api_url
        self.project_id = project_id
        self.token = token
        self.headers = {"PRIVATE-TOKEN": token}

    def get_token_username(self) -> str:
        resp = requests.get(f"{self.api_url}/user", headers=self.headers)
        resp.raise_for_status()
        return resp.json()["username"]

    def get_mr_notes(self, mr_iid: str) -> List[dict]:
        url = f"{self.api_url}/projects/{self.project_id}/merge_requests/{mr_iid}/notes"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def post_mr_note(self, mr_iid: str, message: str) -> None:
        url = f"{self.api_url}/projects/{self.project_id}/merge_requests/{mr_iid}/notes"
        resp = requests.post(url, headers=self.headers, data={"body": message})
        if resp.status_code != 201:
            raise RuntimeError(
                f"Failed to post note: {resp.status_code} - {resp.text}"
            )
