import os
import platform
import sqlite3
import subprocess

def clear_gmail_cookies_edge(cookie_path):
    """Clear Gmail-related cookies from Edge."""
    gmail_domains = ['mail.google.com', 'accounts.google.com']

    if os.path.exists(cookie_path):
        print(f"Clearing Gmail session cookies in Edge: {cookie_path}")
        try:
            # Open the Edge cookies file
            conn = sqlite3.connect(cookie_path)
            cursor = conn.cursor()

            # Delete Gmail-related cookies from both domains
            for domain in gmail_domains:
                cursor.execute("DELETE FROM cookies WHERE host_key LIKE ?;", ('%' + domain,))

            # Commit and close the database connection
            conn.commit()
            conn.close()
            print("Cleared Gmail session cookies in Edge.")
        except sqlite3.Error as e:
            print(f"Failed to clear cookies in Edge: {e}")
    else:
        print("Edge cookies file not found.")

def close_edge():
    """Forcefully close Edge."""
    try:
        if platform.system() == "Windows":
            subprocess.run(["taskkill.exe", "/IM", "msedge.exe", "/F"], check=True)
            print("Edge has been closed using taskkill.")
        elif platform.system() == "Darwin":
            subprocess.run(["pkill", "Microsoft Edge"], check=True)
            print("Edge has been closed on macOS.")
        else:
            print("Unsupported operating system.")
    except subprocess.CalledProcessError:
        print("Failed to close Edge. It may not be running.")

def logout_gmail_and_close_edge():
    """Log out of all Gmail accounts and close Edge."""
    # Path to Edge cookies
    if platform.system() == "Windows":
        edge_cookies_path = os.path.join(os.environ['APPDATA'], "Microsoft", "Edge", "User Data", "Default", "Cookies")
    elif platform.system() == "Darwin":  # macOS
        edge_cookies_path = os.path.expanduser("~/Library/Application Support/Microsoft Edge/Default/Cookies")
    else:
        print("Unsupported OS for this script.")
        return

    # Log out of Gmail for Edge
    clear_gmail_cookies_edge(edge_cookies_path)

    # Close Edge
    close_edge()

    print("Logout from Gmail and Edge closure complete.")

if __name__ == "__main__":
    logout_gmail_and_close_edge()
