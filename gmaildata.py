from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("email.address1711@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
driver.implicitly_wait(6)
driver.find_element_by_name("password").send_keys("Super@123")
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
driver.implicitly_wait(6)


