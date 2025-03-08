from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# URL router
login_url = 'http://192.168.1.1/cgi-bin/index2.asp'

# Kombinasi username dan password
username = 'admin'
password = 'admin'

# Setup Firefox WebDriver
options = Options()
options.binary_location = '/usr/bin/firefox'  # Adjust the path if necessary
service = Service('/usr/local/bin/geckodriver')  # Use the correct path
driver = webdriver.Firefox(service=service, options=options)

try:
    # Buka halaman login
    driver.get(login_url)
    
    # Tunggu sampai halaman sepenuhnya dimuat
    time.sleep(3)
    
    # Temukan field username dan password
    username_field = driver.find_element(By.NAME, "username")  # Ganti "username" dengan nama field yang sesuai
    password_field = driver.find_element(By.NAME, "password")  # Ganti "password" dengan nama field yang sesuai
    
    # Isi username dan password
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Submit form
    password_field.send_keys(Keys.RETURN)
    
    # Tunggu beberapa detik untuk proses login dan redirect
    time.sleep(5)
    
    # Cek URL setelah login
    print("URL setelah login:", driver.current_url)
    
    # Ambil konten halaman setelah login
    page_content = driver.page_source
    print("Isi halaman setelah login:", page_content)
    
    # Jika perlu, lakukan interaksi lebih lanjut dengan halaman dashboard
    # Contoh: Klik tombol reset Wi-Fi
    reset_button = driver.find_element(By.ID, "reset_wifi_button")  # Ganti dengan ID yang sesuai
    reset_button.click()
    
    # Tunggu konfirmasi reset
    time.sleep(3)
    
    # Terima alert konfirmasi
    alert = driver.switch_to.alert
    alert.accept()
    
    print("Wi-Fi berhasil direset.")
    
except Exception as e:
    print("Terjadi kesalahan:", e)
    # Debug: Print page source atau ambil screenshot
    print(driver.page_source)
    driver.save_screenshot("error.png")
    
finally:
    # Tutup browser
    driver.quit()