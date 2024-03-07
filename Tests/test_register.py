from Pages.LogInSignUpPage import SignUp
from Configs.testData import testData
from Tests.test_base import BaseTest

#test case number 1
class Test(BaseTest):

    def test_signUp_delete(self):
        signup_obj = SignUp(self.driver_2)
        homepage_text, new_user_singup_text, enter_info_text, account_created_text, loggedin_as_text = signup_obj.sign_up(
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
        assert homepage_text == testData.homepage_text
        assert loggedin_as_text == testData.new_user_name
        assert new_user_singup_text == testData.new_user_text
        assert enter_info_text == testData.enter_information_text
        assert account_created_text == testData.acc_created_text
        assert loggedin_as_text == testData.new_user_name
        account_deleted_text = signup_obj.delete_account()
        assert account_deleted_text == testData.acc_deleted_text
        
        
        
