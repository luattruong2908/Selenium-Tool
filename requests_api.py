#This code is in testing for new feature

import requests

def add_gift(sessionId, code, srt, cookies):
    url = "https://pay.ebay.com/rxo/ajax?action=addIncentive"

    headers = {
        # "authority": "pay.ebay.com",
        # "accept": "application/json, text/plain, */*",
        # "accept-language": "en-US,en;q=0.9",
        # "content-type": "application/json",
        # "origin": "https://pay.ebay.com",
        # "referer": "https://pay.ebay.com/rxo?action=view&sessionid=2110043308011",
        # "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        # "sec-ch-ua-full-version": "118.0.0.0",
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-model": '""',
        # "sec-ch-ua-platform": '"Windows"',
        # "sec-ch-ua-platform-version": "10.0.0",
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Cookie": cookies
    }

    data = {
        "redemptionCode": code,
        "sessionid": sessionId,
        "srt": srt,
        "pageType": "ryp"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return(response.json())
    else:
        return(f"Lỗi {response.status_code}: {response.text}")

def change_address(addressID, sessionId, cookies): 

    url = "https://pay.ebay.com/rxo/ajax?action=changeAddress"

    headers = {
        "authority": "pay.ebay.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://pay.ebay.com",
        "referer": "https://pay.ebay.com/rxo?action=view&sessionid=2110043308011",
        "sec-ch-ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        "sec-ch-ua-full-version": "118.0.0.0",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": "10.0.0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Cookie": cookies
    }

    data = {
        "addressId": addressID,
        "addressType": "SHIPPING",
        "pageType": "ryp",
        "sessionid": sessionId,
        "srt": srt
    }


    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return(response.json())
    else:
        return(f"Lỗi {response.status_code}: {response.text}")
    

sessionId = "2119341421011"
code = "IGC_AQAGAAAAQP+rpVKOPG2wCBlKQ1h3MnLDJ6o4B4erV7b0IUaNbayM0fGhXs+gsdlsEHnankFtd1m6JLCRrXSYyu7Kr0boB/Q="
addressID = "10002833295372"
srt = "01000900000050547ba20a11507b136b3d7393bea33a10e9aaccdc815fde2d7ec2eaaee2964b0f0cad53d921699ad41f1202ea1e2baa0b4597529af6e55f13bd9aa761971fbdeaaf908e592f5600a1dcf4e38b79d6876b"
cookies = "BAQAAAYxL36hOAAWAAAEAB2WPo31QZW5raml2AAMAAWWPpZ4wAAwACmWPpZ4yNTk0NjQxMjMxABEADWWOVsUwMDAwMHBlay01NTUzAD0ACGWPpZ5wZWstNTU1MwCoAAFlj6N1MQDuABhlj6WeMAZodHRwczovL3d3dy5lYmF5LmNvbS8HAPgAIGWPpZ5hMTUzYjYwZjE4YzBhY2YzOTZkN2UxYzlmZmYxNmVmYgFlAAJlj6WeIzIgdNOpioTvaPAN2lCTULpUiaEEsg**"

print(add_gift(sessionId, code, srt, cookies))
#IGC_AQAGAAAAQP+rpVKOPG2wCBlKQ1h3MnLDJ6o4B4erV7b0IUaNbayM0fGhXs+gsdlsEHnankFtd1m6JLCRrXSYyu7Kr0boB/Q=



# def edit_address(addressID, sessionId, name):

#     url = "https://pay.ebay.com/rxo/ajax?action=editAddress"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0",
#         "Accept": "application/json, text/plain, */*",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Content-Type": "application/json;charset=utf-8",
#         "Origin": "https://pay.ebay.com",
#         "Connection": "keep-alive",
#         "Referer": f"https://pay.ebay.com/rxo?action=view&sessionid={sessionId}",
#         "Cookie": cookies
#     }

#     data = {
#         "addressId": addressID,
#         "addressLine1": "4430 Cornwall St",
#         "addressLine2": "123 123",
#         "addressType": "SHIPPING",
#         "city": "West Linn",
#         "country": "US",
#         "disableValidation": "true",
#         "firstName": name,
#         "lastName": "Luat",
#         "makePrimary": "false",
#         "pageType": "ryp",
#         "phoneCountryCode": "US",
#         "phoneNumber": "5033725964",
#         "postalCode": "97068",
#         "sessionid": sessionId,
#         "srt": srt,
#         "stateOrProvince": "OR"
#     }


#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code == 200:
#         return(response.json())
#     else:
#         return(f"Lỗi {response.status_code}: {response.text}")