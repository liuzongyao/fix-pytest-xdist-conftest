import requests, json, random

proxy = {
    "http": "http://alauda:Tnriw2z267geivn5aLvk@139.186.17.154:52975",
    "https": "http://alauda:Tnriw2z267geivn5aLvk@139.186.17.154:52975"
}

headers = {"Content-Type": "application/json",
           "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY3YWNmNjZlZDI2NmQwOWQ2MGU1MjYzMjNlYjdmZWZmMDFhNTI0NWIifQ.eyJpc3MiOiJodHRwczovL3JlY292ZXJ5LmFsYXVkYS5jbi9kZXgiLCJzdWIiOiJDaVF3T0dFNE5qZzBZaTFrWWpnNExUUmlOek10T1RCaE9TMHpZMlF4TmpZeFpqVTBOallTQld4dlkyRnMiLCJhdWQiOiJhbGF1ZGEtYXV0aCIsImV4cCI6MTYwMzg4MDMyNSwiaWF0IjoxNjAzNzkzOTI1LCJub25jZSI6ImFsYXVkYS1jb25zb2xlIiwiYXRfaGFzaCI6IjRuZjVwWXVxRDNseWdydmpuMmFEYVEiLCJlbWFpbCI6ImFkbWluQGNwYWFzLmlvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJhZG1pbiIsImV4dCI6eyJpc19hZG1pbiI6dHJ1ZSwiY29ubl9pZCI6ImxvY2FsIn19.K6ErgIPaK46m6nSubcXqh8B1P46rUiKsyVG6kGll0mLMHMtUszS6auSzzPvJ8sJS_dFQAnyQMItfZ0D6yKWDfa2CBfrtn7qs_nm7s-5MVT_Ot262bRxrKIKux5vCUIbXU0X0Etd7cF3EyXSFzK1veOPNNk-mWvhWSrSk8s1VTXuNiaPeWMCGtlzhN_sDXKVfKaeEr_TRfvGKrGGVR8ErR7Nzfmogl94jlYjq9G19QJRUEuse3kAJyYYt29ABLiXDrwJOVO65Z3__nlNCtnPQo9NxpNhKSOGxXQ0UK4QUIhzvutQwV5Gz-nrsA7I8JuR6pk6hLw-J6lyzXXsq8AOD1g"}
name = str(random.randint(1, 10))
value = {"metadata": {"name": name,
                      "namespace": "devops"}, "type": "kubernetes.io/basic-auth",
         "stringData": {"username": "demo", "password": "demo"}}
data = json.dumps(value)
print(type(data))
url_json = 'https://recovery.alauda.cn/devops/api/v1/secret/devops'

r_json = requests.post(url_json, json=value, headers=headers, proxies=proxy, verify=False)
print(r_json)
print(r_json.text)
print(r_json.content)
