#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
    url = "https://ipinfo.thordata.com/"
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    html_content = sb.get_page_source()
    print(html_content)
