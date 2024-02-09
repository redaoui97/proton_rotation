import subprocess
import time
import argparse
import requests

def rotate_ip():
    # Command to disconnect from ProtonVPN
    subprocess.run(["protonvpn-cli", "disconnect"])

    # Wait for a few seconds for disconnection
    time.sleep(2)

    # Command to connect to ProtonVPN
    subprocess.run(["protonvpn-cli", "connect", "-f"])  # "-f" flag for auto-connect

def run_command(command):
    # Run the provided command
    subprocess.run(command, shell=True)

def check_target_status(target_url):
    try:
        response = requests.get(target_url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking target status: {e}")
        return False

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Rotate IP address and execute command while checking target status")
    parser.add_argument("-c", "--command", required=True, help="Command to execute")
    parser.add_argument("-r", "--rotation-interval", type=int, default=5, help="Rotation interval in seconds (default: 5)")
    parser.add_argument("-u", "--target-url", required=True, help="Target URL or domain")
    args = parser.parse_args()

    try:
        while True:
            # Rotate IP
            rotate_ip()

            # Check target status
            if check_target_status(args.target_url):
                print("Target status: OK")

                # Run command
                run_command(args.command)

                # Wait for rotation interval
                time.sleep(args.rotation_interval)
            else:
                print("Target status is not 200. Waiting before retrying...")
                time.sleep(10)  # Wait for 10 seconds before retrying

    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()

