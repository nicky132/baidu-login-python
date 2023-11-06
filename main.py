import time

from selenium import webdriver
import base64
import json
import requests
# 1.导入ActionChinas类
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.common.devtools.v118 import browser
from selenium.webdriver.remote.webelement import WebElement


# 64位编码流
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


# 第一步：打开浏览器，访问登录页面
# 1.1启动浏览器
driver = webdriver.Chrome()
# 1.2 打开后台监控平台的登录页面
driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//a[@name="tj_login"]').click()
# browser.find_element(by=By.XPATH, value="//a[@name='tj_login']").click()
# browser.find_element(by=By.XPATH, value="//a[@name='tj_login']").click()
driver.find_element("id", "s-top-loginbtn").click()
time.sleep(2)
# driver.quit()

# # 第二步：输入账号、密码
# # 输入账号
driver.find_element("id", "TANGRAM__PSP_11__userName").send_keys('15733269638')
# # 输入密码
driver.find_element("id", "TANGRAM__PSP_11__password").send_keys('dsfdh')

# time.sleep(5)
# driver.quit()

#
# # 第三步：识别验证码图片中的内容
# # 3.1截取网站中的验证码图片
# # 3.1.1、对当前网页进行截图,并保存为page.png的图片
# driver.save_screenshot('page.png')
# # 3.1.2  定位页面的图片元素，
# pic_ele = driver.find_element_by_xpath('//div//img')
# # 3.1.3 获取图片在页面中的坐标位置(此处计数位置要考虑屏幕的缩放比例)
# rec = pic_ele.rect
# # 验证码左边界位置
# left = rec['x'] * 1.50
# # 验证码上边界位置
# top = rec['y'] * 1.50
# # 验证码右边界位置
# right = (rec['x'] + rec['width']) * 1.50
# # 验证码下边界位置
# button = (rec['y'] + rec['height']) * 1.50
# location = (left, top, right, button)
#
# # 3.1.4通过验证码的位置进行截图
# page = Image.open('page.png')
# code_pic = page.crop(location)
# # 3.1.5 保存截取下来的验证码为code.png的图片
# code_pic.save('code.png')
#
# # 3.2 调用验证码识别的方法去识别
# result = base64_api(uname='', pwd='', img='code.png', typeid=11)
# print("识别的结果是：", result)
#
# # 第四步：输入识别之后的结果，点击登录
# # 4.1 输入计算结果之后的验证码
# driver.find_element_by_xpath('//input[@placeholder="验证码"]').send_keys(result)
#
# # 4.2点击登录按钮
# driver.find_element_by_xpath('//button[@type="button"]').click()
# driver.find_element("id", "TANGRAM__PSP_11__smsIsAgree").click()
# driver.find_element(By.XPATH, ".//input[@name='smsIsAgree']").click()
# driver.find_element(by=By.XPATH, value="//input[@class='pass-checkbox-input pass-checkbox-isAgree']").click()
# driver.find_element_by_xpath("//input[@class='pass-checkbox-input pass-checkbox-isAgree' and @id='TANGRAM__PSP_11__smsIsAgree']").click()
# driver.find_element(by=By.XPATH, value="//input[@class='pass-checkbox-input pass-checkbox-isAgree' and "
#                                        "@id='TANGRAM__PSP_11__smsIsAgree']").click()
# ele  = driver.find_element(by=By.XPATH, value="//input[@class='pass-checkbox-input pass-checkbox-isAgree']")
# driver.execute_script("arguments[0].click();", ele)

# driver.find_element(By.XPATH, "//*[text()='阅读并接受']").click()

# time.sleep(2)
# ele = driver.find_element("id", "TANGRAM__PSP_11__smsIsAgree")
# print(ele)
# time.sleep(5)
# # # 2.实例化ActionChinas对象
# # actions = ActionChains(driver)
# # # 3.执行鼠标操作，如点击元素
# # actions.click(ele).perform()
# ele.click()


driver.find_element(By.XPATH,'//label[@for="TANGRAM__PSP_11__isAgree"]').click()
driver.find_element(By.XPATH,'//input[@id="TANGRAM__PSP_11__submit"]').click()

time.sleep(1)

flyButton = driver.find_element(By.XPATH,'//div[@class="passMod_slide-grand"]')
ActionChains(driver).move_to_element(flyButton).perform()

flyButton_div = driver.find_element(By.XPATH,'//div[@class="passMod_spin-footer"]')
#
print(flyButton_div.size['width'], flyButton_div.size['height'])
#
huakuia = ActionChains(driver)
huakuia.click_and_hold(flyButton).perform()
# #1、
# huakuia.move_by_offset(flyButton_div.size['width'], 0).perform()
# #
# huakuia.release()

#2、
x = flyButton_div.size['width']
i = 0
step = 8
while i < x:
    i = i + step
    huakuia.move_by_offset(step, 0).perform()
    time.sleep(3)

huakuia.release()



# try:
#     dr = webdriver.Chrome()
#     dr.get("https://www.baidu.com")
#     dr.implicitly_wait(5)
#     dr.find_element_by_xpath('//span[@class="soutu-btn"]').click()
#     ele = dr.find_element_by_xpath('//div[@class="upload-wrap"]/input[@type="file"]')
#     # 2.实例化ActionChinas对象
# 	actions = ActionChains(dr)
# 	# 3.执行鼠标操作，如点击元素
#     actions.click(ele).perform()
#     time.sleep(3)
#     send_keys(keys=r'D:\api_test.jpg')
#     send_keys(keys='{ENTER}')
#     time.sleep(30)
# except Exception as e:
#     raise e
# finally:
#     dr.quit()


# element = driver.find_element("id", "TANGRAM__PSP_11__smsSubmit")
# webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

# 定位全部复选框，然后进行循环点击
# t = driver.find_element(By.CSS_SELECTOR,'input[class="pass-checkbox-input pass-checkbox-isAgree"]')
# for i in t:
#     i.click()
#     time.sleep(2)

# time.sleep(2)
# driver.find_element("id", "TANGRAM__PSP_11__smsSubmit").click()
#
time.sleep(2)
# driver.quit()
