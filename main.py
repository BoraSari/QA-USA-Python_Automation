import time
from pydoc import Helper
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import Pages
import helpers
from data import URBAN_ROUTES_URL
from helpers import is_url_reachable



class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes Server.")
        else:
            print("Cannot connect to Urban Routes.")

    def test_set_route(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601","1300 1st St")
        urban_page.click_call_taxi_button()

        taxi_element = self.driver.find_element(By.XPATH, "//button[contains(text(),'Call a taxi')]")
        assert taxi_element.is_displayed()



    def test_select_plan(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()

        supportive_plan_element_price = self.driver.find_element(By.XPATH,"(//div[@class='tcard-price'])[5]").text
        assert supportive_plan_element_price.__contains__("8.6")

    def test_fill_phone_number(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        urban_page.click_phone_number_field()
        urban_page.enter_phone_number("+1 123 123 12 12")
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.enter_verification_code(phone_code)

        next_button = self.driver.find_element(By.XPATH,"//button[contains(text(),'Next')]")
        assert  next_button.is_enabled()

    def test_fill_card(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        urban_page.click_cash_icon()
        urban_page.click_add_card_icon()
        urban_page.enter_card_informations("1234 5678 9100","1111")


        actual_result = self.driver.find_element(By.ID,"number").get_property("value")
        expected_result = "1234 5678 9100"
        assert expected_result.__contains__(actual_result)



    def test_comment_for_driver(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        urban_page.enter_message_for_driver("Stop at the juice bar, please")


        actual_result = self.driver.find_element(By.ID,"comment").get_attribute("value")
        expected_result = "Stop at the juice bar, please"
        assert expected_result.__contains__(actual_result)




    def test_order_blanket_and_handkerchiefs(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        urban_page.order_blanket_and_handkerchiefs()
        urban_page.order_soundproof_curtain()


        Blanket_and_Handkerchiefs_Element = self.driver.find_element(By.XPATH,"//span[@class='slider round'][1]")
        assert Blanket_and_Handkerchiefs_Element.is_enabled()





    def test_order_2_ice_creams(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        for mission in range(0,2):
            urban_page.select_ice_cream()
            time.sleep(5)



        quantity_of_ice_creams = self.driver.find_element(By.XPATH,"//div[@class='counter-value' and contains(text(),'2')]")
        assert quantity_of_ice_creams.text.__contains__("2")



    def test_car_search_model_appears(self):
        urban_page = Pages.UrbanRoutesPage(self.driver)
        self.driver.get(URBAN_ROUTES_URL)
        urban_page.enter_locations("East 2nd Street, 601", "1300 1st St")
        urban_page.click_call_taxi_button()
        urban_page.click_supportive_plan()
        urban_page.click_phone_number_field()
        urban_page.enter_phone_number("+1 123 123 12 12")
        phone_code = helpers.retrieve_phone_code(self.driver)
        urban_page.enter_verification_code(phone_code)
        urban_page.enter_message_for_driver("Stop at the juice bar, please")
        urban_page.click_Number_And_Order_Button()



        search_car_message = self.driver.find_element(By.XPATH,"//div[contains(text(),'Car search')]")
        assert search_car_message.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
