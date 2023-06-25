from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def get_data(url) -> list:
    browser_options = ChromeOptions()
    #browser_options.headless = True
    
    driver = Chrome(options=browser_options)
    driver.get(url)
    
    element = driver.find_element(By.ID, "topgranos")
    driver.execute_script("arguments[0].click();", element)
    sleep(10)

    element = driver.find_element(By.ID, "form-check-mobile00")
    #element = driver.find_element(By.XPATH,"//*[@id='form-check-mobile00']/div[1]")
    element.submit()
    #"//*[@id='form-check-mobile00']/div[1]"
    #driver.execute_script("arguments[0].click();", element)
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[@for='form-check-mobile00']"))).click()
    #driver.quit() 
    data = True 
    return data


def main():
    data = get_data("https://precio-alimentos.eltoque.com/")
    print(data)


if __name__ == '__main__':
    main()


   