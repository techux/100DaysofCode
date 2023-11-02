from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

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
    captcha = input("Enter the captcha : ")
    driver.find_element(By.ID, "txtcaptcha").send_keys(captcha)
    driver.find_element(By.ID, "btnLogin").click()
    print("Processing...")
    time.sleep(5)
    print("Logged In Successfull!\n")
    return True

def attendance():
    table_data = []
    for row in driver.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[4]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[1]/table").find_elements(By.TAG_NAME,"tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME,"td")]
        table_data.append(row_data)
    print("\n \t My Attendance")
    for row in table_data[1:]:
        print(f"{row[2]}%\t{row[0]}")
    print("\n")

def homepage():
    print("""\tMENU\n
        1. My Attendance
        2. Quit""")

    choice = int(input("\nChoose an option: "))
    if choice == 1:
        attendance()
    else :
        print("Quiting...")
        quit()

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