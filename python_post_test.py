import requests

f = open(".telent_auth", 'r')
auth = f.readlines()
f.close()
  
auth = [l.strip('\n\r') for l in auth]

asset_id = 17
start_date  ="2019-10-15 00:00"
end_date  ="2019-10-29 00:00"

header = {"X-RequestVerificationToken":auth[0],"Username": auth[1]}

request_body = {
  "assetId":asset_id,
  "startDate":start_date,
  "endDate":end_date
}

r = requests.post(url = "https://acm.telent.com:8443/api/Readings/GetReadings",
headers = header,
data=request_body
)

r.json()['sensors'][0]
