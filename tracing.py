from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # ✅ Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()
    page.goto("https://example.com")

    # Perform some actions (you can add more steps)
    page.click("text=More information")  # if exists

    # ✅ Stop tracing and save to file
    context.tracing.stop(path="trace.zip")

    print("✅ Trace saved as trace.zip")

    browser.close()
