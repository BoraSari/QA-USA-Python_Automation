import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers


class UrbanRoutesPage:
 ##Locators
        From_Field_Locator = (By.ID,"from")
        To_Field_Locator = (By.ID,"to")
        Card_Icon_Locator = (By.XPATH,"//img[@src='/static/media/card.411e0152.svg' and @alt='cash']")
        Add_Card_Icon_Locator = (By.XPATH,"//div[contains(text(),'Add card')]")
        Card_Number_Input_Field_Locator = (By.ID,"number")
        Cvv_Locator = (By.NAME,"code")
        Link_Card_Locator = (By.XPATH,"//button[@type='submit' and contains(text(),'Link')]")
        Taxi_Icon_Locator = (By.XPATH,"//img[@src='/static/media/taxi-active.b0be3054.svg']")
        Call_Taxi_Button_Locator = (By.XPATH,"//button[contains(text(),'Call a taxi')]")
        Phone_Field_Locator = (By.XPATH,"//div[contains(text(),'Phone number')]")
        Phone_Number_Field_Locator = (By.ID,"phone")
        Supportive_Plan_Locator = (By.XPATH,"//img[@src='/static/media/kids.27f92282.svg'][1]")
        Next_Button_Locator = (By.XPATH,"//button[contains(text(),'Next')]")
        Cash_Icon_Locator = (By.XPATH,"//img[@src='/static/media/cash.632a51f2.svg' and @alt='cash'][1]")
        Close_Button_Locator = (By.XPATH,"(//button[@class='close-button section-close'])[2]")
        Message_Input_Field = (By.ID,"comment")
        Blanket_And_Handkerchiefs_Locator = (By.XPATH,"//span[@class='slider round'][1]")
        Soundproof_Curtain_Locator = (By.XPATH, "(//span[@class='slider round'])[2]")
        Ice_Cream_locator = (By.XPATH,"//div[@class='counter-plus'][1]")
        Order_Requirements_Locator = (By.XPATH,"//div[contains(text(),'Order requirements')]")
        Enter_The_Number_And_Order_Locator = (By.XPATH,"(//button[@type='button'])[4]")
        Close_Card_Section_Locator = (By.XPATH,"(//button[@class='close-button section-close'])[3]")
        Verification_Input_Fıeld_Locator = (By.ID,"code")
        Confirm_Button_Locator = (By.XPATH,"//button[contains(text(),'Confirm')]")




        def __init__(self, driver):
            self.driver = driver


        def enter_locations(self, from_text, to_text):
            self.driver.find_element(*self.From_Field_Locator).send_keys(from_text)
            self.driver.find_element(*self.To_Field_Locator).send_keys(to_text)



        def click_call_taxi_button(self):
         self.driver.find_element(*self.Call_Taxi_Button_Locator).click()


        def click_supportive_plan(self):
          self.driver.find_element(*self.Supportive_Plan_Locator).click()


        def click_phone_number_field(self):
         self.driver.find_element(*self.Phone_Field_Locator).click()


        def enter_phone_number(self,phone_number):
          self.driver.find_element(*self.Phone_Number_Field_Locator).send_keys(phone_number)
          time.sleep(15)
          self.driver.find_element(*self.Next_Button_Locator).click()
          time.sleep(5)


        def click_add_card_icon(self):
         self.driver.find_element(*self.Add_Card_Icon_Locator).click()


        def enter_card_informations(self,card_number,cvv):
          self.driver.find_element(*self.Card_Number_Input_Field_Locator).send_keys(card_number)
          time.sleep(3)
          self.driver.find_element(*self.Cvv_Locator).send_keys(cvv)
          time.sleep(20)
          self.driver.find_element(*self.Link_Card_Locator).click()
          time.sleep(3)
          self.driver.find_element(*self.Close_Card_Section_Locator).click()


        def link_card(self):
          self.driver.find_element(*self.Link_Card_Locator).click()

        def enter_message_for_driver(self,message):
          self.driver.find_element(*self.Message_Input_Field).send_keys(message)

        def order_blanket_and_handkerchiefs(self):
          self.driver.find_element(*self.Blanket_And_Handkerchiefs_Locator).click()

        def order_soundproof_curtain(self):
          self.driver.find_element(*self.Soundproof_Curtain_Locator).click()

        def select_ice_cream(self):
          self.driver.find_element(*self.Ice_Cream_locator).click()

        def click_cash_icon(self):
         self.driver.find_element(*self.Cash_Icon_Locator).click()

        def click_order_requierements(self):
          self.driver.find_element(*self.Order_Requirements_Locator).click()

        def close_number_section(self):
          self.driver.find_element(*self.Close_Button_Locator).click()

        def click_Number_And_Order_Button(self):
          self.driver.find_element(*self.Enter_The_Number_And_Order_Locator).click()


        def close_Card_section(self):
           self.driver.find_element(*self.Close_Button_Locator).click()


        def enter_verification_code(self,verification_code):
         self.driver.find_element(*self.Verification_Input_Fıeld_Locator).send_keys(verification_code)
         time.sleep(4)
         self.driver.find_element(*self.Confirm_Button_Locator).click()















