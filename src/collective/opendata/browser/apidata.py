# -*- coding: utf-8 -*-
from collective.opendata import utils
from collective.opendata.interfaces import IDataPlugin
from zope.component import queryUtility
from zope.publisher.browser import BrowserPage


class APIDataView(BrowserPage):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self._path = []

    @property
    def traverse_subpath(self):
        return self._path

    def publishTraverse(self, request, name):
        self._path.append(name)
        return self

    def _subpath(self):
        return getattr(self, 'traverse_subpath', [])

    @property
    def plugin(self):
        """ """
        plugin = None
        subpath = self._subpath()
        if len(subpath) > 0:
            plugin_id = subpath[0]
            plugin = queryUtility(IDataPlugin, name=plugin_id)
        return plugin

    @property
    def entity(self):
        """ """
        entity = None
        subpath = self._subpath()
        if len(subpath) > 1:
            entity_id = subpath[1].replace(' ', '_')
            plugin = self.plugin
            entity = getattr(plugin, entity_id, None)
        return entity

    def __call__(self):
        """ Return a JSON response
        """
        request = self.request
        response = ''
        plugin = self.plugin
        entity = self.entity
        if plugin:
            if entity:
                subpath = self._subpath()
                data = entity(request, subpath=subpath)
                response = plugin.json(data) if data else '{}'
            else:
                response = plugin.json(plugin.entities())
        else:
            data = []
            plugins = utils.plugins()
            for plugin in plugins:
                tmp = {
                    'name': plugin.name,
                    'title': plugin.title,
                    'uri': plugin.uri
                }
                data.append(plugin.json(tmp))
            response = '[{0}]'.format(', '.join(data))
        request.response.setHeader('Content-Type',
                                   'application/json;charset=utf-8')
        return response
