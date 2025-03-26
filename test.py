#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB


def test():
    with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
        url = "https://www.ygg.re/"
        sb.activate_cdp_mode(url)
        sb.uc_gui_click_captcha()
        html_content = sb.cdp.get_page_source()
        print(html_content)


if __name__ == "__main__":
    print("Hello, World!")
