from selenium import webdriver
import time
import config
import enums


def login(driver):
    login_page_url = "https://selfregistration.cowin.gov.in/"
    driver.get(login_page_url)
    mobile_number_field = driver.find_element_by_id("mat-input-0")
    mobile_number_field.send_keys(config.phone_number)
    time.sleep(0.5)
    get_otp_button = driver.find_element_by_class_name("login-btn")
    get_otp_button.click()
    input("Please enter otp, click verify otp and press enter in the terminal")
    return


def select_patient(driver):
    schedule_button = driver.find_element_by_link_text("Schedule")
    schedule_button.click()
    time.sleep(0.5)

    schedule_now_button = driver.find_element_by_css_selector(
        ".register-btn.schedule-appointment ")
    schedule_now_button.click()
    time.sleep(1)


def select_district(driver):
    # Switch to district wise search
    switch_to_district = driver.find_element_by_css_selector(
        ".custom-checkbox label div")
    switch_to_district.click()
    time.sleep(0.5)

    # Open state list
    state_select_dropdown = driver.find_element_by_css_selector(
        'mat-select.mat-select[formcontrolname="state_id"]')
    state_select_dropdown.click()

    # Select State
    element_id = "mat-option-" + config.state_id
    state_select_list_item = driver.find_element_by_id(element_id)
    state_select_list_item.click()

    time.sleep(0.5)

    # Open district list
    district_select_dropdown = driver.find_element_by_css_selector(
        'mat-select.mat-select[formcontrolname="district_id"]')
    district_select_dropdown.click()

    # Select district
    element_id = "mat-option-" + config.district_id
    district_select_list_item = driver.find_element_by_id(element_id)
    district_select_list_item.click()

    return


def click_search(driver):
    search_button = driver.find_element_by_css_selector(
        ".pin-search-btn.district-search ")
    search_button.click()
    time.sleep(0.5)
    return


def select_filters(driver):
    # TODO add age option to config // currently limited to 18+
    # Age filter
    if config.age is enums.AgeType.MoreThanEighteen:
        select_filter("1")
    if config.age is enums.AgeType.MoreThanFortyFive:
        select_filter("2")

    # Vaccine filter
    if config.vaccine_type is enums.VaccineType.Covishield:
        select_filter("3")
    if config.vaccine_type is enums.VaccineType.Covaxin:
        select_filter("4")

    # Paid filter
    if config.paid_type is enums.PaidType.Paid:
        select_filter("5")
    if config.paid_type is enums.PaidType.Free:
        select_filter("6")


def select_filter(filter_id):
    selector = '.agefilterblock div label[for="c'+ filter_id + '"]'
    '.agefilterblock div label[for="c%s"]'.format(filter_id)
    filter_button = driver.find_element_by_css_selector(selector)
    filter_button.click()


def search_slot(driver):
    all_slots = driver.find_elements_by_css_selector(
        """.slot-available-main[_ngcontent-wlg-c117] .slot-available-wrap[_ngcontent-wlg-c117] li[_ngcontent-wlg-c117] .slots-box[_ngcontent-wlg-c117] a[_ngcontent-wlg-c117]""")
    for slot in all_slots:
        if 'no-seat' not in slot.get_attribute("class").split():
            # If slot is found
            slot.click()
            sleep(0.1)
            return True
    # If no slot is found retry after 15 seconds
    return False


def confirm(driver):
    pass

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login(driver)
    select_patient(driver)
    select_district(driver)
    click_search(driver)
    select_filters(driver)
    while not search_slot(driver):
        print("waiting 5 seconds")
        time.sleep(5)
        click_search(driver)
        select_filters(driver)
    confirm(driver)
    input("You got it?")