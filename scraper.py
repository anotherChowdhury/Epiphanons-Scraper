from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json


def get_data(URL):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    browser.get(URL)
    try:
        picture_link = browser.find_element_by_css_selector(
            '.scaledImageFitWidth.img').get_attribute('src')
        # print(picture_link)
    except Exception as e:
        print(e)
    try:
        name = browser.find_element_by_css_selector(
            '.fwb.fcg').text.strip()
        profile_link = browser.find_element_by_css_selector(
            '.fwb.fcg a').get_attribute('href').split('?')[0].strip()
        # print(name)
        # print(profile_link)
    except Exception as e:
        print(e)
        if('&id=' in URL):
            profile_link = "https://www.facebook.com/profile.php/" + \
                URL.split("=")[-1].strip()
        else:
            profile_link = URL.split('post')[0].strip()
    try:
        post_text = browser.find_element_by_css_selector(
            'div[data-testid="post_message"]').text.strip()
        # print(post_text)
    except Exception as e:
        print(e)
    try:
        time_of_post = browser.find_element_by_css_selector(
            '.timestampContent').text.strip()
        print(time_of_post)
    except Exception as e:
        print(e)

    browser.quit()

    return ({
        "name": name,
        "date": time_of_post,
        "postLink": URL,
        "profileLink": profile_link,
        "text": post_text,
        "image": picture_link
    })

    # for object in respone_object:
    #     print(json.loads(object))
    # try:
    #     browser.find_element_by_css_selector('button[name="login"]').click()
    # except:
    #     browser.find_element_by_css_selector('input[value="Log In"]').click()
