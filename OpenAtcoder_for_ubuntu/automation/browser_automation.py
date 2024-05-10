from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# WebDriverを初期化して、Webページを開く
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://kenkoooo.com/atcoder/#/table/")

# JavaScriptコードを実行してボックスに "y177649" を入力
js_code = """
var element = document.querySelector('[your-selector]'); // 実際のCSSセレクタを指定
element.value = 'y177649';
"""
driver.execute_script(js_code)
