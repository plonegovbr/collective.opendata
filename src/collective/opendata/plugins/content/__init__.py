# -*- coding: utf-8 -*-
from collective.opendata.interfaces import IDataPlugin
from collective.opendata.plugins import DataPlugin
from plone import api
from zope.interface import implements

DC_MAPPING = {
    'contributor': 'listContributors',
    'coverage': '',
    'creator': 'Creator',
    'date': 'Date',
    'description': 'Description',
    'format': 'Format',
    'identifier': 'Identifier',
    'language': 'Language',
    'publisher': 'Publisher',
    'relation': '',
    'rights': 'Rights',
    'source': '',
    'subject': 'Subject',
    'title': 'Title',
    'type': ''
}


class Content(DataPlugin):
    implements(IDataPlugin)

    name = 'content'
    title = 'Content Metadata'
    description = '''Content information'''

    portal_types = ['File', 'Document', 'Image', 'Event', 'News Item', 'Folder']

    def __init__(self, *args, **kwargs):

        for pt in self.portal_types:
            attr_name = pt.replace(' ', '_')
            setattr(self, attr_name, self._process_content)

    def _process_content(self, request=None, **kwargs):
        subpath = kwargs.get('subpath', [])
        portal_type = subpath[1] if len(subpath) > 1 else None
        uid = subpath[2] if len(subpath) > 2 else None
        if uid:
            return self.content(portal_type=portal_type, uid=uid)
        else:
            return self.list(portal_type=portal_type)

    @property
    def structure(self):
        structure = {}
        dc_fields = {
            'uri': 'Content URI',
            'url': 'Content site address',
            'Id': 'Content id',
            'Title': 'Dublin Core Title element - resource name.',
            'Description': 'Dublin Core Description element - resource name.',
            'Creator': 'Dublin Core Creator element - resource author.',
        }
        for portal_type in self.portal_types:
            structure[portal_type] = {
                'description': 'Dublin Core info for {0}'.format(portal_type)
            }
            structure[portal_type]['fields'] = dc_fields.copy()
        return structure

    def _dc_content(self, content):
        """ Returns DC info

        :returns: dictionary with content information
        :rtype: dict
        """
        data = {}
        for key, value in DC_MAPPING.items():
            if value and hasattr(content, value):
                # Using method
                data[key] = getattr(content, value)()
        data['type'] = content.portal_type
        return data

    def content(self, portal_type=None, uid=None):
        """ Returns info about a content

        :returns: dictionary with content information
        :rtype: dict
        """
        data = {}
        if uid:
            try:
                content = api.content.get(UID=uid)
            except ValueError:
                return data
            if content.portal_type == portal_type:
                data = self._dc_content(content)
        return data

    def list(self, portal_type=None):
        """ Returns info about a content

        :returns: dictionary with content information
        :rtype: dict
        """
        ct = api.portal.get_tool('portal_catalog')
        items = []
        results = ct.searchResults(portal_type=portal_type)
        for brain in results:
            uid = brain.UID
            item = {'uid': uid}
            item['identifier'] = brain.getURL()
            # Need to escape portal_type
            item['uri'] = '{0}/{1}/{2}'.format(
                self.uri,
                portal_type,
                uid
            )
            item['title'] = brain.Title
            items.append(item)
        return items
