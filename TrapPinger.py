import requests
import time
from statistics import mean
from colorama import *
from art import *

init()
print(Fore.RED + '')
tprint("Trap",font="block",chr_ignore=True)
print('--------------------- >> lol << ---------------------')

def ping_website(url, num_pings):
    """
    Ping a website multiple times and return statistics.

    :param url: URL of the website to ping
    :param num_pings: Number of times to ping the website
    :return: Dictionary with statistics (status codes, response times, and site status)
    """
    response_times = []
    status_codes = []
    errors = []

    for i in range(num_pings):
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()

            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            response_times.append(response_time)
            status_codes.append(response.status_code)

            print(f"Ping {i + 1}: Status Code {response.status_code}, Response Time {response_time:.2f} ms")

        except requests.RequestException as e:
            # Handle request exceptions
            response_times.append(None)
            status_codes.append(None)
            errors.append(str(e))
            print(f"Ping {i + 1}: Failed with error {e}")

    # Calculate statistics
    successful_responses = [rt for rt in response_times if rt is not None]
    stats = {
        "url": url,
        "pings": num_pings,
        "successful_pings": len(successful_responses),
        "failed_pings": num_pings - len(successful_responses),
        "min_response_time_ms": min(successful_responses, default=None),
        "max_response_time_ms": max(successful_responses, default=None),
        "average_response_time_ms": mean(successful_responses) if successful_responses else None,
        "status_codes": status_codes,
        "errors": errors
    }

    return stats

def main():
    url = input("Enter the URL to ping (e.g., https://www.example.com): ")
    num_pings = int(input("Enter the number of times to ping: "))
    result = ping_website(url, num_pings)
    
    print("\nSummary:")
    if result["successful_pings"] > 0:
        print(f"Total Pings: {result['pings']}")
        print(f"Successful Pings: {result['successful_pings']}")
        print(f"Failed Pings: {result['failed_pings']}")
        print(f"Min Response Time: {result['min_response_time_ms']:.2f} ms")
        print(f"Max Response Time: {result['max_response_time_ms']:.2f} ms")
        print(f"Average Response Time: {result['average_response_time_ms']:.2f} ms")
        print(f"Status Codes: {result['status_codes']}")
    else:
        print(f"All pings failed with errors: {result['errors']}")

if __name__ == "__main__":
    main()

    
