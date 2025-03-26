#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en", xvfb="True") as sb:
    url = "https://www.ygg.re/"