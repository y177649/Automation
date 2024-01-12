from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chromeドライバのパス
webdriver_path = "C:\\Users\\y177649\\Downloads\\chromedriver-win64\\chromedriver.exe"

# Chromeオプションの設定
options = Options()

# Chromeドライバサービスの設定
service = Service(webdriver_path)

# Chromeドライバの起動
driver = webdriver.Chrome(service=service, options=options)

# ウェブサイトにアクセス
driver.get("https://kenkoooo.com/atcoder/#/table/")

# 要素が表示されるまで最大10秒待つ
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_id")))

# 要素の検索とテキストの入力
text_box = driver.find_element(By.ID, "user_id")
text_box.send_keys("y177649")

# スクリプトを終了する前に一定時間待つ（必要に応じて）
time.sleep(86400)

# ブラウザを閉じる（長時間待機後に必要な場合）
driver.quit()