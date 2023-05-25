
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from random import choice
import string
import names
from random import randint
from selenium.webdriver import ActionChains
from captchaSolver import captchaSolver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys

def generate_username():
	if randint(1, 100) % 2 == 0:
		username = names.get_first_name()
	else:
		username = names.get_last_name()

	username += ''.join(str(randint(0, 9)) for i in range(3, 9))
	while len(username) > 19:
		username = username[:-1]
	return username

def generate_password():
	password = ''.join(choice(string.ascii_letters + string.digits) for i in
					   range(randint(10, 20)))
	return password


def launch_browser_to_reddit(driver):
	driver.maximize_window()
	driver.get("https://www.reddit.com/register/")

def launch_browser_to_needed_post(driver):
	driver.maximize_window()
	driver.get("https://www.reddit.com/r/Romania/comments/x4qkps/azi_a_ieșit_giurgiu_care_județ_va_fi_următorul/") #add needed url


def navigate_first_page(driver, email: str):
	email_box = driver.find_element(by=By.ID, value="regEmail")
	ActionChain = ActionChains(driver)
	ActionChain.move_to_element(email_box).click(
		email_box).send_keys(email).perform()

	driver.implicitly_wait(randint(2, 5))

	continue_button = driver.find_element(by=By.XPATH,
						value="/html/body/div[1]/main/div[1]/div/div[2]/form/fieldset[3]/button")
	ActionChain.move_to_element(continue_button).click(
		continue_button).perform()



def nagivate_second_page(username: str, password: str, driver):
	# print(driver.find_element(by=By.XPATH, value="/html/body").text)
	ActionChain = ActionChains(driver)
	username_box = driver.find_element(by=By.CSS_SELECTOR, value='#regUsername')
	# ActionChain.click(username_box).send_keys(username).perform()
	username_box.click()
	username_box.send_keys(username)

	driver.implicitly_wait(randint(2, 5))
	password_box = driver.find_element(by=By.CSS_SELECTOR, value='#regPassword')
	# field = driver.find_element(by=By.CSS_SELECTOR, value="#registerPasswordField")
	ActionChain.click(password_box).send_keys(password).perform()
	driver.implicitly_wait(randint(2, 5))

	captchaSolver(driver)

	driver.implicitly_wait(randint(2, 5))
	sign_up_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div[2]/div/div/div[3]/button")
	sign_up_box.click()


def create_reddit_account(email: str, username: str, password: str, driver):
	launch_browser_to_reddit(driver)
	navigate_first_page(driver, email)
	nagivate_second_page(username, password, driver)
	time.sleep(5)
	driver.delete_all_cookies()
	driver.close()


def logInRedditPost(username: str, password: str, driver):
	login_button = driver.find_element(by=By.XPATH,
									   value='//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]')
	login_button.click()
	driver.implicitly_wait(4)

	iframe = driver.find_element(by=By.CSS_SELECTOR,
								 value='#SHORTCUT_FOCUSABLE_DIV > div:nth-child(6) > div._1UtFUrE2ijAe5ba5uPgcfQ > div > iframe')
	driver.switch_to.frame(iframe)
	username_field = driver.find_element(by=By.CLASS_NAME,
										 value='AnimatedForm__textInput')
	username_field.click()
	username_field.send_keys(username)

	password_field = driver.find_element(by=By.XPATH,
										 value='//*[@id="loginPassword"]')
	password_field.click()
	password_field.send_keys(password)

	login_button_2 = driver.find_element(by=By.CSS_SELECTOR,
										 value='body > div > main > div.OnboardingStep.Onboarding__step.mode-auth > div > div.Step__content > form > fieldset:nth-child(8) > button')
	login_button_2.click()

	time.sleep(10)
	driver.quit()


def launchALl(emails: list, accounts: dict) -> dict:
	count = 0
	for email in emails:
		options = webdriver.ChromeOptions()
		options.add_argument("--incognito")
		options.add_argument('--disable-blink-features=AutomationControlled')
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_experimental_option('useAutomationExtension', False)
		driver = webdriver.Chrome(ChromeDriverManager().install(),
								  options=options)
		driver.execute_script(
			"Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		username = generate_username()
		password = generate_password()
		create_reddit_account(email, username, password, driver)
		accounts[username] = password
		count += 1

	return accounts
