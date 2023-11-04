from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
from IPython.display import Image as Image2

options = webdriver.ChromeOptions() 
options.headless = True
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get("https://uims.cuchd.in/uims")

def login(UID,PWD):
    driver.find_element(By.ID, "txtUserId").send_keys(UID)
    driver.find_element(By.ID, "btnNext").click()
    driver.find_element(By.ID, "txtLoginPassword").send_keys(PWD)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://uims.cuchd.in/uims/GenerateCaptcha.aspx")
    driver.save_screenshot("captcha.png")
    full_screenshot = Image.open("captcha.png")
    left = (full_screenshot.width - 130) // 2  
    top = (full_screenshot.height - 70) // 2 
    right = left + 130 
    bottom = top + 70 
    cropped_screenshot = full_screenshot.crop((left, top, right, bottom))
    cropped_screenshot.save("captcha.png")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    Image.open("captcha.png").show()
    Image2(filename='captcha.png') 
    captcha = input("Enter the captcha : ")
    driver.find_element(By.ID, "txtcaptcha").send_keys(captcha)
    driver.find_element(By.ID, "btnLogin").click()
    print("Processing...")
    time.sleep(5)
    print("Logged In Successfull!\n")
    return True

def homepage():
    print("""\tMENU\n
        1. My Attendance
        2. Quit""")

    choice = int(input("\nChoose an option: "))
    if choice == 1:
        attendance()
        print()
        homepage()
    else :
        print("Quiting...")
        quit()

def attendance():
    table_data = []
    for row in driver.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[4]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[1]/table").find_elements(By.TAG_NAME,"tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME,"td")]
        table_data.append(row_data)
    print("\n \t My Attendance")
    for row in table_data[1:]:
        print(f"{row[2]}%\t{row[0]}")
    print("\n")

def mentor():
    print("\tMENTOR DETAILS \n")
    print(driver.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[1]").text)
    print(driver.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[2]").text)

def imp_msg():
    for i in driver.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[4]/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/ul").find_elements(By.TAG_NAME, "li"):
        print(i.text)

def profile():
    # driver.get("https://uims.cuchd.in/uims/frmStudentProfile.aspx")
    data = {}
    data['Name'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[14]/td[5]/table/tbody/tr/td/div').text
    data['UID'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td/div/div/span[2]').text
    data['Section'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[7]/td[2]/table/tbody/tr/td/div/div/span[2]').text
    data['DoB'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[26]/td[4]/table/tbody/tr/td/div').text
    
    data['Father_Name'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[16]/td[4]/table/tbody/tr/td/div').text
    data['Mother_Name'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[20]/td[4]/table/tbody/tr/td/div').text
    data['Address'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[32]/td[5]/table/tbody/tr/td/div').text

    data['Mobile_Number'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[47]/td[2]/table/tbody/tr[5]/td[5]/div').text
    data['Email'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[47]/td[2]/table/tbody/tr[5]/td[6]/div').text

    data['10_School'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[3]/td[4]/div').text
    data['10_Pass_Year'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[3]/td[6]/div').text
    data['10_Marks'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[3]/td[7]/div').text

    data['12_School'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[4]/td[4]/div').text
    data['12_Pass_Year'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[4]/td[6]/div').text
    data['12_Marks'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[43]/td[2]/table/tbody/tr[4]/td[7]/div').text


    data['Hostel'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[70]/td[4]/table/tbody/tr/td/div').text
    data['Hostel_Name'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[72]/td[3]/table/tbody/tr/td/div').text
    data['Hostel_Room'] = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[74]/td[3]/table/tbody/tr/td/div').text

    max_key_length = max(len(key) for key in data.keys())
    for key, value in data.items():
        formatted_key = key.replace('_', ' ').title()
        formatted_key = formatted_key.ljust(max_key_length)
        print(f'{formatted_key} : {value}')

def main():
    print("\n\tWelcome to UIMS-Xplorer\n\n")
    UID = input("Enter you UID : ")
    PASSWORD = input("Enter your password : ")
    if login(UID,PASSWORD) :
        homepage()
    else :
        print("SOMETHING WRONG")

if __name__ == "__main__":
    main()