import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip', help="the IP of the key light")

args = parser.parse_args()

def get_state():
    response = requests.get(f"http://{args.ip}:9123/elgato/lights")
    return response.json()

def set_state(state, value):
    state["lights"][0]["on"] = value
    response = requests.put(f"http://{args.ip}:9123/elgato/lights", data=json.dumps(state))

def main():
    state = get_state()
    current_value = state["lights"][0]["on"]
    if current_value == 0:
        set_state(state, 1)
    else:
        set_state(state, 0)

if __name__ == '__main__':
    main()
