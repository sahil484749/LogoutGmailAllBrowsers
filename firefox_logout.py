import os
import platform
import sqlite3
import subprocess

def clear_gmail_cookies_firefox(profile_path):
    """Clear Gmail-related cookies from all Firefox profiles."""
    # Define the Gmail session cookies to delete
    gmail_domains = ['mail.google.com', 'accounts.google.com']

    for profile in os.listdir(profile_path):
        profile_dir = os.path.join(profile_path, profile)
        cookies_file = os.path.join(profile_dir, "cookies.sqlite")
        
        if os.path.exists(cookies_file):
            print(f"Clearing Gmail session cookies in Firefox profile: {profile}")
            try:
                # Open the cookies.sqlite file for the Firefox profile
                conn = sqlite3.connect(cookies_file)
                cursor = conn.cursor()
                
                # Delete Gmail-related cookies from both domains
                for domain in gmail_domains:
                    cursor.execute("DELETE FROM moz_cookies WHERE host LIKE ?;", ('%' + domain,))

                # Commit and close the database connection
                conn.commit()
                conn.close()
                print(f"Cleared Gmail session cookies in profile: {profile}")
            except sqlite3.Error as e:
                print(f"Failed to clear cookies for profile {profile}: {e}")

def close_firefox():
    """Forcefully close Firefox."""
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "firefox.exe", "/F"], check=True)
            print("Firefox has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "firefox"], check=True)
            print("Firefox has been closed on macOS.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError:
        print("Failed to close Firefox. It may not be running.")

def logout_gmail_and_close_firefox():
    """Log out of all Gmail accounts and close Firefox."""
    # Path to Firefox profiles
    if platform.system() == "Windows":
        firefox_profile_path = os.path.join(os.environ['APPDATA'], "Mozilla", "Firefox", "Profiles")
    elif platform.system() == "Darwin":  # macOS
        firefox_profile_path = os.path.expanduser("~/Library/Application Support/Firefox/Profiles")
    else:
        print("Unsupported OS for this script.")
        return

    # Log out of Gmail for Firefox by clearing session cookies
    clear_gmail_cookies_firefox(firefox_profile_path)

    # Close Firefox
    close_firefox()

    print("Logout from Gmail and Firefox closure complete.")

if __name__ == "__main__":
    logout_gmail_and_close_firefox()
