from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Chromeオプションの設定
options = Options()
options.add_argument('--headless')  # 必要に応じてヘッドレスモード

# WebDriver Managerで最新のChromeDriverを取得
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# サイトにアクセス
driver.get("https://kenkoooo.com/atcoder/#/table/")

# テスト用の要素を検索し、操作が可能か確認
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 要素が表示されるまで最大10秒待つ
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_id")))

# ユーザーID入力ボックスに値を入力
text_box = driver.find_element(By.ID, "user_id")
text_box.send_keys("y177649")

# 確認のため数秒待つ
import time
time.sleep(10)

# ブラウザを閉じる
#driver.quit()
