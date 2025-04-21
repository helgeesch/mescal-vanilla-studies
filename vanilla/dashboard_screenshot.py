import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def take_screenshot_of_html_dashboard(
        dashboard_html_path: str,
        output_path: str,
        width: int = 1200,
        delay: int = 2
):
    """
    Takes a full-page screenshot of an HTML dashboard and saves it as PNG.

    Args:
        dashboard_html_path: Path to the saved HTML dashboard file
        output_path: Path where to save the PNG image
        width: Width of the browser viewport in pixels
        delay: Seconds to wait for the page to fully render

    Returns:
        Path to the saved screenshot
    """

    # Ensure the dashboard file exists
    if not os.path.exists(dashboard_html_path):
        raise ValueError(f"Dashboard file not found at {dashboard_html_path}")

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Set initial window size
        driver.set_window_size(width, 800)

        # Load the HTML file
        file_url = f"file://{os.path.abspath(dashboard_html_path)}"
        driver.get(file_url)

        # Wait for page to render (especially important for Plotly and Folium)
        time.sleep(delay)

        # Get total height of the page and resize window
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(width, total_height)

        # Take screenshot
        driver.save_screenshot(output_path)

        return output_path

    finally:
        driver.quit()
