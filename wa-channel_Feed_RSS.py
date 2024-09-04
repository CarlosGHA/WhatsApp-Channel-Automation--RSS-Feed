# WhatsApp Channel Automation
# This Selenium-based script checks all the feeds from Promecal's newspapers, launches WhatsApp Web, and automatically navigates through the channels,
# checking if there are new items in the feeds. When there is new content, the news is sent to the channel, and so on for all channels.

# Based on the script architecture from https://github.com/simbon/wa-channel
# Fork made by https://github.com/CarlosGHA/wa-channel_Feed_RSS
# MAY I HAVE A COFFE? FEEL FREE TO DONATE AT: buymeacoffee.com/carlosgha

import feedparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import sys

# Configuration of RSS feeds and WhatsApp channels
FEEDS_AND_CHANNELS = [
    {'feed_url': 'https://www.YourBlog.com/RSS/V5/Blog1.xml', 'channel_name': 'Blog 1'},
    {'feed_url': 'https://www.YourBlog.com/RSS/V5/Blog2.xml', 'channel_name': 'Blog 2'},
    # Add more feeds and channels here...
]

CHECK_INTERVAL = 60  # Check interval in seconds
CHANNEL_SEARCH_TIMEOUT = 30  # Maximum wait time to search for the WhatsApp channel in seconds
SEND_MESSAGE_DELAY = 10  # Delay in seconds before sending a message after typing it

# Function to print text with animation
def print_with_animation(text, delay=0.01):
    """Prints text character by character with a given delay for animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ensures the message ends on a new line

def print_startup_message():
    startup_message = """
*******************************************************
*                                                     *
*    🚀 WhatsApp Channel Automation                   *
*                                                     *
*    This Selenium-based script checks all the feeds  *
*    from your website's blogs, launches WhatsApp Web,*
*    and automatically navigates through the channels,*
*    checking if there are new items in the feeds.    *
*    When new content is found, it sends the news to  *
*    the channel, and so on for all channels.         *
*                                                     *
*    #Based on the script architecture                *
*    https://github.com/simbon/wa-channel             *
*                                                     *
*    #Fork made by                                    *
*    https://github.com/CarlosGHA/wa-channel_Feed_RSS *
*                                                     *
*    Instructions:                                    *
*    1. Once a new window opens in your terminal,     *
*       accept Chrome as the default browser.         *
*    2. A WhatsApp Web window with a QR code will     *
*       appear, which you must scan with the phone    *
*       that manages the WhatsApp channels you want   *
*       to automate.                                  *
*    3. After logging into WhatsApp and Chrome shows  *
*       the app interface, press ENTER.               *
*    4. The program will start the automation. Keep   *
*       the console open.                             *
*                                                     *
*    WARNING:                                         *
*    This version may fail. It is a basic automation  *
*    not intended as a definitive solution.           *
*    WhatsApp does not officially support this        *
*    third-party automation and it may be against     *
*    Meta's official usage guidelines. Use this tool  *
*    at your own risk.                                *
*                                                     *
*                                                     *
*     MAY I HAVE A COFFE?                             *
*     Feel free to donate at:                         *
*     buymeacoffee.com/carlosgha                      *
*                                                     *
*                                                     *

*******************************************************
"""
    print_with_animation(startup_message, delay=0.01)

# Initialize the Chrome browser
def initialize_browser():
    try:
        chrome_driver = ChromeDriverManager().install()
        driver = webdriver.Chrome(service=Service(chrome_driver))
        driver.get('https://web.whatsapp.com/')
        input("Press Enter after logging into WhatsApp Web.")
        return driver
    except Exception as e:
        print(f"Error initializing the browser: {e}")
        raise

# Initialize the channel search window only once
def initialize_channel_search(driver):
    try:
        print("Initializing channel search.")
        
        # Attempt to click the channel icon to open the search
        channel_icon_css = "span[data-icon='newsletter-unread-outline'], span[data-icon='newsletter-outline']"
        channel_icon = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, channel_icon_css))
        )
        channel_icon.click()

        # Wait and click on the search bar
        search_bar = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/p'))
        )
        search_bar.click()
        time.sleep(1)  # Short pause to ensure the search bar is ready
        
    except Exception as e:
        print(f"Error initializing channel search: {e}")
        raise

# Navigate directly to the WhatsApp channel
def navigate_to_channel(driver, channel_name):
    try:
        print(f"Navigating to channel {channel_name}")

        # Use the existing search bar to find the channel
        search_bar = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/p'))
        )
        search_bar.clear()
        search_bar.send_keys(channel_name)
        
        # Wait for the channel to appear in the results and be clickable
        channel_xpath = f"//span[@class='matched-text _ao3e' and contains(text(), '{channel_name}')]"
        channel = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, channel_xpath))
        )
        channel.click()
    except Exception as e:
        print(f"Error navigating to channel {channel_name}: {e}")
        raise

# Clear the current channel search
def clear_search(driver):
    try:
        print("Clearing current channel search.")
        clear_search_button = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[1]/div/div/div[2]/span/button'))
        )
        clear_search_button.click()
        time.sleep(2)  # Pause to ensure the search is fully cleared

        # Confirm that the search bar is empty
        search_bar = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/p'))
        )
        if search_bar.text != "":
            print("Search bar is not empty, waiting...")
            time.sleep(1)  # Additional wait if the bar is not empty
    except Exception as e:
        print(f"Error clearing search: {e}")
        raise

# Send a message via WhatsApp
def send_message(driver, message):
    try:
        textarea = WebDriverWait(driver, CHANNEL_SEARCH_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
        )
        textarea.send_keys(message)
        time.sleep(SEND_MESSAGE_DELAY)  # Wait before sending the message

        send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        send_button.click()
    except Exception as e:
        print(f"Error sending message: {e}")
        raise

# Fetch the RSS feed and return new items published today
def fetch_new_feed_items(feed_url, sent_items):
    try:
        feed = feedparser.parse(feed_url)
        new_items = []
        today = datetime.now().date()

        for entry in feed.entries:
            published_date = datetime(*entry.published_parsed[:6]).date()
            if published_date == today and entry.link not in sent_items:
                new_items.append(entry)
                sent_items.add(entry.link)

        return new_items
    except Exception as e:
        print(f"Error reading feed {feed_url}: {e}")
        return []

def process_feed(driver, feed_info, sent_items_per_feed):
    feed_url = feed_info['feed_url']
    channel_name = feed_info['channel_name']
    
    # Print the feed being checked
    print(f"Checking feed: {feed_url} for channel: {channel_name}")

    # Get new items for the current feed
    new_feed_items = fetch_new_feed_items(feed_url, sent_items_per_feed[feed_url])

    # If there are new items, navigate to the channel and send the messages
    if new_feed_items:
        try:
            # Navigate directly to the channel using the existing search bar
            navigate_to_channel(driver, channel_name)
            
            # Send a message for each new item
            for item in new_feed_items:
                message = item.link
                send_message(driver, message)
        except Exception as e:
            print(f"Error processing channel {channel_name} for feed {feed_url}: {e}")
        
        # Clear the search after sending the messages
        try:
            clear_search(driver)
        except Exception as e:
            print(f"Error clearing search after processing channel {channel_name}: {e}")

def main():
    try:
        print_startup_message()

        driver = initialize_browser()

        # Keep a set of sent items for each feed to avoid duplicates
        sent_items_per_feed = {feed['feed_url']: set() for feed in FEEDS_AND_CHANNELS}

        # Initialize the channel search only once
        initialize_channel_search(driver)

        # Infinite loop to check for new updates
        while True:
            # Process the feeds
            for feed_info in FEEDS_AND_CHANNELS:
                process_feed(driver, feed_info, sent_items_per_feed)
                time.sleep(5)  # Wait before checking the next feed

            print("Completed check of all feeds. Waiting for the next check interval.")
            time.sleep(CHECK_INTERVAL)  # Wait before checking all feeds again
    except Exception as e:
        print(f"Error in the main flow: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
