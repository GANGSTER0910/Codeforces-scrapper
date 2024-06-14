from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def cf_answer_submitter(contest_link, handle_or_email, password, prblm_no, language, code):
    driver = webdriver.Chrome()
    driver.get(contest_link)
    driver.find_element(By.LINK_TEXT, "Enter").click()
    time.sleep(5)
    login = driver.find_element(By.ID, "handleOrEmail").send_keys(handle_or_email)
    time.sleep(5)
    password = driver.find_element(By.ID,"password" ).send_keys(password)
    time.sleep(5)
    remember = driver.find_element(By.ID, "remember").click()
    login_btn = driver.find_element(By.CLASS_NAME, "submit")
    login_btn.click()
    time.sleep(5)
    prblm = driver.find_element(By.LINK_TEXT, prblm_no ).click()
    time.sleep(10)
    submit_Code= driver.find_element(By.LINK_TEXT, "SUBMIT CODE").click()
    time.sleep(5)
    
    set_Code = driver.find_element(By.CLASS_NAME, "ace_text-input").send_keys(code)
    time.sleep(2)

    choose_problem = driver.find_element(By.NAME, "submittedProblemIndex").click()

    time.sleep(5)
    xpath_prblm = f'//*[@id="pageContent"]/form/table/tbody/tr[1]/td[2]/label/select/option[{ord(prblm_no) - 63}]'
    select = driver.find_element(By.XPATH, xpath_prblm).click()
    time.sleep(5)
    language= language.upper()
    language_selector= {
        'JAVA':11,
        'C++': 4,
        'C': 6,
        'PYTHON':22
    }
    xpath_lang = f'//*[@id="pageContent"]/form/table/tbody/tr[3]/td[2]/select/option[{language_selector.get(language)}]'
    select_lang = driver.find_element(By.XPATH,xpath_lang).click()

    time.sleep(2)

    submit_btn = driver.find_element(By.XPATH,'//*[@id="singlePageSubmitButton"]' ).click()

    time.sleep(20)



def read_code():
    print("Enter the code: ")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    java_code = "\n".join(lines)
    return java_code


# contest_link = input("Enter the contest link: ")
# handleoremail = input("Enter the handleoremail: ")
# passw = input("Enter the password of cf handle: ")
# prblmno = input("Enter the prblem no: ")
# lang = input("Enter your language: ")
# code = read_code()

# cf_answer_submitter(contest_link, handleoremail, passw, prblmno,  lang, code)
