from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    
    # Create context with no fixed viewport → lets window size be max
    context = browser.new_context(no_viewport=True)  # THIS is the key
    page = context.new_page()
    
    page.goto("https://auth.scalekit.com")
    print("Title:", page.title())
    
    time.sleep(5)
    print("Page launch successfully")
        
    emails_to_test = [
    "", "usergmail.com", "@gmail.com", "user@", "user@@gmail.com",
    "user @gmail.com", "user@ gmail.com", "user..name@gmail.com",
    "user.@gmail.com", "user+test@gmail.com", "user@gmail.x",
    "user@gmail.com<script>", "üser@gmail.com"
    ]
    
    page.locator("span", has_text= "Continue with Google").click()
    time.sleep(1)
    page.go_back()
    
    page.locator("a", has_text="Start for free").click()
    time.sleep(2)
    page.locator("a", has_text="Login").click()
    time.sleep(2)
    
    for email in emails_to_test:
        page.locator('[name="email"]').fill(email)
        page.locator("button.relative.button.button--variant_solid.button--size_md.button--color_sk_primary.w-full").click()
        time.sleep(2)
        page.reload()
    
    
    
    