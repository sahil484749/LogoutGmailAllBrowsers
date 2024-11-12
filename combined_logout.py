import os
import platform
import sqlite3
import subprocess

# Firefox: Clear Gmail cookies and close Firefox
def clear_gmail_cookies_firefox(profile_path):
    gmail_domains = ['mail.google.com', 'accounts.google.com']
    for profile in os.listdir(profile_path):
        profile_dir = os.path.join(profile_path, profile)
        cookies_file = os.path.join(profile_dir, "cookies.sqlite")
        if os.path.exists(cookies_file):
            print(f"Clearing Gmail session cookies in Firefox profile: {profile}")
            try:
                conn = sqlite3.connect(cookies_file)
                cursor = conn.cursor()
                for domain in gmail_domains:
                    cursor.execute("DELETE FROM moz_cookies WHERE host LIKE ?;", ('%' + domain,))
                conn.commit()
                conn.close()
                print(f"Cleared Gmail session cookies in profile: {profile}")
            except sqlite3.Error as e:
                print(f"Failed to clear cookies for profile {profile}: {e}")

def close_firefox():
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "firefox.exe", "/F"], check=True)
            print("Firefox has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "firefox"], check=True)
            print("Firefox has been closed on macOS.")
    except subprocess.CalledProcessError:
        print("Failed to close Firefox. It may not be running.")

# Chrome: Clear Gmail cookies and close Chrome
def clear_gmail_cookies_chrome(cookie_path):
    gmail_domains = ['mail.google.com', 'accounts.google.com']
    if os.path.exists(cookie_path):
        print(f"Clearing Gmail session cookies in Chrome: {cookie_path}")
        try:
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()
            for domain in gmail_domains:
                cursor.execute("DELETE FROM cookies WHERE host_key LIKE ?;", ('%' + domain,))
            conn.commit()
            conn.close()
            print("Cleared Gmail session cookies in Chrome.")
        except sqlite3.Error as e:
            print(f"Failed to clear cookies in Chrome: {e}")

def close_chrome():
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "chrome.exe", "/F"], check=True)
            print("Chrome has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "chrome"], check=True)
            print("Chrome has been closed on macOS.")
    except subprocess.CalledProcessError:
        print("Failed to close Chrome. It may not be running.")

# Edge: Clear Gmail cookies and close Edge
def clear_gmail_cookies_edge(cookie_path):
    gmail_domains = ['mail.google.com', 'accounts.google.com']
    if os.path.exists(cookie_path):
        print(f"Clearing Gmail session cookies in Edge: {cookie_path}")
        try:
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()
            for domain in gmail_domains:
                cursor.execute("DELETE FROM cookies WHERE host_key LIKE ?;", ('%' + domain,))
            conn.commit()
            conn.close()
            print("Cleared Gmail session cookies in Edge.")
        except sqlite3.Error as e:
            print(f"Failed to clear cookies in Edge: {e}")

def close_edge():
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "msedge.exe", "/F"], check=True)
            print("Edge has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "Microsoft Edge"], check=True)
            print("Edge has been closed on macOS.")
    except subprocess.CalledProcessError:
        print("Failed to close Edge. It may not be running.")

# Main function to logout Gmail and close all browsers
def logout_gmail_and_close_all():
    browser = input("Which browser would you like to close? (firefox/chrome/edge): ").strip().lower()

    if browser == "firefox":
        if platform.system() == "Windows":
            firefox_profile_path = os.path.join(os.environ['APPDATA'], "Mozilla", "Firefox", "Profiles")
        elif platform.system() == "Darwin":
            firefox_profile_path = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")
        clear_gmail_cookies_fire
