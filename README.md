# AutoCtrl+V

AutoCtrl+V is a Python-based automation tool designed to streamline repetitive keyboard tasks. It uses the `pyautogui`, `keyboard`, and `time` libraries to simulate keyboard inputs, and `colorama` and `logging` for user-friendly console output and logging.

## Features

- **Keyboard Simulation**: The script simulates the pressing of 'Ctrl + V' and 'Enter' keys, useful for tasks that require repetitive pasting and submitting of data.
- **Customizable Hotkey**: The hotkey to start and stop the script is customizable. By default, it is set to 'F1'.
- **Adjustable Delay**: The delay between each 'Ctrl + V' command can be adjusted according to the user's needs.
- **Logging**: All key presses and actions are logged into a file 'AutoCtrl+V.log' for future reference and debugging.

## Installation

Before running AutoCtrl+V, you need to install the required Python libraries. These libraries are listed in the `requirements.txt` file. You can install them using pip, a package manager for Python. Here's how:

1. Open your terminal.
2. Navigate to the directory where `requirements.txt` is located.
3. Run the following command:

```bash
pip install -r requirements.txt
```
This command will download and install the required libraries. Once the installation is complete, you can run the AutoCtrl+V script.

## Usage

To use AutoCtrl+V, simply run the script and press the hotkey (default 'F1') to start the automation. Press the same hotkey again to stop the automation. The script will automatically paste the clipboard content and press 'Enter' with a delay between each action.

## Note

This tool is intended to automate repetitive tasks and should be used responsibly. It is not designed for spamming or any form of misuse. Please use it responsibly.