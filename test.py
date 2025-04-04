#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB


def test():
    with SB(
        uc=True,
        test=True,
        locale_code="en",
        xvfb=True,
        incognito=True,
    ) as sb:
        url = "https://vstat.info/amazon.com"
        # url = "https://www.ygg.re/"
        # sb.uc_open_with_reconnect(url, 5)
        sb.activate_cdp_mode(url)
        sb.sleep(5)
        print(sb.get_page_title())
        sb.uc_gui_click_captcha()
        print(sb.get_page_title())
        sb.sleep(2)
        print(sb.get_page_title())
        # html_content = sb.get_page_source()
        # print(html_content)


if __name__ == "__main__":
    test()
