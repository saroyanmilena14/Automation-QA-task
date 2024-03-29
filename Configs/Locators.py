from selenium.webdriver.common.by import By

class Locators:
    
    homepage_elem_loc= (By.XPATH, "//*[text()='Full-Fledged practice website for Automation Engineers']")
    sign_up_elem_loc = (By.XPATH, "//*[text()=' Signup / Login']")
    new_user_signup_loc = (By.XPATH, "//div[@class='signup-form']//h2")
    input_name_loc = (By.XPATH, "//input[@data-qa='signup-name']")
    input_email_loc = (By.XPATH, "//input[@data-qa='signup-email']")
    sing_up_button_loc =(By.XPATH, "//button[@data-qa='signup-button']")
    enter_info_loc = (By.XPATH, "//*[text()='Enter Account Information']")
    gender_elem_loc = (By.XPATH, "//*[@id='uniform-id_gender1']")
    password_elem_loc = (By.XPATH, "//*[@data-qa='password']")
    days_elem_loc = (By.XPATH, "//*[@id='days']")
    day_option_loc = (By.XPATH, "//*[@id='days']//option[@value='1']")
    months_elem_loc = (By.XPATH, "//*[@id='months']")
    month_option_loc = (By.XPATH, "//*[@id='months']//option[@value='3']")
    years_elem_loc = (By.XPATH, "//*[@id='years']")
    year_option_loc = (By.XPATH,"//*[@id='years']//option[@value='2000']")
    news_checkbox__elem_loc = (By.XPATH, "//*[@id='newsletter']")
    special_elem_loc = (By.XPATH, "//*[@id='optin']")
    first_name_loc = (By.XPATH, "//*[@data-qa='first_name']")
    last_name_loc = (By.XPATH, "//*[@data-qa='last_name']")
    company_elem_loc = (By.XPATH, "//*[@data-qa='last_name']")
    address_elem_loc = (By.XPATH, "//*[@data-qa='address']")
    address2_elem_loc = (By.XPATH, "//*[@data-qa='address2']")
    country_elem_loc = (By.XPATH, "//*[@id='country']")
    country_option_elem_loc = (By.XPATH, "//*[@id='country']//option[@value='Canada']")
    state_elem_loc = (By.XPATH, "//*[@id='state']")
    city_elem_loc = (By.XPATH, "//*[@id='city']")
    zipcode_elem_loc = (By.XPATH, "//*[@id='zipcode']")
    mobile_num_elem_loc = (By.XPATH, "//*[@id='mobile_number']")
    create_ac_elem_loc = (By.XPATH, "//*[@data-qa='create-account']")
    account_created_deleted_text_loc = (By.XPATH, "//h2[@data-qa]")
    continue_elem_loc = (By.XPATH, "//*[@data-qa='continue-button']")
    loggedin_as_loc = (By.XPATH, "//*[text()=' Logged in as ']//b")
    delete_elem_loc = (By.XPATH, "//*[text()=' Delete Account']")
    alert_elem_loc = (By.XPATH, "//*[text()='Save']")
    products_elem_loc = (By.XPATH, "//*[text()=' Products']")
    all_products_text_elem_loc = (By.XPATH, "//h2[@class='title text-center']")
    search_input_elem_loc = (By.XPATH, "//*[@id='search_product']")
    content_text_elem_loc = (By.XPATH, "//div[@class='productinfo text-center']")
    sumbit_search_elem_loc = (By.XPATH, "//*[@id='submit_search']")
    login_email_elem_loc = (By.XPATH, "//*[@data-qa='login-email']")
    login_pass_elem_loc = (By.XPATH, "//*[@data-qa='login-password']")
    login_elem_loc = (By.XPATH, "//*[@data-qa='login-button']")
    cart_elem_loc = (By.XPATH, "//*[text()=' Cart']")
    add_to_cart_ele_loc = (By.XPATH, "//*[text()='Add to cart']")
    continue_shop_elem_loc = (By.XPATH, "//*[text()='Continue Shopping']")
    shopping_cart_elem_loc = (By.XPATH, "//*[@class='breadcrumb']//li[2]")
    proceed_elem_loc = (By.XPATH, "//*[text()='Proceed To Checkout']")
    address1_verify_elem_loc = (By.XPATH, "//li[@class='address_address1 address_address2'][2]")
    address2_verify_elem_loc = (By.XPATH, "//li[@class='address_address1 address_address2'][3]")
    city_verify_elem_loc = (By.XPATH, "//*[@id='address_delivery']//li[@class='address_city address_state_name address_postcode']")
    name_on_card_elem_loc = (By.XPATH, "//*[@data-qa='name-on-card']")
    card_num_elem_loc = (By.XPATH, "//*[@data-qa='card-number']")
    cvc_elem_loc = (By.XPATH, "//*[@data-qa='cvc']")
    month_exp_elem_loc = (By.XPATH, "//*[@data-qa='expiry-month']")
    year_exp_elem_loc = (By.XPATH, "//*[@data-qa='expiry-year']")
    confirm_order_elem_loc = (By.XPATH, "//*[@id='submit']")
    confirmed_successful_loc = (By.XPATH, "//*[@data-qa='order-placed']//b")
    comment_elem_loc = (By.XPATH, "//*[@name='message']")
    place_order_elem_loc = (By.XPATH, "//*[text()='Place Order']")
    subscription_elem_loc = (By.XPATH, "//*[text()='Subscription']")
