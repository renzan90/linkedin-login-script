from selenium import webdriver
from getpass import getpass
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager

usr=input("Enter your username or email: ")
pwd=getpass("Enter your password: ")

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.linkedin.com/')

sign_in_btn= driver.find_element_by_class_name('nav__button-secondary').click()

username_box=driver.find_element_by_id('username')
username_box.send_keys(usr)

password_box=driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_btn=driver.find_element_by_class_name('login__form_action_container')
login_btn.submit()


