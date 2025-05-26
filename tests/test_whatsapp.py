import pytest
from playwright.sync_api import Page

@pytest.mark.regression
def test_contact_form_submission(page: Page):
    page.goto("https://web.whatsapp.com/")
    page.wait_for_timeout(5000)

    page.get_by_text("Log in with phone number").click()

    page.locator("svg.x50qr9i.x1iffjtl").click(force=True)
    page.locator("#wa-popovers-bucket").get_by_role("textbox").fill("91")
    page.locator("[aria-label='Selected country: India. Click to select a different country.']").click()

    page.locator('[aria-label="Type your phone number."]').fill("916379129773")
    page.get_by_text("Next").click()
    
   
    page.wait_for_timeout(30000)  
    
    page.locator("[aria-label='Search input textbox']").fill("Pranesh")
    page.keyboard.press("Enter")
    page.wait_for_timeout(4000)
    
    page.get_by_title("Pranesh FSSA").click(force=True)
    print("Pranesh clicked sucessfully")
    page.get_by_role("textbox").fill("Hello Pranesh")
    print("Message Enter sucessfully")
    page.keyboard.press("Enter")
    
