# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests>=2.33.1",
# ]
# ///
import os
import requests

def main():
    print(f'Hello, {os.path.expanduser("~")} from helloworld!')
    resp = requests.get('https://peps.python.org/api/peps.json')
    data = resp.json()
    print(f'Request response was: \n\n{data["1"]}\n')


if __name__ == "__main__":
    main()
