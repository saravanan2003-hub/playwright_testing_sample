
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    # Create context with no fixed viewport → this makes it full screen
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://www.youtube.com/")
    print("Title:", page.title())

    time.sleep(5)
    print("Page launch successfully")

    # Type the search query
    page.locator("[name='search_query']").fill("trending songs")
    print("Input Entered Successfully")
    page.keyboard.press("Enter")

    time.sleep(10)  # Wait for search results to load


    
    thumbnails = page.locator("ytd-thumbnail.style-scope.ytd-video-renderer")
    count = thumbnails.count()
    print("Total thumbnails found:", count)

    for i in range(min(5, count)):
        
        # Refetch the thumbnail every loop (DOM might reload)
        page.locator("ytd-thumbnail.style-scope.ytd-video-renderer").nth(i).click()
        time.sleep(3)
        
        subscriber = page.locator("yt-formatted-string.style-scope.ytd-video-owner-renderer").nth(0).inner_text()
        print(subscriber)
        
        # likes = page.locator('button[title="I like this"]').first.inner_text()
        # print(likes)
        
        dislike = page.locator("div.yt-spec-touch-feedback-shape.yt-spec-touch-feedback-shape--touch-response").nth(0).inner_text()
        if dislike == "" :
            print("dislike :", 0)
        else:
            print("dislike:" ,dislike)
        
        description = page.locator("div#description").first.inner_text()
        print(description)

       
        
            
        
        
        

        
        

        page.go_back(wait_until="domcontentloaded")
        page.wait_for_selector("ytd-thumbnail.style-scope.ytd-video-renderer")
        time.sleep(3)
       
   

    browser.close() 