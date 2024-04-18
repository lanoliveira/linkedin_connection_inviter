# LinkedIn Connection Inviter

## Overview

The LinkedIn Connection Inviter is a Python script designed to automate the process of sending connection invitations to potential contacts on LinkedIn. It utilizes Selenium WebDriver to navigate LinkedIn's web interface and interact with elements such as search bars, buttons, and input fields.

## Features

- **Automated Connection Invitations:** The script automatically sends connection invitations to profiles that match specified search criteria.
- **Customizable Messages:** You can personalize the invitation messages using variables such as the recipient's name.
- **Randomized Delays:** Randomized delays between actions mimic human behavior, reducing the likelihood of triggering LinkedIn's spam detection algorithms.
- **Flexible Search Criteria:** The script allows you to define search keywords and filters to target specific profiles.

## Requirements

- Python 3.x
- Undetected Chromedriver
- Selenium WebDriver
- Python-dotenv
- LinkedIn account with Premium subscription

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/linkedin-connection-inviter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd linkedin-connection-inviter
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your LinkedIn credentials:

    ```plaintext
    USERNAME=your_linkedin_email@example.com
    PASSWORD=your_linkedin_password
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. The script will prompt you to enter the search keywords and other search criteria. You can also customize the search URL by copying the URL with desired filters applied and modifying the `search_url` variable in the script.

3. Once configured, the script will automate the process of sending connection invitations.

4. Sit back and let the script do the work! Monitor the console for progress updates and any potential errors.

## Customization

You can customize various aspects of the script to suit your preferences:

- **Message Content:** Edit the `message.txt` file to customize the invitation message.
- **Search Criteria:** Modify the `keywords` variable in the script to refine the search criteria.

## Contribution

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## Disclaimer

This script is provided for educational purposes only. Use it responsibly and at your own risk. The developers are not responsible for any misuse or violation of LinkedIn's terms of service.
