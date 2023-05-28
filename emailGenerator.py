import jsonpickle
import requests


def generate_email():
    # generates gmail account, returns email address
    url = "https://temp-gmail.p.rapidapi.com/get"

    querystring = {"domain": "gmail.com", "username": "random",
                   "server": "server-1", "type": "real"}

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "temp-gmail.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers,
                                params=querystring)
    json_response = response.json()
    gmail = json_response['items']['email']
    return gmail


def write_file(emails: list):
    with open("emails", 'w') as f:
        f.write(jsonpickle.dumps(emails))


def __read_file():
    try:
        with open("emails", 'r') as f:
            return jsonpickle.loads(f.read())

    except Exception:
        return {}


def start_email_generator():
    emails = __read_file()
    number_of_emails = int(input("Enter the amount of emails accounts you "
                                 "want: "))
    for i in range(number_of_emails):
        emails.append(generate_email())
    write_file(emails)
