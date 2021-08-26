import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip', help="the IP of the key light")

args = parser.parse_args()

def get_state():
    response = requests.get(f"http://{args.ip}:9123/elgato/lights")
    return response.json()["lights"][0]["on"]

def set_state(value):
    j = {"numberOfLights": 1,
          "lights": [
             {"on": value,
              "brightness": 18,
               "temperature": 288}
             ]
        }
    response = requests.put(f"http://{args.ip}:9123/elgato/lights", data=json.dumps(j))

def main():
    state = get_state()
    if state == 0:
        set_state(1)
    else:
        set_state(0)

if __name__ == '__main__':
    main()
