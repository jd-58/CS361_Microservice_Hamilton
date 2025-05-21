# Affirmation Microservice

This microservice provides affirmations based on the mood sent in a POST request. Below are clear instructions for how to programmatically request and receive data from the microservice.

---

## How to Programmatically Request Data

To request data from the microservice, send a POST request to the `/get_affirmation` endpoint with a JSON payload containing the `mood` key. The `mood` value should be a string representing the user's mood (e.g., "happy", "sad", "anxious", or "angry"). The microservice will likely be running locally, or if on the web, at a certain url. The example call shows a URL for if you are running the microservice (and your app) locally.

### Example Request

Here is an example of how to programmatically send a request using Python:

```python
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
```

How to Programmatically Receive Data
The microservice will respond with JSON. If the mood is recognized, the response will include an affirmation. If the mood is not recognized, the response will include an error message.


Example Response Handling
Here is an example of how to handle the response programmatically using Python:

```python

def handle_response():
    # Example response from the microservice
    response = {
        "affirmation": "Glad to hear!"
    }

    # Check if the response contains an affirmation
    if "affirmation" in response:
        print("Affirmation received:", response["affirmation"])
    elif "error" in response:
        print("Error received:", response["error"])
    else:
        print("Unexpected response format:", response)
```

In this example, the mood "happy" is hard coded. In actual use, this will be dependent on user input.


+-------------------------+ HTTP POST +-----------------------------+ | Test Client | ---------------------------------> | Flask Microservice | | (test_microservice.py) | | (get_affirmation endpoint) | +-------------------------+ +-----------------------------+ | - url: str | | - affirmations: dict | | - test_payload: dict | | | | + test_microservice() | | + get_affirmation(): JSON | +-------------------------+ +-----------------------------+ | V +------------------------------+ | Affirmation Logic | +------------------------------+ | - Mood categories: [happy, | | sad, anxious, angry] | | - Random selection per mood | +------------------------------+
