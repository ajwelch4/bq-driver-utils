# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""BQ Driver Utilities CLI."""
import logging
import signal
import sys
from types import FrameType
from typing import Optional

import click

from bq_driver_utils import jdbc, odbc

root_logger = logging.getLogger()
logger = logging.getLogger("bq_driver_utils")


class LoggingFormatter(logging.Formatter):
    """Color-coded logging.Formatter."""

    red = "\033[0;31m"
    light_red = "\033[0;91m"
    yellow = "\033[0;33m"
    green = "\033[0;32m"
    white = "\033[0;97m"
    reset = "\033[0m"

    format_string = (
        "%(asctime)s: {color}%(levelname)s:{reset} %(threadName)s: %(message)s"
    )

    formats = {
        logging.DEBUG: format_string.format(color=white, reset=reset),
        logging.INFO: format_string.format(color=green, reset=reset),
        logging.WARNING: format_string.format(color=yellow, reset=reset),
        logging.ERROR: format_string.format(color=light_red, reset=reset),
        logging.CRITICAL: format_string.format(color=red, reset=reset),
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def _shutdown_handler(  # pylint: disable=unused-argument,redefined-outer-name
    signal: int, frame: Optional[FrameType] = None
) -> None:
    logger.info("Signal received, safely shutting down.")
    sys.exit(0)


signal.signal(signal.SIGTERM, _shutdown_handler)


@click.group()
@click.option("--verbose", default=False)
def cli(verbose):
    """BQ Driver Utilities."""
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(LoggingFormatter())
    root_logger.addHandler(console_handler)


cli.add_command(odbc.odbc)
cli.add_command(jdbc.jdbc)


if __name__ == "__main__":
    cli()
