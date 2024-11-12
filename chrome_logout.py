import os
import platform
import sqlite3
import subprocess

def clear_gmail_cookies_chrome(cookie_path):
    """Clear Gmail-related cookies from Chrome."""
    gmail_domains = ['mail.google.com', 'accounts.google.com']
    
    if os.path.exists(cookie_path):
        print(f"Clearing Gmail session cookies in Chrome: {cookie_path}")
        try:
            # Open the Chrome cookies file
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()

            # Delete Gmail-related cookies from both domains
            for domain in gmail_domains:
                cursor.execute("DELETE FROM cookies WHERE host_key LIKE ?;", ('%' + domain,))

            # Commit and close the database connection
            conn.commit()
            conn.close()
            print("Cleared Gmail session cookies in Chrome.")
        except sqlite3.Error as e:
            print(f"Failed to clear cookies in Chrome: {e}")
    else:
        print("Chrome cookies file not found.")

def close_chrome():
    """Forcefully close Chrome."""
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "chrome.exe", "/F"], check=True)
            print("Chrome has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "chrome"], check=True)
            print("Chrome has been closed on macOS.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError:
        print("Failed to close Chrome. It may not be running.")

def logout_gmail_and_close_chrome():
    """Log out of all Gmail accounts and close Chrome."""
    # Path to Chrome cookies
    if platform.system() == "Windows":
        chrome_cookies_path = os.path.join(os.environ['APPDATA'], "Google", "Chrome", "User Data", "Default", "Cookies")
    elif platform.system() == "Darwin":  # macOS
        chrome_cookies_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Cookies")
    else:
        print("Unsupported OS for this script.")
        return

    # Log out of Gmail for Chrome
    clear_gmail_cookies_chrome(chrome_cookies_path)

    # Close Chrome
    close_chrome()

    print("Logout from Gmail and Chrome closure complete.")

if __name__ == "__main__":
    logout_gmail_and_close_chrome()
