#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
    url = "https://www.ygg.re/"
    # sb.uc_open_with_reconnect(url, 5)
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    html_content = sb.cdp.get_page_source()
    print(html_content)
    
# 在这里添加一个换行符