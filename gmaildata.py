from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("email.address1711@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
driver.implicitly_wait(6)
driver.find_element_by_name("password").send_keys("Super@123")
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
driver.implicitly_wait(6)

comp_ose= driver.find_element_by_class_name('z0').click()#compose
driver.implicitly_wait(4)

Address= driver.find_element_by_name("to").send_keys("email.address1711@gmail.com")#to address
driver.implicitly_wait(4)

subject_element= driver.find_element_by_name("subjectbox").send_keys('Test with selenium')#subject
driver.implicitly_wait(4)

message=driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("hiiii!!!!! welcome jenkins")#message
driver.implicitly_wait(4)

driver.find_element_by_class_name('dC').click()#sending message
#driver.implicitly_wait(30)
#driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a").click()
#driver.find_element_by_css_selector("a[aria-label='Google Account: email address1']").click()
#driver.implicitly_wait(10)
#driver.find_element_by_xpath("//*[@id='gb_71']").click()




