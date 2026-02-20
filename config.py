import os

class Configuration:
    """
    A singleton class to manage configuration settings for the loan application system.
    Uses environment variables for sensitive information and defaults for others.
    """

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        """
        Loads configuration from environment variables and sets default values.
        """
        self.api_key = os.getenv('FIN_API_KEY', 'default_key')
        self.max_loan_amount = float(os.getenv('MAX_LOAN_AMOUNT', 10000))
        self.min_credit_score = int(os.getenv('MIN_CREDIT_SCORE', 650))
        self.financial_api_url = os.getenv('FINANCIAL_API_URL', 'https://api.example.com')
        self.check_interval = int(os.getenv('CHECK_INTERVAL', 3600)) # in seconds

    def get(self, key):
        """
        Returns the value of a configuration parameter.
        """
        if key == 'api_key':
            return self.api_key
        elif key == 'max_loan_amount':
            return self.max_loan_amount
        elif key == 'min_credit_score':
            return self.min_credit_score
        elif key == 'financial_api_url':
            return self.financial_api_url
        elif key == 'check_interval':
            return self.check_interval
        else:
            raise KeyError(f"Configuration key {key} not found.")