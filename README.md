# RedditAccountCreator

Python program that makes use of different API's in order to create Reddit accounts. Selenium webdriver has been used to interact with Google Chromem to create Reddit accounts.<br/><br/>
The emails used for the accounts are brought in with the help of RapidAPI's Temp Gmail: https://rapidapi.com/mrsonj/api/temp-gmail and the passwords generated are random. The accounts details are then saved locally in a file.<br/><br/>
In order to proceed with the creation of the Reddit accounts, captchas are supposed to be solved. This thing is being done by calling 2captcha's API https://2captcha.com/2captcha-api which provides means to solved different types of captchas. The entire process and how it works is explained well on their website.
