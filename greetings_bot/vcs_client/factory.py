from greetings_bot.vcs_client.gitlab import GitLabClient


class VCSFactory():

    @staticmethod
    def create(platform: str, **kwargs):
        if platform == "gitlab":
            return GitLabClient(kwargs["api_url"], kwargs["project_id"], kwargs["token"])
        else:
            raise ValueError("Client not implemented")
