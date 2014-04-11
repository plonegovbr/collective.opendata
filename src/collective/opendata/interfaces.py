# -*- coding: utf-8 -*-
from zope.interface import Interface


class IDataPlugin(Interface):
    ''' An Open Data Plugin '''

    def name():
        pass

    def title():
        pass

    def description():
        pass

    def structure():
        pass
