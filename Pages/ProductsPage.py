from Pages.BasePage import Base
from Configs.Locators import Locators

class Products(Base):
   
   
    def _init_(self, driver):
        self.driver = driver

    def search_product(self, productType):
        homepage_text = self.wait_for(Locators.homepage_elem_loc).text
        products_button = self.wait_for_click(Locators.products_elem_loc).click()
        all_prods_text = self.wait_for(Locators.all_products_text_elem_loc).text
        search_button = self.wait_for_click(Locators.search_input_elem_loc).send_keys(productType)
        submit_button = self.wait_for_click(Locators.sumbit_search_elem_loc).click()
        searched_prods_text = self.wait_for(Locators.all_products_text_elem_loc).text
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        searched_products_list = self.find(Locators.content_text_elem_loc)
        searched_texts = []
        for searched_product in searched_products_list:
               searched_texts.append(searched_product.text)
        return homepage_text, all_prods_text, searched_prods_text, searched_texts