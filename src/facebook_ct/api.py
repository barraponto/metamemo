import requests
from purl import URL
from django.conf import settings


class CrowdTangleAPI:
    """API Client for CrowdTangle posts endpoint."""

    ENDPOINT = "https://api.crowdtangle.com/posts"

    def __init__(self, account):
        """Creates CrowdTangle API client for user account posts."""
        self.url = (
            URL(self.ENDPOINT)
            .query_params(
                {
                    "accounts": account,
                    "token": settings.CROWDTANGLE_FACEBOOK_API_KEY,
                    "timeframe": settings.CROWDTANGLE_POSTS_INTERVAL,
                    "count": settings.CROWDTANGLE_POSTS_COUNT,
                    "sortBy": "date",
                }
            )
            .as_string()
        )

    def __load_data(self):
        """Load data. @TODO: deal with errors."""
        response = requests.get(self.url)
        response.raise_for_status()
        data = response.json()
        return data["result"].get("posts", []), data["result"].get("nextPage")

    def __iter__(self):
        while self.url:
            posts, self.url = self.__load_data()
            for post in posts:
                yield post
