from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    
    # Create context with no fixed viewport → lets window size be max
    context = browser.new_context(no_viewport=True)  # THIS is the key
    page = context.new_page()
    
    page.goto("https://link-upp.netlify.app")
    print("Title:", page.title())

    page.locator("#Login-Email").fill("saranamas2@gmail.com")
    page.locator("#Login-password").fill("Sara@123456")
    page.locator("#eye").click()
    page.locator("#eye").click()
    
    page.locator("#login").click()
    print("Login Successfully")

    page.wait_for_url("https://link-upp.netlify.app/pages/homepage.html", timeout=10000)
    time.sleep(10)

    page.locator("#comment-RPguqhC210wlfZtt5QEW").dblclick()
    print("comment box open Successfully")
    page.locator("#xmarkComment").click()
    print("comment box close successfully")
    time.sleep(10)

    # page.locator("#comment-RPguqhC210wlfZtt5QEW").click()
    # page.locator("#commentText").fill("coorg is very nice place to visit")
    # print("comment Enter successfully ")
    # page.locator("#CommentSend").click()
    # print("comment send successfully ")

    time.sleep(6)
    
    def handle_dialogs(dialog):
        print("Dialog message:", dialog.message)
        assert dialog.type == "confirm"
        dialog.accept()  # or dialog.dismiss() for Cancel
    
    page.locator("#Logout").click()
    print("Logout button clicked")
    time.sleep(4)
    
    page.on("dialog", handle_dialogs)
    
    
    time.sleep(4)
    
    browser.close()
