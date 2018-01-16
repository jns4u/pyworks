import http.client

conn = http.client.HTTPSConnection("nodejs.org")

headers = {
    'cache-control': "no-cache",
    'token': "JNS-e2f52acf-b226-b50c-009f-4f7acd6358b5"
    }

conn.request("GET", "/dist/latest-v8.x/docs/api/index.json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
