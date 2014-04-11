# -*- coding: utf-8 -*-
from collective.opendata.interfaces import IDataPlugin
from zope.component import getUtilitiesFor
# from z3c.relationfield.interfaces import IRelationValue
from plone.namedfile.file import NamedBlobImage

from datetime import date
from datetime import datetime


def plugins():
    """Returns a list of Open Data plugins

    :returns: list of Data Plugins
    :rtype: DataPlugin
    """
    registered = getUtilitiesFor(IDataPlugin)
    registered = [item for item in registered]
    registered.sort()
    plugins = [p[1] for p in registered]
    return plugins


def type_cast(value):
    """Convert the value to something serializable.

    :param value: [required] value to be converted
    :type value: almost anything
    :returns: serializable value
    :rtype: str
    """
    if value is None:
        return ''

    elif isinstance(value, date):
        return value.strftime('%Y-%m-%d')

    elif isinstance(value, datetime):
        return value.isoformat()

    elif isinstance(value, NamedBlobImage):
        # XXX: we need to decide what to do with the images
        #      we can embed them or use an URL to point to
        return 'image'

#    elif IRelationValue.providedBy(value):
#        return value.to_path

    elif isinstance(value, list):

        # XXX: we don't want to mess around the original
        # object so we just create a copy of the value
        tmp = list(value)
        # we must take care of two scenaries: in one we are
        # storing relations; on the other, just values
        for i in tmp:
            # if IRelationValue.providedBy(i):
                # return just the path to the related object for now
            #     tmp[tmp.index(i)] = type_cast(i)
            if type(i) == dict:
                # call function recursively on each value of the list
                tmp[tmp.index(i)] = dict(
                    (v[0], type_cast(v[1])) for v in i.items())
        return tmp

    return value
