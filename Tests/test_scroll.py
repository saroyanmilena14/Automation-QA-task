from Pages.Homepage import Home
from Configs.testData import testData
from Tests.test_base import BaseTest

#test case number 25
class Test(BaseTest):

    def test_scroll(self):
        homepage_obj = Home(self.driver_2)
        homepage_text, subsciption_button_text = homepage_obj.scroll_down()
        homepage_text1 = homepage_obj.scroll_up()
        assert homepage_text == testData.homepage_text
        assert subsciption_button_text == testData.subscrip_button_text
        assert homepage_text1 == testData.homepage_text
