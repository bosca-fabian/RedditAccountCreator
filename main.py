import os
import jsonpickle
from redditAccountLogic import launchALl
from VPNCountrySwitcher import switchRegionVPN
from emailGenerator import start_email_generator

def write_file(items):
    with open("accounts", 'w') as f:
        f.write(jsonpickle.dumps(items))


def __read_file(path: str):
    try:
        with open(path, 'r') as f:
            return jsonpickle.loads(f.read())

    except Exception as ex:
        print(ex)
        return {}


def main():
    emails = __read_file("emails")
    existing_accounts = __read_file("accounts")
    new_accounts = launchALl(emails, existing_accounts)
    write_file(new_accounts)


if __name__ == '__main__':
    main()
