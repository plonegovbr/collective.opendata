# -*- coding: utf-8 -*-
from collective.opendata.interfaces import IDataPlugin
from collective.opendata.testing import INTEGRATION_TESTING
from plone import api
from zope.component import queryUtility

import unittest


class CMSPluginTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.view = api.content.get_view(
            name='apidata', context=self.portal, request=self.request)

    def test_plugin_registered(self):
        plugin = queryUtility(IDataPlugin, name='cms')
        self.assertIsNotNone(plugin)

    def test_plugin_name(self):
        plugin = queryUtility(IDataPlugin, name='cms')
        self.assertEqual(plugin.name, 'cms')

    def test_plugin_title(self):
        plugin = queryUtility(IDataPlugin, name='cms')
        self.assertEqual(plugin.title, 'CMS')

    def test_plugin_description(self):
        plugin = queryUtility(IDataPlugin, name='cms')
        self.assertIn('CMS used', plugin.description)

    def test_plugin_methods(self):
        plugin = queryUtility(IDataPlugin, name='cms')
        structure = plugin.structure
        for item in structure:
            self.assertIsNotNone(getattr(plugin, item, None))

    def test_plugin_site_info(self):
        self.portal.title = 'Gov Portal'
        self.portal.description = 'Portal Description'
        plugin = queryUtility(IDataPlugin, name='cms')
        data = plugin.site_info()
        self.assertEqual(data['title'], 'Gov Portal')
        self.assertEqual(data['description'], 'Portal Description')
        self.assertEqual(
            data['software'],
            'collective.opendata'
        )
        self.assertEqual(
            data['software_version'],
            '1.0a2'
        )
