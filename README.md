# Roblox Tool

---

## Introduction
The `roblox-tool` is a Python-based utility designed to enhance gameplay automation for Roblox by enabling functionalities such as Anti-AFK, Proximity Prompt Spam, and Auto-Clicker. This tool leverages the `dearpygui` library for a graphical user interface (GUI) to facilitate quick configuration of these automation features.

## Features
- **Anti-AFK**:
  - **Spin camera** to make it appear as if you’re active.
  - **Move around** randomly within the game.
  - **Perform emotes** (dance, wave, etc.).
  - **Clicking** to keep your character active.
  - **Jumping** to avoid being kicked for inactivity.
  
- **Proximity Prompt Spam**:
  - Automatically press a specified key (e.g., "E") repeatedly to activate proximity prompts.

- **Auto Clicker**:
  - Perform automated mouse clicks at a specified interval.
  - Optionally repeat until stopped or for a fixed number of clicks.

## Installation
1. Clone or download the repository:
   ```shell
   git clone https://github.com/yourusername/roblox-tool.git
   cd roblox-tool
   ```

2. Install the necessary libraries:
   ```shell
   pip install pydirectinput dearpygui json
   ```

## Usage
1. Run the main application:
   ```shell
   python main.py
   ```

2. Configure settings in the GUI:
   - **Anti-AFK**: Use the `Toggle bind` field to activate this feature. Check boxes for `Spin camera`, `Move around`, `Chat emotes`, `Clicking`, and `Jumping` as needed.
   - **Proximity Prompt Spam**: Set the `Letter` and the `PP duration` time interval.
   - **Auto Clicker**: Adjust `Click interval`, `Repeat X times`, and choose `Repeat until stopped` if desired.
   - Click on the `Save config` button to persist settings across sessions.

3. Use defined keyboard shortcuts (configured in `config.json`) to toggle features:
   - **Anti-AFK**: Default is `home`
   - **Proximity Prompt Spam**: Default is `end`
   - **Auto Clicker**: Default is `insert`

4. The tool will alert you when a configuration is successfully saved or loaded through an on-screen message.

## Configuration
The default configuration values are provided in `config.json`:
```json
{
    "antiafk-spin": false,
    "antiafk-move": false,
    "antiafk-emotes": false,
    "antiafk-click": false,
    "antiafk-jump": false,
    "pp-letter": "E",
    "pp-duration": 1.0,
    "sleep-interval": 1.0,
    "always-on-top": false,
    "autoclicker-interval": 0.1,
    "autoclicker-repeat": 10,
    "autoclicker-toggle-bind": "insert",
    "antiafk-toggle-bind": "home",
    "pp-toggle-bind": "end"
}
```

### Saving & Loading Configurations
- The tool saves and loads configurations automatically. You can manually save or load the configuration through buttons within the GUI.

## Keybinds
- **Anti-AFK Toggle**: `home`
- **Proximity Prompt Spam Toggle**: `end`
- **Auto-Clicker Toggle**: `insert`

## Technical Overview
- The tool uses `pydirectinput` to simulate mouse and keyboard actions.
- `dearpygui` provides the graphical user interface.
- All automation operations run on separate threads to avoid blocking the main UI.

## Troubleshooting
- If you encounter issues loading the configuration, ensure that `config.json` exists or has default values.
- If the application freezes or behaves unexpectedly, restarting the application or rechecking configurations might resolve the issue.
