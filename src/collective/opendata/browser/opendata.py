# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from collective.opendata import utils


class OpenDataView(BrowserView):
    """
    """

    @property
    def plugins(self):
        """ Open Data Plugins"""
        registered = utils.plugins()
        plugins = [self._p(p) for p in registered]
        return plugins

    def _p(self, plugin):
        p = {}
        p['name'] = plugin.name
        p['uri'] = plugin.uri
        p['title'] = plugin.title
        p['description'] = plugin.description
        structure = plugin.structure
        entities = []
        for item in structure:
            entity = structure[item]
            tmp = {}
            tmp['uri'] = '{0}/{1}'.format(plugin.uri, item)
            tmp['title'] = item
            tmp['description'] = entity['description']
            fields = [
                {'title': title,
                 'description': description}
                for title, description in entity['fields'].items()]
            tmp['fields'] = fields
            entities.append(tmp)
        p['entities'] = entities
        return p
