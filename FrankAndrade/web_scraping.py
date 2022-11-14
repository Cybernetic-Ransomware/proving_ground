from datetime import datetime
import os
# import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd


# application_path = os.path.dirname(sys.executable)  # does not work well on venvs
application_path = os.path.dirname(os.path.abspath(__file__))
current_time = datetime.now()
current_time_text = current_time.strftime("%Y-%m-%d_%H-%M")


website = r'https://wspieram.to/'
path = r'H:\PycharmProjects\Selenium\web_drivers\chromedriver'

# to avoid opening browser window
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)


containters = driver.find_elements(by='xpath', value='//a[@class="PrjBox crowdfunding"]')

titles = []
categoryies_and_locations = []
descriptions = []
hyperlinks = []


for container in containters:
    title = container.find_element(by='xpath', value='./div[@class="txt"]/h3').text
    titles.append(title)

    category_and_location = container.find_element(by='xpath', value='./div[@class="txt"]/span').text
    categoryies_and_locations.append(category_and_location)

    description = container.find_element(by='xpath', value='./div[@class="txt"]/div').text
    descriptions.append(description)

    hyperlink = container.get_attribute('href')
    hyperlinks.append(hyperlink)


my_dict = {'titles': titles, 'categoryies_and_locations': categoryies_and_locations,
           'descriptions': descriptions, 'hyperlinks': hyperlinks}
df_headlines = pd.DataFrame(my_dict)


#  use os to unificatate difrent roots on Windows, macOS and Linux
file_name = f'{current_time_text}_promoted_foundings.csv'
route_to_save = os.path.join(application_path, file_name)

df_headlines.to_csv(route_to_save)


driver.quit()
