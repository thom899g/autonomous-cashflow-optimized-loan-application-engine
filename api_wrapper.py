import requests
from typing import Dict, Any
from .config import Configuration

class APIWrapper:
    """
    Wrapper class for interacting with financial institution APIs.
    Implements retry logic and handles rate limiting.
    """

    def __init__(self):
        self.config = Configuration()
        self.session = requests.Session()
        self.retries = 3
        self.timeout = 10.0

    def make_request(self, method: str, url: str, params: Dict[str, Any] = None) -> Dict:
        """
        Makes API requests with retries and handles responses.
        Args:
            method: HTTP method (GET, POST)
            url: API endpoint URL
            params: Optional parameters for the request
        Returns:
            Parsed JSON response from the API
        Raises:
            RequestException if all retries fail
        """
        try:
            max_retries = self.retries
            for attempt in range(max_retries):
                response = self.session.request(
                    method,
                    url,
                    params=params,
                    timeout=self.timeout,
                    headers={'Authorization': f'Bearer {self.config.get("api_key")}'}
                )
                
                if response.status_code == 200:
                    return response