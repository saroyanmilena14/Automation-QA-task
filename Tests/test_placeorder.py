from Pages.LogInSignUpPage import SignUp
from Configs.testData import testData
from Tests.test_base import BaseTest
from Pages.CartPage import Cart

#test case number 16
class Test(BaseTest):

    def test_place_order(self):
        placeorder_obj = Cart(self.driver_2)
        login_obj = SignUp(self.driver_2)
        signup_obj = SignUp(self.driver_2)
        homepage_text, new_user_singup_text, enter_info_text, account_created_text,  loggedin_as_text = signup_obj.sign_up(
            testData.new_user_name,
            testData.new_user_email, 
            testData.passWord,
            testData.lastName,
            testData.company,
            testData.address_1,
            testData.address_2,
            testData.state,
            testData.city,
            testData.zipcode,
            testData.mobile_number)
        verify_cart_text, address1_verify_button_text, address2_verify_button_text, city_state_zipcode_button_text, confirmed_success_text= placeorder_obj.place_oder(testData.comment, testData.cardName, testData.cardNum, testData.cvc, testData.month_exp, testData.year_exp)
        account_deleted_text = signup_obj.delete_account()
        assert homepage_text == testData.homepage_text
        assert loggedin_as_text == testData.new_user_name
        assert verify_cart_text == testData.shopping_cart_text
        assert address1_verify_button_text == testData.address_1
        assert address2_verify_button_text == testData.address_2
        assert city_state_zipcode_button_text == testData.city+" "+testData.state+" "+testData.zipcode
        assert confirmed_success_text == testData.success_text
        assert account_deleted_text == testData.acc_deleted_text
        