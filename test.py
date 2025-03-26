#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB


def test():
    with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
        print("-----开始执行测试用例-----")
        url = "https://www.ygg.re/"
        sb.uc_open_with_reconnect(url, 5)
        # sb.activate_cdp_mode(url)
        # sb.sleep(2)
        sb.uc_gui_click_captcha()
        html_content = sb.get_page_source()
        print(html_content)


if __name__ == "__main__":
    test()
