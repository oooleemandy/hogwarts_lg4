#!/usr/bin/env python
# -*- coding: utf-8 -*-
from podemo1.page.index_page import IndexPage


class TestContact:
    def setup(self):
        self.index = IndexPage()

    def test_addcontact(self):
        name = "AA"
        account = "aa"
        phonenum = "13011111111"

        addmemberpage = self.index.click_add_member()
        addmemberpage.add_member(name, account, phonenum)
        result = addmemberpage.get_member(name)
        assert name in result