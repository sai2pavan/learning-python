import sys
import requests
import os


def main():
    # Validate command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Get API key from environment variable
    api_key = os.getenv("COINCAP_API_KEY")
    if not api_key:
        sys.exit("API key not found")

    url = "https://rest.coincap.io/v3/assets/bitcoin"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Request failed")

    total_cost = n * price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()

