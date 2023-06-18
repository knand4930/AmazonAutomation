import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

# from amazoncaptcha import AmazonCaptcha
# from PIL import Image
# import pytesseract


service = Service(ChromeDriverManager().install())

def open_browser(url, username, password, keywords, CardNumber, CardHolder, ExpireMonth, ExpireYear, cvv):

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Launch browser in incognito mode
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Perform the login process with different credentials for each browser
    login_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
    login_field.send_keys(username)
    login_submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input')
    login_submit.click()
    
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/input')
    password_field.send_keys(password)
    password_submit = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input")
    password_submit.click()    
    time.sleep(40)
    # captch = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/div[1]/img')
    # captcha = AmazonCaptcha.fromlink(captch)
    # solution = captcha.solve(keep_logs=True)
    # print("Solutions : ", solution)
    # time.sleep(2)

    #Captcha
    # /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/input
    # /html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[4]/span/span/input
    
    # Perform item search and add to cart

    search_field = driver.find_element("id", "twotabsearchtextbox")
    search_field.send_keys(keywords)
    search_field.send_keys(Keys.ENTER)
    time.sleep(2)

 
    try:
        product_path_1 = '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img'
        product_field_1 = driver.find_element(By.XPATH, product_path_1)
        product_field_1.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)      

        buy_field = driver.find_element(By.ID, "buy-now-button")
        buy_field.click()
        time.sleep(2)

        credit_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
        credit_card.click()
        time.sleep(2)

        click_enter_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
        click_enter_card.click()
        time.sleep(2)

        iframe = WebDriverWait(driver, 10).until(
                            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/iframe"))
                        )
        
        card_number = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
        card_number.clear()
        card_number.send_keys(CardNumber)
        time.sleep(2)
        
        card_holder = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
        card_holder.clear()
        card_holder.send_keys(CardHolder)
        time.sleep(2)

        expire_month = driver.find_element(By.NAME, "ppw-expirationDate_month")
        select_month = Select(expire_month)
        select_month.select_by_visible_text(ExpireMonth)
        #select_month.select_by_value(ExpireMonth)
        time.sleep(2)

        expire_year = driver.find_element(By.NAME, "ppw-expirationDate_year")
        select_year = Select(expire_year)
        select_year.select_by_visible_text(ExpireYear)
        #select_year.select_by_value(ExpireYear)
        time.sleep(2)

        complete_card = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
        complete_card.click()
        time.sleep(2)

        driver.switch_to.default_content()
        time.sleep(15)

        add_cvv = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")
        add_cvv.send_keys(cvv)
        time.sleep(10)

        save_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[9]/div/div[1]/div/label/input")
        save_card.click()
        time.sleep(10)

        complete_payment= driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span")
        complete_payment.click()
        time.sleep(10)

        place_order=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span/span/input")
        place_order.click()

        time.sleep(180)
        driver.quit()
    except NoSuchElementException:
        msg = "Errror"
        try:
            product_path_2 = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img"
            product_field_2 = driver.find_element(By.XPATH, product_path_2)
            product_field_2.click()

            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)

            buy_field = driver.find_element(By.ID, "buy-now-button")
            buy_field.click()
            time.sleep(2)

            credit_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
            credit_card.click()
            time.sleep(2)

            click_enter_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
            click_enter_card.click()
            time.sleep(2)

            iframe = WebDriverWait(driver, 10).until(
                            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/iframe"))
                        )
            
            card_number = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
            card_number.clear()
            card_number.send_keys(CardNumber)
            time.sleep(2)
            
            card_holder = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
            card_holder.clear()
            card_holder.send_keys(CardHolder)
            time.sleep(2)

            expire_month = driver.find_element(By.NAME, "ppw-expirationDate_month")
            select_month = Select(expire_month)
            select_month.select_by_visible_text(ExpireMonth)
            #select_month.select_by_value(ExpireMonth)
            time.sleep(2)

            expire_year = driver.find_element(By.NAME, "ppw-expirationDate_year")
            select_year = Select(expire_year)
            select_year.select_by_visible_text(ExpireYear)
            #select_year.select_by_value(ExpireYear)
            time.sleep(2)

            complete_card = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
            complete_card.click()
            time.sleep(2)

            driver.switch_to.default_content()
            time.sleep(15)

            add_cvv = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")
            add_cvv.send_keys(cvv)
            time.sleep(10)

            save_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[9]/div/div[1]/div/label/input")
            save_card.click()
            time.sleep(10)

            complete_payment= driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span")
            complete_payment.click()
            time.sleep(10)

            place_order=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span/span/input")
            place_order.click()

            time.sleep(180)
            driver.quit()
        except NoSuchElementException as E:
            print(E)
            try:
                product_path_3 = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img"
                product_field_3 = driver.find_element(By.XPATH, product_path_3)
                product_field_3.click()
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(2)

                buy_field = driver.find_element(By.ID, "buy-now-button")
                buy_field.click()
                time.sleep(2)

                credit_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
                credit_card.click()
                time.sleep(2)

                click_enter_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
                click_enter_card.click()
                time.sleep(2)

                iframe = WebDriverWait(driver, 10).until(
                            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/iframe"))
                        )
                
                card_number = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
                card_number.clear()
                card_number.send_keys(CardNumber)
                time.sleep(2)
                
                card_holder = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
                card_holder.clear()
                card_holder.send_keys(CardHolder)
                time.sleep(2)

                expire_month = driver.find_element(By.NAME, "ppw-expirationDate_month")
                select_month = Select(expire_month)
                select_month.select_by_visible_text(ExpireMonth)
                #select_month.select_by_value(ExpireMonth)
                time.sleep(2)

                expire_year = driver.find_element(By.NAME, "ppw-expirationDate_year")
                select_year = Select(expire_year)
                select_year.select_by_visible_text(ExpireYear)
                #select_year.select_by_value(ExpireYear)
                time.sleep(2)

                complete_card = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
                complete_card.click()
                time.sleep(2)

                driver.switch_to.default_content()
                time.sleep(15)

                add_cvv = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")
                add_cvv.send_keys(cvv)
                time.sleep(10)

                save_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[9]/div/div[1]/div/label/input")
                save_card.click()
                time.sleep(10)

                complete_payment= driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span")
                complete_payment.click()
                time.sleep(10)

                place_order=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span/span/input")
                place_order.click()

                time.sleep(180) 
                driver.quit()
            except NoSuchElementException as E:
                print(E)
                try:
                    product_path_4 = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img"
                    product_field_4 = driver.find_element(By.XPATH, product_path_4)
                    product_field_4.click()
                    driver.switch_to.window(driver.window_handles[-1])
                    time.sleep(2)

                    buy_field = driver.find_element(By.ID, "buy-now-button")
                    buy_field.click()
                    time.sleep(2)

                    credit_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
                    credit_card.click()
                    time.sleep(2)

                    click_enter_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
                    click_enter_card.click()
                    time.sleep(2)

                    iframe = WebDriverWait(driver, 10).until(
                            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/iframe"))
                        )
                    
                    card_number = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
                    card_number.clear()
                    card_number.send_keys(CardNumber)
                    time.sleep(2)
                    
                    card_holder = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
                    card_holder.clear()
                    card_holder.send_keys(CardHolder)
                    time.sleep(2)

                    expire_month = driver.find_element(By.NAME, "ppw-expirationDate_month")
                    select_month = Select(expire_month)
                    select_month.select_by_visible_text(ExpireMonth)
                    #select_month.select_by_value(ExpireMonth)
                    time.sleep(2)

                    expire_year = driver.find_element(By.NAME, "ppw-expirationDate_year")
                    select_year = Select(expire_year)
                    select_year.select_by_visible_text(ExpireYear)
                    #select_year.select_by_value(ExpireYear)
                    time.sleep(2)

                    complete_card = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
                    complete_card.click()
                    time.sleep(2)
                    
                    driver.switch_to.default_content()
                    time.sleep(15)

                    add_cvv = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")                    
                    add_cvv.send_keys(cvv)
                    time.sleep(10)

                    #field
                    save_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[9]/div/div[1]/div/label/input")
                    save_card.click()
                    time.sleep(10)

                    complete_payment= driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span")
                    complete_payment.click()
                    time.sleep(10)

                    place_order=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span/span/input")
                    place_order.click()
                    time.sleep(180)

                    driver.quit()
                except NoSuchElementException as E:
                    print(E)
                    try:
                        product_path_5 = "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img"
                        product_field_5 = driver.find_element(By.XPATH, product_path_5)
                        product_field_5.click()
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(2)
                        
                        buy_field = driver.find_element(By.ID, "buy-now-button")
                        buy_field.click()
                        time.sleep(2)

                        credit_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[1]/span/div/label/input")
                        credit_card.click()
                        time.sleep(2)

                        click_enter_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/span/div/a")
                        click_enter_card.click()
                        time.sleep(2)

                        iframe = WebDriverWait(driver, 10).until(
                                EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/iframe"))
                            )
                        
                        card_number = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div/input")
                        card_number.clear()
                        card_number.send_keys(CardNumber)
                        time.sleep(2)
                        
                        card_holder = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/input")
                        card_holder.clear()
                        card_holder.send_keys(CardHolder)
                        time.sleep(2)

                        expire_month = driver.find_element(By.NAME, "ppw-expirationDate_month")
                        select_month = Select(expire_month)
                        select_month.select_by_visible_text(ExpireMonth)
                        #select_month.select_by_value(ExpireMonth)
                        time.sleep(2)

                        expire_year = driver.find_element(By.NAME, "ppw-expirationDate_year")
                        select_year = Select(expire_year)
                        select_year.select_by_visible_text(ExpireYear)
                        #select_year.select_by_value(ExpireYear)
                        time.sleep(2)

                        complete_card = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div/form/div[2]/div/span[2]/span/input")
                        complete_card.click()
                        time.sleep(2)
                        
                        driver.switch_to.default_content()
                        time.sleep(15)

                        add_cvv = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/div[1]/input[1]")                    
                        add_cvv.send_keys(cvv)
                        time.sleep(10)

                        #field
                        save_card = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[5]/div/div[3]/div/div/div[2]/div/div[2]/div/div/form/div/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[9]/div/div[1]/div/label/input")
                        save_card.click()
                        time.sleep(10)

                        complete_payment= driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/span/span/span/span")
                        complete_payment.click()
                        time.sleep(10)

                        place_order=driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/span/span/input")
                        place_order.click()
                        time.sleep(180)

                        driver.quit()
                    except NoSuchElementException as E:
                        print(E)

    
    time.sleep(180)
    driver.quit()

if __name__ == "__main__":
    urls = [
        "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
        "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
    ]

    usernames = [
        "Kingntrntnl@gmail.com",
        "tradersv358@gmail.com",
    ]
    
    passwords = [
        "Abcd@1234",
        "Abcd@1234",
    ]

    keywords = [
        "sumsung ",
        "one plus",
    ]

    CardNumber = [
        "5321350208188946",
        "5321350208189043",
    ]

    CardHolder = [
        "Kingntrntnl",
        "Kinginter",
    ]

    ExpireMonth = [
        "06",
        "06",
    ]

    ExpireYear = [
        "2023",
        "2023",
    ]

    cvv = [
        "556",
        "913",
    ]

    processes = []

    for i in range(len(urls)):
        process = Process(target=open_browser, args=(urls[i], usernames[i], passwords[i], keywords[i], CardNumber[i], CardHolder[i], ExpireMonth[i], ExpireYear[i], cvv[i]))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()