from typing import TYPE_CHECKING
import os
import io
from pathlib import Path
from IPython.display import Image, display

if TYPE_CHECKING:
    import plotly.graph_objects as go
    import folium
    from mescal.visualizations.html_dashboard import HTMLDashboard
    from mescal.visualizations.html_table import HTMLTable


class ConditionalRenderer:
    """
    ConditionalRenderer handles interactive or static rendering of visual content in Jupyter notebooks,
    depending on the environment.

    If the environment variable `PREPARING_NOTEBOOKS_FOR_GITHUB_UPLOAD=True` is set, it will:
    - Render Plotly figures as static PNG images
    - Render Folium maps as static PNG screenshots
    - Render HTML dashboards via temporary HTML file and screenshot

    Otherwise (default behavior), it will:
    - Show Plotly figures with full interactivity (`fig.show()`)
    - Display Folium maps with native Leaflet interactivity
    - Render HTML dashboards as embedded iframes

    This enables seamless switching between interactive exploration and static output (e.g., for GitHub previews).

    Args:
        width (int): Browser viewport width used for HTML screenshots. Default is 1200 pixels.
        height (int): Initial browser viewport height (can grow for full-page screenshots). Default is 800 pixels.
        screenshot_delay (int): Seconds to wait before capturing a screenshot (to allow JS rendering). Default is 2.
        preparing_for_github_env_var (str): Name of the environment variable that toggles static rendering mode.
                                            Default is "preparing_notebooks_for_github_upload".
    """

    def __init__(
            self,
            width: int = 1200,
            height: int = 800,
            screenshot_delay: int = 2,
            preparing_for_github_env_var: str = "PREPARING_NOTEBOOKS_FOR_GITHUB_UPLOAD",
            _env_file_path: Path | str = ".env"
    ):
        self._load_env_file(str(_env_file_path))
        self.preparing_for_github = os.environ.get(preparing_for_github_env_var, "False").lower() == "true"
        self.width = width
        self.height = height
        self.screenshot_delay = screenshot_delay
        self._tmp_dir = None

    @property
    def tmp_dir(self) -> Path:
        if self._tmp_dir is None:
            import tempfile
            self._tmp_dir = Path(tempfile.mkdtemp())
        return self._tmp_dir

    def show_plotly(self, fig: 'go.Figure'):
        if self.preparing_for_github:
            export_path = self.tmp_dir / "plot.png"
            fig.write_image(str(export_path), width=self.width, height=self.height)
            display(Image(filename=str(export_path)))
        else:
            fig.update_layout(height=self.height)
            fig.show()

    def show_folium(self, m: 'folium.Map'):
        if self.preparing_for_github:
            from PIL import Image as PILImage

            export_path = self.tmp_dir / "map.png"
            img_data = m._to_png(self.screenshot_delay)
            img = PILImage.open(io.BytesIO(img_data))
            img.save(export_path)
            display(Image(filename=str(export_path)))
        else:
            display(m)

    def show_html_dashboard(self, dashboard: 'HTMLDashboard'):
        html_path = self.tmp_dir / "dashboard.html"
        dashboard.save(html_path)

        if self.preparing_for_github:
            screenshot_path = self.tmp_dir / "dashboard_screenshot.png"
            self._take_screenshot_of_html(html_path, screenshot_path)
            display(Image(filename=str(screenshot_path)))
        else:
            dashboard.show(height=str(self.height))

    def show_html_table(self, table: 'HTMLTable'):
        html_path = self.tmp_dir / "table.html"
        table.save_html(str(html_path))

        if self.preparing_for_github:
            screenshot_path = self.tmp_dir / "table_screenshot.png"
            self._take_screenshot_of_html(html_path, screenshot_path)
            display(Image(filename=str(screenshot_path)))
        else:
            table.show(height=str(self.height))

    def _take_screenshot_of_html(
            self,
            html_path: Path,
            output_path: Path,
    ):
        import time

        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.set_window_size(self.width, self.height)
            driver.get(f"file://{html_path.resolve()}")
            time.sleep(self.screenshot_delay)
            total_height = driver.execute_script("return document.body.scrollHeight")
            driver.set_window_size(self.width, total_height)
            driver.save_screenshot(str(output_path))
        finally:
            driver.quit()

    @staticmethod
    def _load_env_file(env_path: str) -> None:
        env_file = Path(env_path)
        if not env_file.exists():
            return

        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())
