from pydirectinput import keyUp, keyDown, press, leftClick, write
from random import randint, choice
import dearpygui.dearpygui as dpg
from threading import Thread
from time import sleep
import json

GV = {
    'antiafk': False,
    'ppsmap': False,
    'autoclicker': False
}

project_name = 'RTools'
config_file = 'config.json'

default_config = {
    "antiafk-spin": False,
    "antiafk-move": False,
    "antiafk-emotes": False,
    "antiafk-click": False,
    "antiafk-jump": False,
    "pp-letter": "E",
    "pp-duration": 1.0,
    "sleep-interval": 1.0,
    "always-on-top": False,
    "autoclicker-interval": 0.1,
    "autoclicker-repeat": 10,
    "autoclicker-toggle-bind": "insert",
    "antiafk-toggle-bind": "home",
    "pp-toggle-bind": "end"
}

def alert(message=str, button=bool):
    dpg.delete_item("info-st-gui", children_only=True)
    with dpg.window(label=f"{project_name} /// alert", width=183, height=30, tag="info-st-gui", pos=[25.5, 50], no_title_bar=False, no_close=True):
        dpg.add_text(f"{message}", tag="alert-txt")
        if button:
            dpg.add_button(label="Ok", pos=[70, 69], width=45, callback=lambda: dpg.delete_item('info-st-gui'))

# Anti-AFK functions
def aa1():
    dpg.set_value("antiafk-status", "Status: Spinning camera")
    keyDown('left')
    sleep(randint(1, 5))
    keyUp('left')

def aa2():
    dpg.set_value("antiafk-status", "Status: Spinning camera")
    keyDown('right')
    sleep(randint(1, 5))
    keyUp('right')

def aa3():
    dpg.set_value("antiafk-status", "Status: Moving around")
    press('a')
    sleep(0.5)
    press('d')

def aa4():
    dpg.set_value("antiafk-status", "Status: Showing emote")
    emote_choice = randint(1, 4)
    emote = {1: "dance", 2: "dance2", 3: "dance3", 4: "wave"}.get(emote_choice, "dance")
    press('/')
    sleep(0.77)
    write(f"/e {emote}")

def aa5():
    dpg.set_value("antiafk-status", "Status: Clicking")
    clicks = randint(1, 8)
    while clicks > 0:
        clicks -= 1
        leftClick()
        sleep(0.4)

def aa6():
    dpg.set_value("antiafk-status", "Status: Jumping")
    jumps = randint(1, 8)
    while jumps > 0:
        jumps -= 1
        press('space')
        sleep(1)

def anti_afk():
    global GV

    def run_anti_afk():
        actions = []

        if dpg.get_value("antiafk-spin"):
            actions.extend([aa1, aa2])
        if dpg.get_value("antiafk-move"):
            actions.append(aa3)
        if dpg.get_value("antiafk-emotes"):
            actions.append(aa4)
        if dpg.get_value("antiafk-click"):
            actions.append(aa5)
        if dpg.get_value("antiafk-jump"):
            actions.append(aa6)

        while GV["antiafk"]:
            if actions:
                action = choice(actions)
                action()
            else:
                dpg.set_value("antiafk-status", "Status: No actions!")
                sleep(1)

    if GV["antiafk"]:
        GV["antiafk"] = False
        dpg.set_value("antiafk-status", "Status: Anti-AFK Stopped")
    elif not GV["antiafk"]:
        GV["antiafk"] = True
        dpg.set_value("antiafk-status", "Status: Starting in 3 Seconds")
        sleep(3)
        dpg.set_value("antiafk-status", "Status: Anti-AFK Started")
        Thread(target=run_anti_afk).start()

# Proximity Prompt
def proximity_prompt_spam():
    global GV

    def run_pp_spam():
        letter = dpg.get_value("pp-letter")
        pp_duration = dpg.get_value("pp-duration")
        sleep_interval = dpg.get_value("sleep-interval")

        while GV["ppsmap"]:
            dpg.set_value("pp-status", "Status: Holding PP")
            keyDown(letter)
            sleep(pp_duration)
            keyUp(letter)
            sleep(sleep_interval)

    if GV["ppsmap"]:
        GV["ppsmap"] = False
        dpg.set_value("pp-status", "Status: PP Spam Stopped")
    elif not GV["ppsmap"]:
        GV["ppsmap"] = True
        dpg.set_value("pp-status", "Status: Starting in 3 Seconds")
        sleep(3)
        dpg.set_value("pp-status", "Status: PP Spam Started")
        Thread(target=run_pp_spam).start()

# Auto Clicker
def auto_clicker():
    global GV

    def run_auto_clicker():
        click_interval = dpg.get_value("auto-click-interval")
        repeat_count = dpg.get_value("auto-click-repeat")
        repeat_until_stopped = dpg.get_value("auto-click-repeat-until-stopped")

        if repeat_until_stopped:
            while GV["autoclicker"]:
                leftClick()
                sleep(click_interval)
        else:
            for _ in range(repeat_count):
                if not GV["autoclicker"]:
                    break
                leftClick()
                sleep(click_interval)

    if GV["autoclicker"]:
        GV["autoclicker"] = False
        dpg.set_value("auto-clicker-status", "Status: Clicker Stopped")
    elif not GV["autoclicker"]:
        GV["autoclicker"] = True
        dpg.set_value("auto-clicker-status", "Status: Starting in 3 Seconds")
        sleep(3)
        dpg.set_value("auto-clicker-status", "Status: Clicker Started")
        Thread(target=run_auto_clicker).start()

def apply_settings():
    always_on_top = dpg.get_value("always-on-top")
    dpg.set_viewport_always_top(always_on_top)

def save_config():
    config = {
        "antiafk-spin": dpg.get_value("antiafk-spin"),
        "antiafk-move": dpg.get_value("antiafk-move"),
        "antiafk-emotes": dpg.get_value("antiafk-emotes"),
        "antiafk-click": dpg.get_value("antiafk-click"),
        "antiafk-jump": dpg.get_value("antiafk-jump"),
        "pp-letter": dpg.get_value("pp-letter"),
        "pp-duration": dpg.get_value("pp-duration"),
        "sleep-interval": dpg.get_value("sleep-interval"),
        "always-on-top": dpg.get_value("always-on-top"),
        "autoclicker-interval": dpg.get_value("auto-click-interval"),
        "autoclicker-repeat": dpg.get_value("auto-click-repeat"),
        "autoclicker-toggle-bind": dpg.get_value("auto-click-toggle-bind"),
        "antiafk-toggle-bind": dpg.get_value("antiafk-toggle-bind"),
        "pp-toggle-bind": dpg.get_value("pp-toggle-bind")
    }
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)
    alert("Saved config", True)

def load_config():
    if not create_default_config():
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                dpg.set_value("antiafk-spin", config.get("antiafk-spin", False))
                dpg.set_value("antiafk-move", config.get("antiafk-move", False))
                dpg.set_value("antiafk-emotes", config.get("antiafk-emotes", False))
                dpg.set_value("antiafk-click", config.get("antiafk-click", False))
                dpg.set_value("antiafk-jump", config.get("antiafk-jump", False))
                dpg.set_value("pp-letter", config.get("pp-letter", "E"))
                dpg.set_value("pp-duration", config.get("pp-duration", 1.0))
                dpg.set_value("sleep-interval", config.get("sleep-interval", 1.0))
                dpg.set_value("always-on-top", config.get("always-on-top", False))
                dpg.set_value("auto-click-interval", config.get("autoclicker-interval", 0.1))
                dpg.set_value("auto-click-repeat", config.get("autoclicker-repeat", 10))
                dpg.set_value("auto-click-toggle-bind", config.get("autoclicker-toggle-bind", "insert"))
                dpg.set_value("antiafk-toggle-bind", config.get("antiafk-toggle-bind", "home"))
                dpg.set_value("pp-toggle-bind", config.get("pp-toggle-bind", "end"))
                apply_settings()
                alert("Loaded config", True)
        except FileNotFoundError:
            create_default_config()
    else:
        alert("Created new config", True)

def create_default_config():
    try:
        with open(config_file, 'x') as f:
            json.dump(default_config, f, indent=4)
        return True
    except FileExistsError:
        return False

def check_keybinds():
    from pynput import keyboard

    def on_press(key):
        try:
            if key.char == dpg.get_value("antiafk-toggle-bind"):
                anti_afk()
            elif key.char == dpg.get_value("pp-toggle-bind"):
                proximity_prompt_spam()
            elif key.char == dpg.get_value("auto-click-toggle-bind"):
                auto_clicker()
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def main():
    dpg.create_context()
    dpg.create_viewport(title=project_name, width=413, height=300, resizable=False)

    with dpg.window(label=f"{project_name} /// main window", width=397, height=261, no_close=True, no_collapse=True, no_resize=True, no_move=True, no_scrollbar=True):
        with dpg.menu_bar():
            with dpg.menu(label="Anti-AFK"):
                dpg.add_input_text(label="Toggle bind", tag="antiafk-toggle-bind", width=55, default_value="home")
                dpg.add_checkbox(label="Spin camera", tag="antiafk-spin")
                dpg.add_checkbox(label="Move around", tag="antiafk-move")
                dpg.add_checkbox(label="Chat emotes", tag="antiafk-emotes")
                dpg.add_checkbox(label="Clicking", tag="antiafk-click")
                dpg.add_checkbox(label="Jumping", tag="antiafk-jump")
            with dpg.menu(label="Proximity prompt"):
                dpg.add_input_text(label="Toggle bind", tag="pp-toggle-bind", width=55, default_value="end")
                dpg.add_input_text(label="Letter", tag="pp-letter", width=20, default_value="E")
            with dpg.menu(label='Auto Clicker'):
                dpg.add_input_text(label="Toggle bind", tag="auto-click-toggle-bind", width=55, default_value="insert")
            with dpg.menu(label="Settings"):
                dpg.add_checkbox(label="Always on top", tag="always-on-top")
                dpg.add_button(label="Apply settings", width=120, callback=apply_settings)
                dpg.add_button(label="Save config", width=120, callback=save_config)
    
        with dpg.child_window(width=198.5, height=91.5, pos=[0, 38], border=True, no_scrollbar=True, menubar=True):
            with dpg.menu_bar():
                dpg.add_text("Anti-AFK")
            dpg.add_button(label="Toggle Anti-AFK", width=183.5, height=32, callback=anti_afk)
            dpg.add_text("Status: Anti-AFK stopped.", tag="antiafk-status")
        
        with dpg.child_window(width=198.5, height=131.5, pos=[0, 129.5], border=True, no_scrollbar=True, menubar=True):
            with dpg.menu_bar():
                dpg.add_text("Proximity prompt spam")
            dpg.add_input_float(label="PP duration", tag="pp-duration", width=85)
            dpg.add_input_float(label="Sleep interval", tag="sleep-interval", width=85)
            dpg.add_button(label="Toggle PP spam", width=183.5, height=32, callback=proximity_prompt_spam)
            dpg.add_text("Status: PP Spam stopped.", tag="pp-status")

        with dpg.child_window(width=198.5, height=222, pos=[198.5, 38], border=True, no_scrollbar=True, menubar=True):
            with dpg.menu_bar():
                dpg.add_text("Auto Clicker")
            dpg.add_input_float(label="Click interval", tag="auto-click-interval", width=85)
            dpg.add_input_int(label="Repeat X times", tag="auto-click-repeat", width=85)
            dpg.add_checkbox(label="Repeat until stopped", tag="auto-click-repeat-until-stopped")
            dpg.add_button(label="Toggle Clicker", width=183.5, height=32, callback=auto_clicker)
            dpg.add_text("Status: Clicker stopped.", tag="auto-clicker-status")

    load_config()
    check_keybinds()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
