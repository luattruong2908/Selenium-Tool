import requests

def add_gift(sessionId, code, srt, cookies):
    url = "https://pay.ebay.com/rxo/ajax?action=addIncentive"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://pay.ebay.com",
        "Connection": "keep-alive",
        "Referer": f"https://pay.ebay.com/rxo?action=view&sessionid={sessionId}",
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

def change_address(addressID, sessionId): 

    url = "https://pay.ebay.com/rxo/ajax?action=changeAddress"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://pay.ebay.com",
        "Connection": "keep-alive",
        "Referer": f"https://pay.ebay.com/rxo?action=view&sessionid={sessionId}",
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
    
def edit_address(addressID, sessionId, name):

    url = "https://pay.ebay.com/rxo/ajax?action=editAddress"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://pay.ebay.com",
        "Connection": "keep-alive",
        "Referer": f"https://pay.ebay.com/rxo?action=view&sessionid={sessionId}",
        "Cookie": cookies
    }

    data = {
        "addressId": addressID,
        "addressLine1": "4430 Cornwall St",
        "addressLine2": "123 123",
        "addressType": "SHIPPING",
        "city": "West Linn",
        "country": "US",
        "disableValidation": "true",
        "firstName": name,
        "lastName": "Luat",
        "makePrimary": "false",
        "pageType": "ryp",
        "phoneCountryCode": "US",
        "phoneNumber": "5033725964",
        "postalCode": "97068",
        "sessionid": sessionId,
        "srt": srt,
        "stateOrProvince": "OR"
    }


    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return(response.json())
    else:
        return(f"Lỗi {response.status_code}: {response.text}")

sessionId = "2081183979019"
code_1 = "IGC_AQAGAAAAQGbJGvy/K+sQxh6yMsSjbOTnSa/WFyJdFztvcAjjssMhZh1tjzx8OcM2wfbvPechiQ7E6+IXXfNU/9LHc/0lQLI="
code_2 = "IGC_AQAGAAAAQGG9uYarh4a0xGWRwRkX1npikisMfNDY+oC2KTAasDsO3tJvUMfkeemSxmwLzTBK8Vta+SdQnBj3Zwbwe3mzMvY="
addressID_1 = "10002064413819"
addressID_2 = "10002784527843"
addressID_3 = "10002784635555"
srt = "01000800000050c315d02af84d0062786207a7281acae635e83c36d581db26d2210399078710eb53a3e944b82f3f14cf32467885f258d36ff3fa67605c7eaf266f73009a9b1b85ff1a58e6fe5dde0cbd9196d48c5aa78f"
cookies = "dp1=bu1p/YXJjdW5fNTc*69183ee2^kms/in69183ee2^pbf/%230000e000e0000001808200000067370b62^u1f/Arynn69183ee2^expt/0001699531034536663d62da^mpc/0%7C067370b62^bl/USen-US69183ee2^; nonsession=BAQAAAYpI47hYAAaAAAQACGciQYlhcmN1bl81NwAQAAhnNwtiYXJjdW5fNTcAMwAOZzcLYjkyMDI1LTU3MTYsVVNBAEAACGc3C2JhcmN1bl81NwCcADhnNwtiblkrc0haMlByQm1kajZ3Vm5ZK3NFWjJQckEyZGo2TUFrSUdqQVplQ3BBV2RqNng5blkrc2VRPT0AnQAIZzcLYjAwMDAwMDAxAMoAIGkYPuJkNTAwZGU3NDE4YTBhYzZiYWVjZDNiZjVmZmZlMjlhOADLAANlVd7qMTQ2AWQAB2kYPuIjMDAwMDhhHtMiYTKiRyaGCmP6pw3nlM2h9i8*; __deba=IWCXPXmzCBYM8nurQymykn8zTh_DmbTR_2Vf1OlhtROUWxcU5S73729uBglIZOdCDlr9sv2cwsrcm1WMFfdDdIhMuWPDTfNNx5GuZV9OGzsVe1FPLWf-wuMbvXwNK6rpthWy-7QaHtAUb45qmKd0Ng==; __uzma=53d26523-a754-4def-8e3c-dff88816e8e0; __uzmb=1695790722; __uzmc=62026304355935; __uzmd=1700124642; __uzme=2735; __uzmf=7f6000799e3190-3d4d-4cde-b1f6-a6e3a3fdafd116957907222894333919790-b167f874f977718f3043; __ssds=2; __ssuzjsr2=a9be0cd8e; __gads=ID=43a41ab9cd08fab0:T=1696994357:RT=1699345931:S=ALNI_MY1j53FOXdGaGUn5CgnmraPg-A-EQ; __gpi=UID=00000a17b71d1038:T=1696994357:RT=1699345931:S=ALNI_MYb6x_q6GZvfk0djGRikOPeGEYSEg; QuantumMetricUserID=cb572514b2d8ed2f414eb50a70192f12; shs=BAQAAAYuxYOBRAAaAAVUAD2ciQYkyMTgyMDM1Nzc5MDA4LDLe/kQFTSoiOaJL2d0PteGcbQ1yKw**; ns1=BAQAAAYpI47hYAAaAAKUAGmc3C2IyNTY5ODAzOTI5LzA7MjQwMzI5NzA1OS8wOwDYAFNnNwtiYzY5fDYwMV4xNjk3MzAwNjExMDQ3Xl4xXjN8Mnw1fDR8N3wxMHw0Mnw0M3wxMV5eXjReM14xMl4xMl4yXjFeMV4wXjFeMF4xXjY0NDI0NTkwNzWSauSLxUOaqCdnMSIxj7KL9axy5A**; forterToken=2ab9d61854714c349f29f88b41562f11_1700124634262_5550_UDF43-m4_15ck; cid=0ilfQ8mx549EVZzL%231513962630; ak_bmsc=A3C1B2C835180CA6DB7EFAD91B4636ED~000000000000000000000000000000~YAAQHg/QF8IDJbGLAQAAp1Xv1hUvQv9RyTcHTFhEIzE4L/gtqSac1WWZQJCGCU/eAzvIVQVGGqUad8oUb/FiEZ1FM3s+aWCZYyW7sF+8VObWYjokfRK5v1MJr6qPQpxJgAv39cLm5p30V4GeCAszXSZESHlRVxbWZN2K9+4swn8Gvb4imoIeEdCgQHRytOycidS9E82SqMPhXqR5zLBzuk4PFhw64gGgVc/iq/fA8ycWqWhs3RWRfpt8CfGMejTnNcJy28YA5vbnSpwOmJS8FgEBGbL6Ja+9nv1dFJ62tKSj+XmZ8dP77VNV4a6L9vOhz4deerWsf26hfmppbfI3jy6E0Yj7jCyPr/BMJ/B05+d0bM/28dyH/da2Mw7JWelqeXDgfl3u4w==; bm_sv=18EC9E9AE62E2644B88950D6ED35EA1D~YAAQGqosF4sgrc2LAQAAnlFT1xXWNcZGLGaee3qwN046p9mmDtTtpPZnR6U+kepFhB8n9jv8BG3vclq24pJ2seH+WGfdnT3r6U8MConWfTLgwD9Pt/kPycQ++lLAbV7VQQ9VA0YfNkuQvHio5HYIuJths60p+hHPhowAsdkkUnbiiQ9UTHQoazu/DTsjhDUsq1wHlFeYrJE1qndUknmrHLCjEdhR7z1ixcCJQfz/GBWTyT4Y9/PES5uaFsIBmBmZ~1; s=CgAD4ACBlVyldZDUwMGRlNzQxOGEwYWM2YmFlY2QzYmY1ZmZmZTI5YTjvbQlG; ebay=%5Ejs%3D1%5Esbf%3D%23000000%5Epsi%3DAUymm%2Bjw*%5E; QuantumMetricSessionID=db47c907dc98d1589a5858eab8d53cd4; ftr_blst_1h=1700123754061; ds2=sotr/b8!A2zzzzzzz^"

#print(edit_address("10002783106179", sessionId, "Truong"))  
#print(add_gift(sessionId, code))

#IGC_AQAGAAAAQGbJGvy/K+sQxh6yMsSjbOTnSa/WFyJdFztvcAjjssMhZh1tjzx8OcM2wfbvPechiQ7E6+IXXfNU/9LHc/0lQLI=