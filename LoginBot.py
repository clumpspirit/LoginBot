from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


options = Options()
unpacked_extension_path = 'C:\\Users\\nide1\\PycharmProjects\\LoginBot\\wizextension\\wizextension.zip'
options.add_extension(unpacked_extension_path)

driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\nide1\\PycharmProjects\\LoginBot\\chromedriver.exe')
driver.get('https://www.freekigames.com/')
time.sleep(6)

def loginfunction(usernamestr, passwordstr):
    login = driver.find_element_by_id('loginContainer')
    time.sleep(5)
    login.click()
    time.sleep(2)
    driver.switch_to.frame('jPopFrame_content')
    userID = driver.find_element_by_id('userName')
    userID.send_keys(usernamestr)

    password = driver.find_element_by_id('password')
    password.send_keys(passwordstr)

    loginagain = driver.find_element_by_id('bp_login')
    loginagain.click()

    print('test1')
    time.sleep(420)
    print('test2')
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.default_content()
    print('test3')
    logout = driver.find_element_by_id('loginContainer')
    logout.click()
    return

#Burner Account #1
# loginfunction('nide1011', 'D8WhZoUi')
# loginfunction('sourapples101', 'D8WhZoUi')
# loginfunction('nide1012', 'wDKLND6w')
# loginfunction('nide1013', 'wDKLND6w')
# loginfunction('nide1014', 'wDKLND6w')
# loginfunction('nide1015', 'wDKLND6w')
# loginfunction('nide1016', 'wDKLND6w')
# loginfunction('nide1017', 'wDKLND6w')
# loginfunction('nide1018', 'wDKLND6w')
# loginfunction('nide1019', 'wDKLND6w')
# loginfunction('nide1020', 'wDKLND6w')
# loginfunction('nide1021', 'wDKLND6w')
# loginfunction('nide1022', 'wDKLND6w')
# loginfunction('nide1023', 'wDKLND6w')
# loginfunction('nide1024', 'wDKLND6w')
# loginfunction('nide1025', 'wDKLND6w')
# loginfunction('nide1026', 'wDKLND6w')
# loginfunction('nide1027', 'wDKLND6w')
# loginfunction('nide1028', 'wDKLND6w')
# loginfunction('nide1029', 'wDKLND6w')
loginfunction('nide1030', 'wDKLND6w')
loginfunction('nide1031', 'wDKLND6w')
loginfunction('nide1032', 'wDKLND6w')
loginfunction('nide1033', 'wDKLND6w')
loginfunction('nide1034', 'wDKLND6w')












