# -*- coding: utf-8 -*-
from collective.opendata import _
from collective.opendata.interfaces import IDataPlugin
from collective.opendata.plugins import DataPlugin
from plone import api
from zope.interface import implements


class CMS(DataPlugin):
    implements(IDataPlugin)

    name = 'cms'
    title = _(u'CMS')
    description = _(u'''Information about the CMS used in this portal''')

    structure = {
        'site_info': {
            'description': _(u'Information about a portal'),
            'fields': {
                'title': _(u'Site title'),
                'description': _(u'Site description'),
                'software': _(u'CMS used'),
                'software_version': _(u'CMS version'),
            }
        }
    }

    def site_info(self, request=None, **kwargs):
        """ Returns site information

        :returns: dictionary with site information
        :rtype: dict
        """
        site = api.portal.get()
        data = {}
        data['title'] = site.title
        data['description'] = site.description
        data['software'] = 'collective.opendata'
        data['software_version'] = '1.0a2'
        return data
