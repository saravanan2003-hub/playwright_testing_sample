from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://www.google.com")
    print("Title:", page.title())

    try:
        page.locator("button:has-text('Accept all')").click(timeout=3000)
    except:
        pass

    page.locator("textarea[name='q']").fill("whatsapp web")
    page.keyboard.press("Enter")

    page.wait_for_selector("a:has-text('WhatsApp Web')", timeout=40000)
    page.locator("a:has-text('WhatsApp Web')").first.click()
    print("WhatsApp Web link clicked successfully!")

    button = page.get_by_text('Log in with phone number')
    time.sleep(6)
    button.click(force=True)
    print("Clicked login with phone number!")
    
    time.sleep(4)
    
    # Click the country code dropdown (svg)
    page.locator("svg.x50qr9i.x1iffjtl").click(force=True)
    print("Country dropdown clicked")
    
   #type country code 
    page.locator("#wa-popovers-bucket").get_by_role("textbox").fill("91")
    time.sleep(2)
    
    page.get_by_label("Selected country: India.").get_by_role("button", name="🇮🇳 India").click()

    # Fill phone number
    page.locator("input[aria-label='Type your phone number.']").fill("6379129773")
    print("Phone number entered")
    
    page.get_by_text("Next").click()

    time.sleep(10)
    browser.close()