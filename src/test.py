from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote( command_executor='http://hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME )

driver.get("https://www.google.com?q=mock")
