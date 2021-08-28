import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip', help="the IP of the key light")
parser.add_argument('-p', '--power', help="toggle power")
parser.add_argument('-t', '--temp', help="the light temperature: 2900 to 7000")
parser.add_argument('-b', '--brightness', help="the brightness level: 3 to 100")

args = parser.parse_args()

def get_state():
    response = requests.get(f"http://{args.ip}:9123/elgato/lights")
    return response.json()

def set_state(state):
    response = requests.put(f"http://{args.ip}:9123/elgato/lights", data=json.dumps(state))

def main():
    state = get_state()
    if args.brightness and (args.brightness in range(3, 100)):
        state["lights"][0]["brightness"] = args.brightness
    if args.temp and (args.temp in range(2900, 7000)):
        state["lights"][0]["temperature"] = args.temp
    if args.power:
        pwr = state["lights"][0]["on"]
        if pwr == 0:
            state["lights"][0]["on"] = 1
        else:
            state["lights"][0]["on"] = 0

    set_state(state)

if __name__ == '__main__':
    main()
