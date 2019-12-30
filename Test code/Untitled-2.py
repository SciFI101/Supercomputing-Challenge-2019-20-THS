import http.client

conn = http.client.HTTPSConnection("priaid-symptom-checker-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "priaid-symptom-checker-v1.p.rapidapi.com",
    'x-rapidapi-key': "ac55215368mshb11971ef5ff14a0p1b5b6ejsn82f40ccda23c"
    }

conn.request("GET", "/body/locations?language=en-us", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))