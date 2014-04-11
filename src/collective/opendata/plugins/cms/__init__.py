# -*- coding: utf-8 -*-
from collective.opendata.interfaces import IDataPlugin
from collective.opendata.plugins import DataPlugin
from plone import api
from zope.interface import implements


class CMS(DataPlugin):
    implements(IDataPlugin)

    name = 'cms'
    title = 'CMS'
    description = '''Information about the CMS used in this portal'''

    structure = {
        'site_info': {
            'description': 'Information about a portal',
            'fields': {
                'title': 'Site title',
                'description': 'Site description',
                'software': 'CMS used',
                'software_version': 'CMS version',
            }
        }
    }

    def site_info(self):
        """ Returns site information

        :returns: dictionary with site information
        :rtype: dict
        """
        site = api.portal.get()
        data = {}
        data['title'] = site.title
        data['description'] = site.description
        data['software'] = 'collective.opendata'
        data['software_version'] = '0.1'
        return data
