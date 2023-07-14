import json

import requests

def sendSmsOneContact(phone, message):
    phone_number = str(phone)
    if phone_number.startswith("998"):
        dt = {
            "messages": [
                {
                    "recipient": phone,
                    "message-id": "abc000000001",
                    "sms": {
                        "originator": "3700",
                        "content": {
                            "text": message
                        }
                    }
                }
            ]
        }

    # return requests.post(url="http://91.204.239.44/broker-api/send",
    #                    auth=('eramax', 'K7fv2tL5Z8'),
    #                    headers={'content-type': 'application/json'},
    #                    data=json.dumps(dt))
