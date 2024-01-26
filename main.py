import tkinter as tk
import time
import os
from dotenv import load_dotenv
from tkinter import messagebox
from selenium.webdriver.common.by import By
from set_proxy import get_chromedriver

load_dotenv()

def main():
    global driver, root, code_entry, input_window

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

    def on_exit(state):
        if state == 2:
            driver.quit()
            root.quit()
        elif state == 1:
            input_window.quit()

    def open_web():
        global driver, root, code_entry, input_window

        proxy = proxy_entry.get()
        cookie_string = cookie_entry.get()
        link = link_entry.get()

        if not proxy or not cookie_string or not link:
            messagebox.showerror("Error", "Vui lòng điền đầy đủ thông tin proxy, cookie và link.")
            return

        # Your proxy parsing logic (e.g., extract ip, port, username, password)
        proxy_parts = proxy.split(':')
        proxy_host = proxy_parts[0]
        proxy_port = proxy_parts[1]
        proxy_user = proxy_parts[2] if len(proxy_parts) > 2 else ''
        proxy_pass = proxy_parts[3] if len(proxy_parts) > 3 else ''

        # Save information to .env file
        with open('.env', 'w') as env_file:
            env_file.write(f"COOKIE={cookie_string}\n")
            env_file.write(f"LINK={link}\n")
            env_file.write(f"PROXY_HOST={proxy_host}\n")
            env_file.write(f"PROXY_PORT={proxy_port}\n")
            env_file.write(f"PROXY_USER={proxy_user}\n")
            env_file.write(f"PROXY_PASS={proxy_pass}\n")

        # Hide the input window
        input_window.withdraw()

        # Continue with the rest of your code
        driver = get_chromedriver(use_proxy=True)

        # Open Ebay
        driver.get(link)
        time.sleep(5)

        driver.delete_all_cookies()

        # Tạo danh sách các cặp "name" và "value" từ chuỗi cookie
        cookie_pairs = [pair.split("=") for pair in cookie_string.split(";")]

        # Thêm mỗi cặp "name" và "value" vào trình duyệt
        for pair in cookie_pairs:
            cookie = {"name": pair[0].strip(), "value": pair[1].strip()}
            driver.add_cookie(cookie)

        time.sleep(2)
        
        driver.get(link)


        # Create main window for input
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
        exit_button = tk.Button(button_frame, text="Thoát", command=lambda: on_exit(2))
        exit_button.pack(side=tk.LEFT, padx=15)

        # Run
        root.mainloop()

    # Create window for input
    input_window = tk.Tk()
    input_window.title("Nhập thông tin trước khi mở web")
    input_window.geometry("400x250")

    proxy_label = tk.Label(input_window, text="Proxy (ip:port:username:pass):")
    proxy_label.pack(pady=5)
    proxy_entry = tk.Entry(input_window, width=50)
    proxy_entry.pack(pady=5)

    cookie_label = tk.Label(input_window, text="Cookie(header string):")
    cookie_label.pack(pady=5)
    cookie_entry = tk.Entry(input_window, width=50)
    cookie_entry.pack(pady=5)

    link_label = tk.Label(input_window, text="Link sản phẩm:")
    link_label.pack(pady=5)
    link_entry = tk.Entry(input_window, width=50)
    link_entry.pack(pady=5)

    submit_input_button = tk.Button(input_window, text="Xác nhận", command=open_web)
    submit_input_button.pack(side=tk.LEFT, padx=(80,0), pady=5)
    exit_button = tk.Button(input_window, text="Thoát", command=lambda: on_exit(1))
    exit_button.pack(side=tk.RIGHT, padx=(0, 80), pady=5)  

    # Run input window
    input_window.mainloop()

if __name__ == "__main__":
    main()
