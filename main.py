import time
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import json
import datetime
import logging


# Membuat logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Membuat handler untuk file log
handler = logging.FileHandler('log.txt')
handler.setLevel(logging.DEBUG)

# Membuat formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Menambahkan handler ke logger
logger.addHandler(handler)


# create session
def start():
    # Catat waktu mulai
    start_time = time.time()

    session = requests.Session()
    domain = "id2.bukanvvip.my.id:8000"
    allUsers = getAllUsers("example.txt")
    usernames = allUsers[0]
    expires = allUsers[1]
    uids = allUsers[2]
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhc2VwIiwiYWNjZXNzIjoic3VkbyIsImV4cCI6MTY4NjkyMzAxMH0.I4gbpsQw9Rnu99oKPcQpTX1XrBx4jM_qqtMrOnb-xCw"
    # token = getToken(domain, session)
    for i in range(len(usernames)):
        username = usernames[i]
        uid = uids[i]
        expire = expires[i]
        try:
            pushUser(domain, session, username, uid, expire, token)
        except Exception as ex:
            logger.error("Terjadi kesalahan di user %s: %s", (username, ex))
        else:
            # Menulis pesan success ke dalam file log
            logger.info("Success add user %s", username)
    print("lihat log di log.txt")
    end_time = time.time()
    # Hitung waktu yang dibutuhkan
    elapsed_time = end_time - start_time

    # Cetak waktu yang dibutuhkan
    print("Waktu yang dibutuhkan:", elapsed_time, "detik")


def getAllUsers(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    username = []
    expire = []
    uid = []

    for line in lines:
        tSplit = line.split()
        if tSplit[1] != "NEVER":
            username.append(tSplit[0])
            expire.append(tSplit[1])
            uid.append(tSplit[3])
        else:
            username.append(tSplit[0])
            expire.append(tSplit[1])
            uid.append(tSplit[2])
    
    return [username,expire,uid]


def toUnixTime(date):
    "date: 2023-07-08"
    date_string = date + " 23:59:59"
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    unix_time = int(date_obj.timestamp())
    return unix_time


def getToken(domain, session):
    urlLogin = 'https://' + domain + '/api/admin/token'
    
    payload = {
        'username': '',
        'password': ''
    }

    # Buat encoder multipart
    encoder = MultipartEncoder(fields=payload)

    # Dapatkan header Content-Type dan WebKitFormBoundary dari encoder
    content_type = encoder.content_type
    webkit_form_boundary = encoder.boundary

    # Lakukan permintaan POST dengan encoder multipart
    response = session.post(urlLogin, data=encoder, headers={'Content-Type': content_type})

    # Parsing response dari format JSON menjadi objek Python
    response_obj = json.loads(response.text)

    # Mengambil access_token dari objek response
    access_token = response_obj['access_token']
    # access_token = 123
    return access_token

def pushUser(domain, session, username, password, expire, token):
    "Expire harus berbentuk 2023-07-18"
    if expire == "NEVER":
        expire = 0
    else:
        expire = toUnixTime(expire)
    urlCreate = "https://" + domain + "/api/user"
    #
    payload = {
    'username': f'{username}',
    'proxies': {
        'trojan': {
            'password': f'{password}',
            'flow': ''
        }
    },
    'data_limit': 107374182400,
    'expire': expire,
    'data_limit_reset_strategy': 'day',
    'status': 'active',
    'inbounds': {
        'trojan': [
            'TROJAN_FALLBACK_INBOUND',
            'TROJAN_WS_BUKANVVIP_INBOUND',
            'TROJAN_WS_INBOUND'
        ],
        'vless': [
            'VLESS_TCP_INBOUND',
            'VLESS_WS_INBOUND'
        ],
        'vmess': [
            'VMESS_TCP_INBOUND',
            'VMESS_WS_INBOUND',
            'VMESS_WS_WORRYFREE_INBOUND'
        ]
    }}
    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json',
    'sec-ch-ua': '\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'cookie': 'i18next=en-US',
    'Referer': 'https://atha.bukanvvip.my.id:8000/dashboard/',
    'Referrer-Policy': 'strict-origin-when-cross-origin'
    }
    json_payload = json.dumps(payload)
    session.post(urlCreate, headers=headers, data=json_payload)
    # print("ini hasil respon")
    # print(response.text)
    # print(headers)

if __name__ == '__main__':
    start()
