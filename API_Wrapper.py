import requests


class BoredAPIWrapper:
    BASE_URL = "https://www.boredapi.com/api/activity"

    def get_random_activity(self, params=None):
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch activity: {response.status_code}")
