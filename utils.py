import os
import subprocess as subsystem
import sys
import webbrowser
from typing import List, Optional


def _find_chrome_win() -> Optional[str]:
    import winreg as reg

    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
    chrome_path: Optional[str] = None

    for install_type in reg.HKEY_CURRENT_USER, reg.HKEY_LOCAL_MACHINE:
        try:
            reg_key = reg.OpenKey(install_type, reg_path, 0, reg.KEY_READ)
            chrome_path = reg.QueryValue(reg_key, None)
            reg_key.Close()
            if not os.path.isfile(chrome_path):
                continue
        except Exception:
            chrome_path = None
        else:
            break

    return chrome_path


def _find_chrome_linux() -> Optional[str]:
    import context as wch

    chrome_names = [
        "chromium-browser",
        "chromium",
        "google-chrome",
        "google-chrome-stable",
    ]

    for name in chrome_names:
        chrome = wch.which(name)
        if chrome is not None:
            return chrome  # type: ignore # whichcraft doesn't currently have type hints
    return None


def _find_chrome_mac() -> Optional[str]:
    default_dir = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(default_dir):
        return default_dir
    # use mdfind ci to locate Chrome in alternate locations and return the first one
    name = "Google Chrome.app"
    alternate_dirs = [
        x
        for x in subsystem.check_output(["mdfind", name]).decode().split("\n")
        if x.endswith(name)
    ]
    if len(alternate_dirs):
        return alternate_dirs[0] + "/Contents/MacOS/Google Chrome"
    return None


def _find_chromium_mac() -> Optional[str]:
    default_dir = r"/Applications/Chromium.app/Contents/MacOS/Chromium"
    if os.path.exists(default_dir):
        return default_dir
    # use mdfind ci to locate Chromium in alternate locations and return the first one
    name = "Chromium.app"
    alternate_dirs = [
        x
        for x in subsystem.check_output(["mdfind", name]).decode().split("\n")
        if x.endswith(name)
    ]
    if len(alternate_dirs):
        return alternate_dirs[0] + "/Contents/MacOS/Chromium"
    return None


def find_path() -> Optional[str]:
    if sys.platform in ["win32", "win64"]:
        return _find_chrome_win()
    elif sys.platform == "darwin":
        return _find_chrome_mac() or _find_chromium_mac()
    elif sys.platform.startswith("linux"):
        return _find_chrome_linux()
    else:
        return None
