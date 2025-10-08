# Unified Social Media Message Manager

## Overview
The Unified Social Media Message Manager is a system designed to centralize communication from various social media platforms into a single interface, specifically within Telegram. This allows users to efficiently manage and respond to messages from different sources without the need to switch between multiple applications.

## Project Structure
```
social_manager/
├── main.py                 # Main entry point of the application
├── config.py              # Configuration settings and environment variable loading
├── database/
│   └── db_manager.py      # SQLite database management
├── bots/
│   ├── telegram_bot.py    # Telegram bot functionality
│   └── vk_bot.py          # VK bot functionality
├── utils/
│   └── message_router.py   # Message routing logic
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not in repository)
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd social_manager
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and add your API tokens and keys as follows:
     ```
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     TELEGRAM_MASTER_CHAT_ID=your_chat_id
     
     VK_GROUP_TOKEN=your_vk_group_token
     VK_GROUP_ID=your_group_id
     VK_CONFIRMATION_TOKEN=your_confirmation_token
     ```

## Usage

1. Start the application by running the main script:
   ```
   python main.py
   ```

2. The Telegram bot will now be active and ready to receive messages from VK and respond to them.

## Features
- Centralized message management from Telegram and VK.
- Quick response capabilities directly from the Telegram interface.
- Contextual message handling to maintain conversation flow.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.