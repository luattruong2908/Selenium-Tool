import tkinter as tk
import time
import os
from dotenv import load_dotenv
from tkinter import messagebox
from selenium.webdriver.common.by import By
from set_proxy import get_chromedriver

load_dotenv()

def main():
    def on_submit():
        code = code_entry.get()

        if code == "":
            messagebox.showerror("Error", "Vui lòng nhập giftcode!")
        else:
            try:
                # Bypass trick here
                # ...

                # Click addgift
                driver.find_element(By.ID, "redemptionCode").send_keys(code)
                driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/div/div[1]/section[4]/div/form/div[1]/div[2]/button").click()
            except:
                messagebox.showerror("Error", "Vui lòng truy cập vào trang mua hàng trước khi nạp giftcode!")

    def on_exit():
        driver.quit()
        root.quit()

    driver = get_chromedriver(use_proxy=True)
    link = os.getenv("LINK")

    # Open Ebay
    driver.get(link)
    time.sleep(5)

    driver.delete_all_cookies()
    cookie_string = os.getenv("COOKIE")

    # Tạo danh sách các cặp "name" và "value" từ chuỗi cookie
    cookie_pairs = [pair.split("=") for pair in cookie_string.split(";")]

    # Thêm mỗi cặp "name" và "value" vào trình duyệt
    for pair in cookie_pairs:
        cookie = {"name": pair[0].strip(), "value": pair[1].strip()}
        driver.add_cookie(cookie)

    time.sleep(2)
    driver.get(link)

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

if __name__ == "__main__":
    main()