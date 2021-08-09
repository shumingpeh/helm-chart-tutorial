import yaml

from app.addition_math.client import HttpClient


class AppStore:
    http_client: HttpClient = None

    # Not putting this in init because we only want to load upon app starting
    def load(self):
        self.http_client = HttpClient()

    @staticmethod
    def _read_yaml(path: str) -> dict:
        return yaml.safe_load(open(path))


app_store = AppStore()