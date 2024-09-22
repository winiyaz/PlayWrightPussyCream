# KAG Directory 

1. This directory will have the work in the form of jupyter notebooks. 
2. Notebooks are form KAGGLE pushed here 

# Working Code wiht Extras 

```py 
import os 
import asyncio
from playwright.async_api import async_playwright, Playwright

url = "https://www.coingecko.com/"
user_agent = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"

async def fetch_and_save_page_content():

    # Defining the actual aysnc playwright function
    async with async_playwright() as playwright:
        firefox = playwright.firefox # or "chromium" or "webkit".
        browser = await firefox.launch()

        # Context defines the actions to be performed
        context = await browser.new_context(record_video_dir="panties/" , 
                                            user_agent=user_agent)
        page = await context.new_page()
        await page.goto(url)
        
        # Capture the page content
        content = await page.content()
        
        # Write the page content to a file
        with open('cg2.txt', "w", encoding="utf-8") as file:
            file.write(content)
        with open('cg2.html', "w", encoding="utf-8") as file:
            file.write(content)
        
        # Take ScreenShot of page also 
        await page.screenshot(path="cg_screenshot.png", full_page=True)
        
        # Close the browser
        await browser.close()
        
        

# Add the task to the current loop and wait for it to complete
loop = asyncio.get_event_loop()
task = loop.create_task(fetch_and_save_page_content())
loop.run_until_complete(task)

# view contents 
os.system("ls -al")
os.system("cat cg2.txt")
os.system("")
```

- Note this is required when trying to run playwright inside jupyter , since jupyter is already a running an event loop. You have to make a nested loop , and wait for it to finish