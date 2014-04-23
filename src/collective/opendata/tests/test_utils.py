# -*- coding: utf-8 -*-
from collective.opendata.testing import INTEGRATION_TESTING
from collective.opendata.utils import type_cast

import unittest


class UtilsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def test_type_cast(self):
        self.assertEqual(type_cast(None), '')

        from datetime import date
        self.assertEqual(type_cast(date(1943, 1, 9)), '1943-01-09')

        from datetime import datetime
        self.assertIn('1943-01-09', type_cast(datetime(1943, 1, 9)))

        from DateTime import DateTime
        self.assertIn('1943-01-09', type_cast(DateTime(1943, 1, 9)))

        from plone.namedfile.file import NamedBlobImage
        image = NamedBlobImage('')
        self.assertEqual(type_cast(image), 'image')

        self.assertEqual(
            type_cast([dict(a=None, b=date(1943, 1, 9))]),
            [dict(a='', b='1943-01-09')]
        )

        self.assertEqual(
            type_cast([None, date(1943, 1, 9)]), ['', '1943-01-09'])
