import requests


def unexpected(host, port, **kwargs):
    this_dict = {}
    tut = requests.get(f"http://{host}:{port}").json()
    for i in kwargs:
        if kwargs[i] != tut[i]:
            this_dict[i] = kwargs[i]
    return this_dict