import requests, random, threading; from colorama import Fore



def main():
    tokens = open('tokens.txt', 'r').read().splitlines()
    token = random.choice(tokens)

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'connection': 'keep-alive',
        'content-length': '188',
        'content-type': 'application/json',
        'fingerprint': '',
        'gacid': '',
        'host': 'graphigo.prd.dlive.tv',
        'origin': 'https://dlive.tv',
        'referer': 'https://dlive.tv/',
        'sec-ch-ua': '\'Not_A Brand\';v=\'99\', \'Google Chrome\';v=\'109\', \'Chromium\';v=\'109\'',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\'Windows\'',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-dlive-mid': '',
        'x-dlive-mtype': 'web',
        'x-dlive-mversion': 'local'
    }

    json = {
      "operationName": "FollowUser",
      "variables": {
        "streamer": channel
      },
      "extensions": {
        "persistedQuery": {
          "version": 1,
          "sha256Hash": "daf146d77e754b6b5a7acd945ff005ae028b33feaa3c79e04e71505190003a5d"
        }
      }
    }

    r = requests.post('https://graphigo.prd.dlive.tv/',headers=headers, json=json)
    if 'FollowResponse' in r.text:
      print(f"{Fore.RESET}{Fore.GREEN}Followed")
    elif 'Require login' in r.text:
      print(f"{Fore.RESET}{Fore.RED}Token invalid")          


if __name__ == '__main__':
  channel = input("Enter channel name > ")
  threads = input("Threads > ")
  for _ in range(int(threads)):
    threading.Thread(target=main).start()
