# -*- coding: utf-8 -*-
from collective.opendata.config import ENDPOINT
from collective.opendata.testing import INTEGRATION_TESTING
from plone import api
from plone.testing.z2 import Browser

import json
import unittest


class APIDataTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        portal_url = api.portal.get().absolute_url()
        self.url = '{0}/{1}/'.format(portal_url, ENDPOINT)

    def test_base_url_headers(self):
        browser = Browser(self.app)
        browser.open(self.url)
        # Should be json
        self.assertEqual('application/json;charset=utf-8',
                         browser.headers['Content-Type'])

    def test_base_url_response(self):
        browser = Browser(self.app)
        browser.open(self.url)
        contents = json.loads(browser.contents)
        # A list with at least one element
        self.assertTrue(isinstance(contents, list))
        self.assertTrue(len(contents) >= 1)
        # At least our CMS Plugin
        plugin = [p for p in contents if p['name'] == 'cms']
        self.assertEqual(len(plugin), 1)
