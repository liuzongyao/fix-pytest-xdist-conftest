import json
import pytest
from filelock import FileLock
import requests
import random

proxy = {
    "http": "http://alauda:Tnriw2z267geivn5aLvk@139.186.17.154:52975",
    "https": "http://alauda:Tnriw2z267geivn5aLvk@139.186.17.154:52975"
}

headers = {"Content-Type": "application/json",
           "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZkYzQyYTk4MjIxNWM3MjNlYTk0MjJhZDIwYjBiNGNhMzViMTVhZWIifQ.eyJpc3MiOiJodHRwczovL2ludC5hbGF1ZGEuY24vZGV4Iiwic3ViIjoiQ2lRd09HRTROamcwWWkxa1lqZzRMVFJpTnpNdE9UQmhPUzB6WTJReE5qWXhaalUwTmpZU0JXeHZZMkZzIiwiYXVkIjoiYWxhdWRhLWF1dGgiLCJleHAiOjE2MDQwMjQ3MjIsImlhdCI6MTYwMzkzODMyMiwibm9uY2UiOiJhbGF1ZGEtY29uc29sZSIsImF0X2hhc2giOiJkMjRWY29BdFFTM19uN2J2d3lqMTVnIiwiZW1haWwiOiJhZG1pbkBjcGFhcy5pbyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiYWRtaW4iLCJleHQiOnsiaXNfYWRtaW4iOnRydWUsImNvbm5faWQiOiJsb2NhbCJ9fQ.N8BWsvCs6XNA-FfgNi0AX3zfO1Ay1dLTshKpdBMuSJzDQ3SvhR6KpwpGPvE4FTYB1gef7m0dIMBgteq3LMvr9A7zOjsrtB8eQE78YYiagUTWuqqgUWN28Itjapz6LONi2iaCMqIA2hmj5ky7GdHO8F-85DUWT8boTxo8mtue75yA-DTdQIf-2Dpl3dCTJ1rMqAxSvJ8nT4Cr5dzFVJGC9i5D3hBVLcRVFlD-R0FR8pluR78dRweR1WHFU-afGdyV8EUjYVIxoZdLnaAKr8BOw639ODQYRLwfLKghEn8czIgq0xV34dZYYTkcUQNzJUuP7GqJ-dKWgV8FZODc9VLZ1Q"}


@pytest.fixture(scope="session")
def start(tmp_path_factory, worker_id):
    # if worker_id == "master":
    #     # not executing in with multiple workers, just produce the data and let
    #     # pytest's fixture caching do its job
    #     produce_expensive_data()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    fn1 = root_tmp_dir / "data1.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = produce_expensive_data()
            produce_expensive_data1()
            fn.write_text(json.dumps(data))
    yield data
    with FileLock(str(fn1) + ".lock"):
        if fn1.is_file():
            json.loads(fn1.read_text())
        else:
            data1 = produce_expensive_data2()
            fn1.write_text(json.dumps(data1))


def produce_expensive_data():
    name1 = str(random.randint(1,10))

    value1 = {"metadata": {"name": name1,
                           "namespace": "devops"}, "type": "kubernetes.io/basic-auth",
              "stringData": {"username": "demo", "password": "demo"}}

    url_json = 'https://int.alauda.cn/devops/api/v1/secret/devops'

    requests.post(url_json, json=value1, headers=headers, proxies=proxy, verify=False)
    dict1 = {"name":"zhangsan"}
    return dict1

def produce_expensive_data1():
    name2 = str(random.randint(1,10))

    value1 = {"metadata": {"name": name2,
                           "namespace": "devops"}, "type": "kubernetes.io/basic-auth",
              "stringData": {"username": "demo", "password": "demo"}}

    url_json = 'https://int.alauda.cn/devops/api/v1/secret/devops'

    requests.post(url_json, json=value1, headers=headers, proxies=proxy, verify=False)


def produce_expensive_data2():
    name3 = str(random.randint(1, 10))

    value1 = {"metadata": {"name": name3,
                           "namespace": "devops"}, "type": "kubernetes.io/basic-auth",
              "stringData": {"username": "demo", "password": "demo"}}

    url_json = 'https://int.alauda.cn/devops/api/v1/secret/devops'

    requests.post(url_json, json=value1, headers=headers, proxies=proxy, verify=False)
    dict1 = {"name":"zhangsan"}
    return dict1
