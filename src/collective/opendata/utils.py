# -*- coding: utf-8 -*-
from DateTime import DateTime
from collective.opendata.interfaces import IDataPlugin
from datetime import date
from datetime import datetime
from plone.namedfile.file import NamedBlobImage
from z3c.relationfield.interfaces import IRelationValue
from zope.component import getUtilitiesFor


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
        return value.isoformat()

    elif isinstance(value, datetime):
        return value.isoformat()

    elif isinstance(value, DateTime):
        return value.ISO()

    elif isinstance(value, NamedBlobImage):
        # XXX: we need to decide what to do with the images
        #      we can embed them or use an URL to point to
        return 'image'

    elif IRelationValue.providedBy(value):
        # return just the path to the related object for now
        return value.to_path

    elif isinstance(value, list):
        # XXX: we don't want to mess around the original list
        # object so we just create a copy of the value
        tmp = list(value)
        for i in tmp:
            # call function recursively on each value of the list
            if type(i) == dict:
                tmp[tmp.index(i)] = dict(
                    (v[0], type_cast(v[1])) for v in i.items())
            else:
                tmp[tmp.index(i)] = type_cast(i)
        return tmp

    return value
