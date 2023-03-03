#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2021 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

import os
import re
import string
import typing


def tty_print(text: str, tty: bool):
    """
    Print text to terminal if tty is True,
    otherwise removes all ANSI escape sequences
    """
    print(text if tty else re.sub(r"\033\[[0-9;]*m", "", text))


def tty_input(text: str, tty: bool) -> str:
    """
    Print text to terminal if tty is True,
    otherwise removes all ANSI escape sequences
    """
    return input(text if tty else re.sub(r"\033\[[0-9;]*m", "", text))


def api_config(tty: typing.Optional[bool] = None):
    """Request API config from user and set"""
    from . import main

    if tty is None:
        print("\033[0;91mThe quick brown fox jumps over the lazy dog\033[0m")
        tty = input("Is the text above colored? [y/N]").lower() == "y"

    if tty:
        print("\033[2J\033[3;1f")
        with open(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "assets", "banner.txt")
            ),
            "r",
        ) as banner:
            print(banner.read().replace("\\033", "\033"))

    tty_print("\033[0;95mWelcome to Hikka Userbot!\033[0m", tty)
    tty_print("\033[0;96m1. Go to https://my.telegram.org and login\033[0m", tty)
    tty_print("\033[0;96m2. Click on \033[1;96mAPI development tools\033[0m", tty)
    tty_print(
        (
            "\033[0;96m3. Create a new application, by entering the required"
            " details\033[0m"
        ),
        tty,
    )
    tty_print(
        (
            "\033[0;96m4. Copy your \033[1;96mAPI ID\033[0;96m and \033[1;96mAPI"
            " hash\033[0m"
        ),
        tty,
    )

    while api_id := tty_input("\033[0;95mEnter API ID: \033[0m", tty):
        if api_id.isdigit():
            break

        tty_print("\033[0;91mInvalid ID\033[0m", tty)

    if not api_id:
        tty_print("\033[0;91mCancelled\033[0m", tty)
        exit(0)

    while api_hash := tty_input("\033[0;96mEnter API hash: \033[0m", tty):
        if len(api_hash) == 32 and all(
            symbol in string.hexdigits for symbol in api_hash
        ):
            break

        tty_print("\033[0;91mInvalid hash\033[0m", tty)

    if not api_hash:
        tty_print("\033[0;91mCancelled\033[0m", tty)
        exit(0)

    (main.BASE_PATH / "api_token.txt").write_text(api_id + "\n" + api_hash)
    tty_print("\033[0;92mAPI config saved\033[0m", tty)
