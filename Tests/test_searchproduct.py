from Pages.ProductsPage import Products
from Configs.testData import testData
from Tests.test_base import BaseTest

#test case number 9
class Test(BaseTest):
    def test_search(self):
        products_obj = Products(self.driver_2)
        homepage_text, all_prods_text, searched_prods_text, searched_texts = products_obj.search_product(testData.prod_type)
        assert homepage_text == testData.homepage_text
        assert all_prods_text == testData.all_prods_text
        assert searched_prods_text == testData.searched_prods_text
        for text in searched_texts:
            assert testData.prod_type in text.lower()
        
