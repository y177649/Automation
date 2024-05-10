from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# ログ設定
logging.basicConfig(level=logging.INFO)

# Chromeオプションの設定
options = Options()
# options.add_argument('--headless')  # 必要に応じてヘッドレスモード
options.add_argument('--no-sandbox')  # 必要に応じてセキュリティ設定を解除

# WebDriver Managerで最新のChromeDriverを取得
logging.info("Setting up ChromeDriver...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# サイトにアクセス
logging.info("Accessing the website...")
driver.get("https://kenkoooo.com/atcoder/#/table/")

# ユーザーID入力ボックスが表示されるまで最大10秒待つ
logging.info("Waiting for user ID input box to load...")
user_id_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user_id"))
)

# ユーザーID入力ボックスに値を入力
logging.info("Entering user ID...")
user_id_box.send_keys("y177649")

# 数秒待ってからブラウザを閉じる
logging.info("Sleeping for 3 seconds before closing the browser...")
time.sleep(3)
#driver.quit()

logging.info("Automation complete.")
