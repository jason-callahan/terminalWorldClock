"""
Terminal world clock: Local, UTC, and Serbia (12h + 24h)
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from textual.app import App, ComposeResult
from textual.widgets import Digits, Static
from textual.containers import Vertical


class ClockApp(App):
    CSS = """

    Vertical {
        height: auto;
    }

    .label {
        padding: 1 0 0 0;
    }

    .small-time {
        text-style: italic;
        color: gray;
    }

    Digits {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical():
            # Local
            yield Static("Local", classes="label")
            yield Static("", id="local-12h", classes="small-time")
            yield Digits(id="local")

            # UTC
            yield Static("UTC", classes="label")
            yield Static("", id="utc-12h", classes="small-time")
            yield Digits(id="utc")

            # Serbia
            yield Static("Serbia", classes="label")
            yield Static("", id="serbia-12h", classes="small-time")
            yield Digits(id="serbia")

    def on_ready(self) -> None:
        self.update_clocks()
        self.set_interval(1, self.update_clocks)

    def update_clocks(self) -> None:
        now_local = datetime.now()
        now_utc = datetime.now(ZoneInfo("UTC"))
        now_serb = datetime.now(ZoneInfo("Europe/Belgrade"))

        # 24-hour format
        self.query_one("#local", Digits).update(f"{now_local:%T}")
        self.query_one("#utc", Digits).update(f"{now_utc:%T}")
        self.query_one("#serbia", Digits).update(f"{now_serb:%T}")

        # 12-hour format
        self.query_one("#local-12h", Static).update(f"{now_local:%I:%M:%S %p}")
        self.query_one("#utc-12h", Static).update(f"{now_utc:%I:%M:%S %p}")
        self.query_one("#serbia-12h", Static).update(f"{now_serb:%I:%M:%S %p}")


if __name__ == "__main__":
    ClockApp().run()
