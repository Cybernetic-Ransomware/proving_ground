from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd


website = r'https://wspieram.to/'
path = r'H:\PycharmProjects\Selenium\web_drivers\chromedriver'

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
df_headlines.to_csv('headline.csv')


driver.quit()
