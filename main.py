from data import URBAN_ROUTES_URL
from helpers import is_url_reachable

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes Server.")
        else:
            print("Cannot connect to Urban Routes.")

    def test_set_route(self):
        # Add in S8
        print("Function created for testing set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for test plan.")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for testing filling phone number field.")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for testing filling card field.")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for testing creating a comment for driver.")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for testing ordering blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        for mission in range(2):
            # Add in S8
            print("Function created for testing ordering an ice creams.")
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for testing searching car models and checking appears.")
        pass
