# -*- coding: utf-8 -*-
from flask import flash


class Country(object):

    def DataList(self, text):
        if text == '':
            flash("no country to display")
        else:
            flash(text + "!!!")
