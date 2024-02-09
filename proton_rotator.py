import subprocess
import time
import argparse
import requests

#protonvpn-cli is deprected but game is game
def rotate_ip():
    subprocess.run(["protonvpn-cli", "disconnect"])
    time.sleep(2)
    subprocess.run(["protonvpn-cli", "connect", "--random"])  # "-f" flag for auto-connect

def check_target_status(target_url):
    try:
        response = requests.get(target_url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Target down: {e}")
        return False

def proton_connect(username):
    subprocess.run(["protonvpn-cli", "login",  username])

def main():
    parser = argparse.ArgumentParser(description="protonvpn-cli ip rotation")
    parser.add_argument("-r", "--rotation-interval", type=int, default=5, help="Rotation interval in seconds (default: 5)")
    parser.add_argument("-u", "--target-url", required=True, help="Target URL or domain")
    parser.add_argument("-n", "--username", required=True, help="protonvpn username, visit 'https://protonvpn.com/' if you don't have an account")
    args = parser.parse_args()

    try:
        proton_connect(args.username)
        while True:
            rotate_ip()
            if check_target_status(args.target_url):
                print("Target status: OK")
                time.sleep(args.rotation_interval)
            else:
                print("Target doesn't respond. Waiting before retrying...")
                time.sleep(5)

    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()

