from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 로또 아이디/비밀번호 입력
USER_ID = ''
USER_PW = ''

try:
    # 사이트 열기
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.dhlottery.co.kr/common.do?method=main")
    driver.maximize_window()
    time.sleep(1)

    # 팝업 창 닫기
    handles = driver.window_handles
    main_handle = driver.current_window_handle
    for handle in handles:
        if handle != main_handle:
            driver.switch_to.window(handle)
            driver.close()
    driver.switch_to.window(main_handle)

    # 로그인 페이지로 이동
    driver.find_element(By.CLASS_NAME, "log").click()
    time.sleep(1)

    # 아이디, 비밀번호 입력
    driver.find_element(By.NAME, "userId").send_keys(USER_ID)
    driver.find_element(By.NAME, "password").send_keys(USER_PW)
    time.sleep(1)

    # 로그인 버튼 클릭
    driver.find_element(By.XPATH, "//div/a[text()='로그인']").click()
    time.sleep(2)

    # 다시 팝업 창 닫기
    handles = driver.window_handles
    main_handle = driver.current_window_handle
    for handle in handles:
        if handle != main_handle:
            driver.switch_to.window(handle)
            driver.close()
    driver.switch_to.window(main_handle)

    # 번호 선택 페이지로 이동
    driver.get("https://ol.dhlottery.co.kr/olotto/game/game645.do")
    time.sleep(2)

    # 자동 선택 1번
    driver.find_element(By.ID, "num2").click()
    time.sleep(1)
    driver.find_element(By.ID, "btnSelectNum").click()
    time.sleep(1)

    # 자동 선택 2번
    driver.find_element(By.ID, "num2").click()
    time.sleep(1)
    driver.find_element(By.ID, "btnSelectNum").click()
    time.sleep(1)
    
    # 자동 선택 3번
    driver.find_element(By.ID, "num2").click()
    time.sleep(1)
    driver.find_element(By.ID, "btnSelectNum").click() 
    time.sleep(1)
    
    # 자동 선택 4번
    driver.find_element(By.ID, "num2").click()
    time.sleep(1)
    driver.find_element(By.ID, "btnSelectNum").click()
    time.sleep(1)

    # 구매하기 버튼 클릭
    driver.find_element(By.ID, "btnBuy").click()
    time.sleep(2)

    # 구매 확인
    driver.find_element(By.XPATH, "//*[@id='popupLayerConfirm']/div/div[2]/input[1]").click()
    time.sleep(3)

    print(" 자동 2개 로또 구매 완료!")

except Exception as err:
    print("오류 발생:", err)
