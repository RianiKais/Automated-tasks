!pip install --upgrade selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get("Your Url")

# Wait for the page to load completely
driver.implicitly_wait(10)

# Find the element to drag and drop using XPath
drag_element = driver.find_element_by_xpath("element label/ID")

# Find the drop target element using XPath
drop_target = driver.find_element_by_xpath(" element label/ID")

# Perform the drag and drop action using ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(drag_element, drop_target).perform()

# Close the browser window
driver.quit()
