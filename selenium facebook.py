#pip install selenium 
#pip install webdriver-manger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def open_Browser():

    # اختيار متصفح جوجل كروم لتنفيذ الكود ويمكن اختيار اي متصفح اخر  

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

    #===========================================================================
    # هنا هيفتح موقع الفيسبوك
    driver.get("https://www.facebook.com")
    # لو النت ضعيف بستخدم الكود ده عشان يتأخر 10 ثواني قبل ما ينفذ الامر التالي
    driver.implicitly_wait(10) 
    #===========================================================================
    # اضغط على مكان الايميل واكتب فيه الاكونت 
    send_your_mail = driver.find_element(By.NAME, "email")
    # هتكتب هنا الاكونت
    send_your_mail.send_keys("7777777saw7777777@gmail.com")
    #===========================================================================
    driver.implicitly_wait(10)# برضه هنا بقولو انتظر 10 ثواني
    #===========================================================================
    # هنا هيضغط عل مكان الباسورد 
    send_your_password = driver.find_element(By.NAME, "pass")
    # ويكتب فيه الباسورد الخاص بك
    send_your_password.send_keys("MS_MOHAMED_MS2001")
    #===========================================================================
    driver.implicitly_wait(10)
    #===========================================================================
    #اوجد مكان زر تسجيل الدخول
    login_to_facebook = driver.find_element(By.NAME, "login")
    # اضغط على زر تسجيل الدخول
    login_to_facebook.click()
    #انتظر 30 ثانية 
    driver.implicitly_wait(30)
    #===========================================================================
    # هنا هيفتح الفيسبوك ويدور على مكان انشاء بوست
    post_text_area = driver.find_element(By.CSS_SELECTOR, '.x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xmjcpbm.x107yiy2.xv8uw2v.x1tfwpuw.x2g32xy.x78zum5.x1q0g3np.x1iyjqo2.x1nhvcw1.x1n2onr6.xt7dq6l.x1ba4aug.x1y1aw1k.xn6708d.xwib8y2.x1ye3gou .xi81zsa.x1lkfr7t.xkjl1po.x1mzt3pk.xh8yej3.x13faqbe span')
    # اضغط على انشاء بوست
    post_text_area.click()
    #===========================================================================
    driver.implicitly_wait(10)
    #===========================================================================
    # هيحدد  المكان ويبعتله النص المكتوب
    send_post = driver.find_element(By.CSS_SELECTOR, '.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x9f619.x1lliihq.x5yr21d.xh8yej3.notranslate')
    # هنا انت بتحدد النص اللي هتكتبه في البوست
    send_post.send_keys("فلسطين حرة")
    #===========================================================================
    # اوجد مكان زر نشر
    click_post = driver.find_element(By.CSS_SELECTOR, '.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1r1pt67')
    # اضغط عليه حتى يتم انشاء البوست
    click_post.click()


open_Browser()
