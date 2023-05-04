from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd



if __name__ == '__main__':

    URL = "https://workshops.aws/"

    path_to_driver = ChromeDriverManager().install()
    print(path_to_driver)
    driver = webdriver.Chrome(service=ChromeService(path_to_driver))
    driver.get(URL)
    aws_workshop_tags = driver.find_elements(By.TAG_NAME, value='aws-workshop-card')

    workshops = []

    for tag in aws_workshop_tags:

        headline = tag.find_elements(By.CLASS_NAME, 'mat-headline')
        # Sanity check for only 1 element in headline
        assert len(headline) == 1
        title = headline[0].text

        details = tag.find_elements(By.TAG_NAME, 'span')
        # Sanity check for only 5 elements in the details list
        assert len(details) == 5

        # Level
        level = details[0].text.split(':')[-1]

        # Categories
        categories = details[1].text.split(":")[-1].split(",")

        # Tags
        tags = details[2].text.split(":")[-1].split(",")

        # Time
        time = details[3].text

        workshops.append(
            {'title' : title, 'level': level, 'categories' : categories, 'tags': tags, 'time': time}
        )

    df = pd.DataFrame.from_dict(workshops)
    df.to_excel('workshops.xlsx', index=False)
