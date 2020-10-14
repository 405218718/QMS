from selenium import webdriver #导入一个可以调用浏览器的模块
import time                   #导入time模块 直接导入无需安装
import datetime               #获取当前时间


#打开Chrome,右键点击运行(快捷键ctrl+shift+F10)
driver = webdriver.Chrome()
driver.set_window_size(1280, 960)  #设置屏幕分辨率
driver.implicitly_wait(0.5)     #时间太快加个等待时间
print('start webdriver')
driver.get("http://www.jd.com")  #发送请求
print('get web in')

driver.find_element_by_link_text('你好，请登录').click()
time.sleep(10)          #休息5-10秒 即扫码过程
print('已登录！')

driver.get('https://item.jd.com/100006607839.html')
buy_time = '2020-09-03 16:00:00'  #设置秒杀时间
print("buy_time" + buy_time + "等待时间到达...")

while True:      #条件不满足时，一直循环下去
    now = datetime.datetime.now()  #获取当前实时时间
    print('当前北京时间: {}'.format(now))
    # 3.监控商品秒杀时间
    if now.strftime('%Y-%m-%d %H:%M:%S') == buy_time:
        #假如现在时间等于设定的购买时间，则提交订单
    # 4.提交订单
        driver.find_element_by_id('InitCartUrl').click() #加入购物车
        driver.find_element_by_id('GotoShoppingCart').click() #去购物车结算
        print("-----已提交订单-----")
        break        #条件满足就退出循环
    time.sleep(0.5)