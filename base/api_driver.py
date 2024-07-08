import requests
from urllib.parse import urlencode

class ApiDriver:
    def __init__(self, url):
        self.url = url

    def authAPI(self):
        payload = {
            'grant_type': 'client_credentials',
            'client_id': 'dc-aehwmq7yzmid7j9h5vdodggfi',
            'client_secret': 'TgIHt2zDNQGW3RyrxrZzLa;gE1amwiQQQXLO6iScmirWKgepFhm',
            'scope': 'READ_BILLING_CONTACTS READ_INVOICING_DETAILS LOAD_INVOICE_FILES READ_BILLING_CARD READ_OVERAGES READ_CONTRACT READ_PSOVERAGES_DATA WRITE_DRAFT_INVOICE READ_IRCASES_DATA',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        encoded_payload = urlencode(payload)

        response = requests.get(self.url, headers=headers, verify = False, data=encoded_payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
