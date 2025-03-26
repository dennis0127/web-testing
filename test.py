#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB


def test():
    with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
        url = "https://www.ygg.re/"
        sb.uc_open_with_reconnect(url)
        # sb.activate_cdp_mode(url)
        # sb.sleep(2)
        sb.uc_gui_click_captcha()
        html_content = sb.get_page_source()
        print(html_content)


if __name__ == "__main__":
    test()
