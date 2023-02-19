import time
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = "Dawid.lachowicz@pkp.ivu"
password = ""
train_number = "1400"
next_mounth = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://irena1.intercity.pl")
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_username"))).send_keys(login)
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "j_password"))).send_keys(password)
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button"))).click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "item--crew-on-trip"))).click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datepicker"))).click()
time.sleep(3)
for x in range(next_mounth):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@title="Następny"]'))).click()
    time.sleep(3)
month = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-month"))).text
year = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-datepicker-year"))).text
elements_days = driver.find_elements(by=By.XPATH, value= '//*[@data-handler="selectDay"]/a')
days=[day.text for day in elements_days]
print(days)
csv_elements = []
for day in days:
    # if day=="3":
    #     break
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "datepicker"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//*[@data-date="{day}"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text()="OK"]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tripnumber-input"))).clear()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tripnumber-input"))).send_keys(train_number)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search-button'))).click()
    time.sleep(3)
    elements_crew = driver.find_elements(by=By.CLASS_NAME, value='crew-value')
    for element_crew in elements_crew:
        try:
            list_crew = element_crew.text.split("\n")
            print(day)
            print([day,list_crew[1],list_crew[3],list_crew[5],list_crew[7],list_crew[9]])
            csv_elements.append([day,list_crew[1],list_crew[3],list_crew[5],list_crew[7],list_crew[9]])
        except:
            csv_elements.append([day,'ERROR','ERROR','ERROR','ERROR','ERROR'])

header = ['Dzien','Osoba', 'Telefon', 'Typ', 'Start', 'Stop']

with open(f'{train_number}_{month}_{year}.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for x in csv_elements:
        writer.writerow(x)

print(f'train_number')
print(f'{train_number}')
print(f'month')
print(f'{month}')
print(f'year')
print(f'{year}')



# path = 'file:///Users/tomaszstasiuk/Desktop/workspace/dawid/kalendarz.html'
# path = 'file:///Users/tomaszstasiuk/Desktop/workspace/dawid/output.html'
# driver.get(path)

    # days_xpath.append(f'//*[@data-date={day.text}]')
# print(days_xpath)


# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tripnumber-input"))).send_keys(train_number)

# calendar_elements = '//*[@data-handler="selectDay"]'
# time.sleep(3)
#
#
#
#
#
#
#
#
# time.sleep(100)



# xpath_login = '//*[@id=""]'
# xpath_password = '//*[@id="j_password"]'

#
# name = '//*[@class="crew-value"]//*[@title="Nazwa"]/span'
# phone = '//*[@class="crew-value"]//*[@title="Numer telefonu"]/a'
# type = '//*[@class="crew-value"]//*[@title="Typ załogi"]/span'
# start_location = '//*[@class="crew-value"]//*[@title="Lokalizacja początkowa i początkowa"]/span'
# end_location = '//*[@class="crew-value"]//*[@title="Koniec i cel"]/span'


# name = '//*[@title="Nazwa"]/span'
# phone = '//*[@title="Numer telefonu"]/a'
# type = '//*[@title="Typ załogi"]/span'
# start_location = '//*[@title="Lokalizacja początkowa i początkowa"]/span'
# end_location = '//*[@title="Koniec i cel"]/span'




# print(element_crew.find_element(by=By.XPATH, value= name).text)
# print(element_crew.find_element(by=By.XPATH, value= phone).text)
# print(element_crew.find_element(by=By.XPATH, value= type).text)
# print(element_crew.find_element(by=By.XPATH, value= start_location).text)
# print(element_crew.find_element(by=By.XPATH, value= end_location).text)











# driver.find_element(by=By.ID, value= 'j_username').send_keys(login)
# driver.find_element(by=By.ID, value= 'j_password').send_keys(password)
# driver.find_element(by=By.ID, value= 'login-button').click()
# driver.find_element(by=By.ID, value= 'item--crew-on-trip').click()


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="/Users/tomaszstasiuk/Desktop/workspace/dawid/chromedriver")


# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
