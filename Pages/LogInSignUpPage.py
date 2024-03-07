from Pages.BasePage import Base
from Configs.Locators import Locators


class SignUp(Base):
   
   
    def _init_(self, driver):
        self.driver = driver

    def sign_up(self, name, email, password, lastName, company, add, add2, state, city, zip, mobNum):
        homepage_text = self.wait_for(Locators.homepage_elem_loc).text
        signUpButton = self.wait_for_click(Locators.sign_up_elem_loc).click()
        new_user_singup_text = self.wait_for(Locators.new_user_signup_loc).text
        name_button = self.wait_for_click(Locators.input_name_loc).send_keys(name)
        email_button = self.wait_for_click(Locators.input_email_loc).send_keys(email)
        sign_up_button = self.wait_for_click(Locators.sing_up_button_loc).click()
        enter_info_text = self.wait_for(Locators.enter_info_loc).text
        gender_select_button = self.wait_for_click(Locators.gender_elem_loc).click()
        pass_input_button = self.wait_for_click(Locators.password_elem_loc).send_keys(password)
        days_elem_button = self.wait_for_click(Locators.days_elem_loc).click()
        day_elem_button = self.wait_for_click(Locators.day_option_loc).click()
        months_elem_button = self.wait_for_click(Locators.months_elem_loc).click()
        month_elem_button = self.wait_for_click(Locators.month_option_loc).click()
        years_elem_button = self.wait_for_click(Locators.years_elem_loc).click()
        year_elem_button = self.wait_for_click(Locators.year_option_loc).click()
        news_let_button = self.wait_for_click(Locators.news_checkbox__elem_loc).click()
        special_offer_button = self.wait_for_click(Locators.special_elem_loc).click()
        first_name_button = self.wait_for_click(Locators.first_name_loc).send_keys(name)
        last_name_button = self.wait_for_click(Locators.last_name_loc).send_keys(lastName)
        company_button = self.wait_for_click(Locators.company_elem_loc).send_keys(company)
        address_button = self.wait_for_click(Locators.address_elem_loc).send_keys(add)
        address2_button = self.wait_for_click(Locators.address2_elem_loc).send_keys(add2)
        countries_button = self.wait_for_click(Locators.country_elem_loc).click()
        country_button = self.wait_for_click(Locators.country_option_elem_loc).click()
        state_button = self.wait_for_click(Locators.state_elem_loc).send_keys(state)
        city_button = self.wait_for_click(Locators.city_elem_loc).send_keys(city)
        zipcode_button = self.wait_for_click(Locators.zipcode_elem_loc).send_keys(zip)
        mobile_num_button = self.wait_for_click(Locators.mobile_num_elem_loc).send_keys(mobNum)
        create_account_button = self.wait_for_click(Locators.create_ac_elem_loc).click()
        account_created_text = self.wait_for(Locators.account_created_deleted_text_loc).text
        continue_button = self.wait_for_click(Locators.continue_elem_loc).click()
        loggedin_as_text = self.wait_for_visible(Locators.loggedin_as_loc).text
        return homepage_text, new_user_singup_text, enter_info_text, account_created_text , loggedin_as_text
        
    def delete_account(self):
        delete_button = self.wait_for_click(Locators.delete_elem_loc).click()
        account_deleted_text = self.wait_for(Locators.account_created_deleted_text_loc).text
        continue_button = self.wait_for_click(Locators.continue_elem_loc).click()
        return account_deleted_text 
    
    def log_in (self, email, password):
        homepage_text = self.wait_for(Locators.homepage_elem_loc).text
        loginButton = self.wait_for_click(Locators.sign_up_elem_loc).click()
        login_email_button = self.wait_for(Locators.login_email_elem_loc).send_keys(email)
        login_pass_button = self.wait_for(Locators.login_pass_elem_loc).send_keys(password)
        login_submit_button = self.wait_for_click(Locators.login_elem_loc).click()