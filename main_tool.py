import tkinter as tk
import json
import time
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By

def on_submit():
    code = code_entry.get()

    if code == "":
        messagebox.showerror("Error", "Vui lòng nhập giftcode!")
    else:
        try:
            code = code_entry.get()
            driver.find_element(By.ID, "redemptionCode").send_keys(code)
            driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/div/div[1]/section[4]/div/form/div[1]/div[2]/button").click()
        except:
            messagebox.showerror("Error", "Vui lòng truy cập vào trang mua hàng trước khi nạp giftcode!")

def on_exit():
    driver.quit()
    root.quit()

driver = webdriver.Firefox()

try:
    extension_path = "D:\Projects\selenium_tool\proxy_toggle-1.2.1.xpi"
    driver.install_addon(extension_path)
except Exception as e:
    print(e)

# Open Ebay
driver.get("https://www.ebay.com/")

try:
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

except Exception as e:
   print(e)

time.sleep(2)
driver.get('https://www.ebay.com/')

# Create window for input
root = tk.Tk()
root.title("Nhập Giftcode")
root.geometry("400x150")

# Display label
login_label = tk.Label(root, text="Hãy tạo trang mua hàng sau đó nhập giftcode bạn muốn thêm") 
login_label.pack(pady=10)

# Create input field
code_entry = tk.Entry(root, width=50)
code_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Confirm button
submit_button = tk.Button(button_frame, text="Xác nhận", command=on_submit)
submit_button.pack(side=tk.LEFT, padx=15)

# Exit button
exit_button = tk.Button(button_frame, text="Thoát", command=on_exit)
exit_button.pack(side=tk.LEFT, padx=15)

# Run
root.mainloop()