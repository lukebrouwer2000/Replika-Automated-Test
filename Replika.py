# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

globeList = []
pass_number = 0
total_test = 8

#YOUR EMAIL AND PASSWORD GO HERE
email = ""
password = ""

class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    # Poor Method for getting all Messages out of Selenium Window...
    def GetMessages(self,  messages=[]):
        try:
            cid = "ChatMessagesList__ChatMessagesListInner-sc-1ajwmer-1"
            divs = self.driver.find_element_by_class_name(cid)
            divs = divs.find_elements_by_tag_name("div")
            for x in divs:
                spans = x.find_elements_by_tag_name("span")
                for x in spans:
                    message = x.get_attribute('innerHTML')
                    if not message in messages and not "<span>" in message:
                        messages.append(message)
            return messages
        except:
            pass

    def GetLastMessage(self, messages=[]):
      try:
        return messages[len(messages) - 1]
      except:
        pass

    # Gets TheLastMessage out of Array messages
    def GetLastMessage(self, messages=[]):
        try:
            return messages[len(messages) - 1]
        except:
            pass

    def test_test1(self):

        self.driver.get("https://my.replika.com/login")
        self.driver.set_window_size(1200, 900)
        self.driver.find_element(By.ID, "emailOrPhone").send_keys(email)
        self.driver.find_element(By.ID, "emailOrPhone").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.ID, "login-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".SolidButton-k70ct8-0").click()
        time.sleep(5)

        self.driver.execute_script("window.scrollTo(0,0)")

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Hello")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Thanks, how are you?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("What are you doing right now?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Nothing as interesting as that lol. What music are you listening to?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Who is the president of the United States?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("¿Cual es la capital de Paraguay?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("was ist die hauptstadt von Deutschland?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("My favorite color is Red.")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("What is My favorite color?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)

        time.sleep(8)
        
        # Domain / Service Capability Testing
        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Tell me who the main character of Halo 2 is.")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Do you know who Link is?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Who is Link?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("What is Attack on Titan?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Tell me about Lilo and Stitch.")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Tell me what you know about the Halo 3 story?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Tell me about Halo. What is it?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Who is the Master Chief from Halo 2?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Tell me the story of Halo 2.")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)

        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Hello can you do mathematics for me?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)
        
        self.driver.find_element(By.ID, "send-message-textarea").send_keys("Okay, what is the square root of 64?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)
        
        self.driver.find_element(By.ID, "send-message-textarea").send_keys("What is the sum of 12 + 16?")
        self.driver.find_element(By.ID, "send-message-textarea").send_keys(Keys.ENTER)
        
        time.sleep(8)
        

        chatlist = self.GetMessages(globeList)
        response = self.GetLastMessage(chatlist)

        print("\n\n\n\n" + response)
