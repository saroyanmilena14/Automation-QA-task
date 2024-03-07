from Pages.BasePage import Base
from Configs.Locators import Locators

class Cart(Base):
   
   
    def _init_(self, driver):
        self.driver = driver

    def place_oder(self, comment, cardName, cardNum, cvc, month_exp,year_exp):
        addto_cart_button = self.wait_for_click(Locators.add_to_cart_ele_loc).click()
        continue_shop_button = self.wait_for_click(Locators.continue_shop_elem_loc).click()
        cart_button = self.wait_for_click(Locators.cart_elem_loc).click()
        verify_cart_text = self.wait_for(Locators.shopping_cart_elem_loc).text
        proceed_button = self.wait_for_click(Locators.proceed_elem_loc).click()
        address1_verify_button_text = self.wait_for(Locators.address1_verify_elem_loc).text
        address2_verify_button_text = self.wait_for(Locators.address2_verify_elem_loc).text
        city_state_zipcode_button_text = self.wait_for(Locators.city_verify_elem_loc).text
        comment_button = self.wait_for(Locators.comment_elem_loc).send_keys(comment)
        place_order_button = self.wait_for_click(Locators.place_order_elem_loc).click()
        name_card_button = self.wait_for(Locators.name_on_card_elem_loc).send_keys(cardName)
        card_num_button = self.wait_for(Locators.card_num_elem_loc).send_keys(cardNum)
        cvc_button = self.wait_for(Locators.cvc_elem_loc).send_keys(cvc)
        month_exp_button = self.wait_for(Locators.month_exp_elem_loc).send_keys(month_exp)
        year_exp_button = self.wait_for(Locators.year_exp_elem_loc).send_keys(year_exp)
        confirm_button = self.wait_for_click(Locators.confirm_order_elem_loc).click()
        confirmed_success_text = self.wait_for(Locators.confirmed_successful_loc).text
        return verify_cart_text, address1_verify_button_text, address2_verify_button_text, city_state_zipcode_button_text , confirmed_success_text