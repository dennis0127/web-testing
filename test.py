#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB

with SB(uc=True, locale_code="en", xvfb="True") as sb:
    url = "https://www.ygg.re/"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.save_screenshot("test.png")
