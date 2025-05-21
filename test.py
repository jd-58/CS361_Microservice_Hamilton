import requests

def test_microservice():
    # URL of the microservice
    url = "http://127.0.0.1:5000/get_affirmation"

    # Example mood to test
    test_payload = {"mood": "happy"}

    try:
        # Print the data being sent
        print("Sending data:", test_payload)

        # Make a POST request to the microservice
        response = requests.post(url, json=test_payload)

        # Print the raw response data
        print("Raw response data:", response.text)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print("Affirmation received:", data.get("affirmation"))
        elif response.status_code == 400:
            error_data = response.json()
            print("Error received:", error_data.get("error"))
        else:
            print("Unexpected response code:", response.status_code)
    except Exception as e:
        print("An error occurred while making the request:", str(e))


if __name__ == "__main__":
    test_microservice()