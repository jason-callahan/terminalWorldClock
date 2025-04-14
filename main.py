"""
Terminal world clock: Local, UTC, and Serbia (12h + 24h)

hot-reload with pytest-watch: 
ptw --runner "textual run main.py --dev"
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from textual.app import App, ComposeResult
from textual.widgets import Digits, Static
from textual.containers import Vertical, Horizontal


class ClockApp(App):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        with Vertical(classes="app"):
            # Local
            with Horizontal(classes="title"):
                yield Static("Local ", classes="label")
                yield Static("", id="local-12h", classes="small-time")
            with Horizontal():
                yield Digits(id="local")
                yield Static("", id="local-sec", classes="small-seconds")

            # Salt Lake City
            with Horizontal(classes="title"):
                yield Static("SLC (-2) ", classes="label")
                yield Static("", id="slc-12h", classes="small-time")
            with Horizontal():
                yield Digits(id="slc")
                yield Static("", id="slc-sec", classes="small-seconds")

            # UTC
            with Horizontal(classes="title"):
                yield Static("UTC (+4) ", classes="label")
                yield Static("", id="utc-12h", classes="small-time")
            with Horizontal():
                yield Digits(id="utc")
                yield Static("", id="utc-sec", classes="small-seconds")

            # Serbia
            with Horizontal(classes="title"):
                yield Static("Serbia (+6) ", classes="label")
                yield Static("", id="serbia-12h", classes="small-time")
            with Horizontal():
                yield Digits(id="serbia")
                yield Static("", id="serbia-sec", classes="small-seconds")

    def on_ready(self) -> None:
        self.update_clocks()
        self.set_interval(1, self.update_clocks)

    def update_clocks(self) -> None:

        now_local = datetime.now()
        self.query_one("#local-12h", Static).update(f"{now_local:%I:%M %p}")
        self.query_one("#local", Digits).update(f"{now_local:%H:%M}")
        self.query_one("#local-sec", Static).update(f"{now_local:%S}")

        now_slc = datetime.now(ZoneInfo("America/Denver"))
        self.query_one("#slc-12h", Static).update(f"{now_slc:%I:%M %p}")
        self.query_one("#slc", Digits).update(f"{now_slc:%H:%M}")
        self.query_one("#slc-sec", Static).update(f"{now_slc:%S}")

        now_utc = datetime.now(ZoneInfo("UTC"))
        self.query_one("#utc", Digits).update(f"{now_utc:%H:%M}")
        self.query_one("#utc-12h", Static).update(f"{now_utc:%I:%M %p}")
        self.query_one("#utc-sec", Static).update(f"{now_utc:%S}")

        now_serb = datetime.now(ZoneInfo("Europe/Belgrade"))
        self.query_one("#serbia", Digits).update(f"{now_serb:%H:%M}")
        self.query_one("#serbia-12h", Static).update(f"{now_serb:%I:%M %p}")
        self.query_one("#serbia-sec", Static).update(f"{now_serb:%S}")


if __name__ == "__main__":
    ClockApp().run()
