# WhatsApp Channel Automation Feed RSS

🚀 **WhatsApp Channel Automation Feed RSS** is a Selenium-based Python script designed to automate content distribution across multiple WhatsApp channels. This tool checks Feed RSSs from various Feed RSSs from blogs and sends updates directly to designated WhatsApp channels. The script is ideal for content creators, news distributors, and digital marketers who want to streamline their content-sharing process.

### Features

- **Automated Feed Checking:** Continuously monitors Feed RSSs for new content.
- **WhatsApp Integration:** Automatically sends updates to specified WhatsApp channels.
- **Easy Setup:** Simple installation and setup process.
- **Customizable:** Easily extend the script to include more feeds or customize message formats.

### How It Works

1. **Initialize WhatsApp Web:** The script launches a Chrome browser session, where you need to log in to WhatsApp Web.
2. **Feed Monitoring:** It monitors the specified Feed RSSs for any new content.
3. **Channel Navigation:** The script navigates to the appropriate WhatsApp channel.
4. **Message Sending:** Upon detecting new content, it formats and sends the message to the channel.

### Requirements

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- Feedparser
- A WhatsApp account with channel admin privileges

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/whatsapp-channel-automation.git
   cd whatsapp-channel-automation
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

### Usage

- After running the script, a Chrome window will open, and you will be prompted to log in to WhatsApp Web.
- Once logged in, the script will start monitoring the Feed RSSs and sending messages to your configured WhatsApp channels automatically.

### Contribution

Feel free to fork this repository, submit issues, or propose new features. Contributions are welcome!

### Donations

If you find this project useful and want to support its development, consider making a donation. Your contributions will help cover hosting costs, continuous development, and future improvements.

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/BX8W8QZ4TECTS)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-orange.svg)](https://www.buymeacoffee.com/carlosgha)

<a href="https://www.buymeacoffee.com/carlosgha" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

Thank you for your support!
