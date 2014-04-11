# -*- coding: utf-8 -*-
from collective.opendata.config import ENDPOINT
from collective.opendata.interfaces import IDataPlugin  # noqa
from plone import api

import json


class DataPlugin(object):

    name = ''
    title = ''
    description = ''
    structure = {}

    @property
    def uri(self):
        base_uri = '{0}/{1}/{2}'
        return base_uri.format(
            api.portal.get().absolute_url(),
            ENDPOINT,
            self.name
        )

    def entities(self):
        structure = self.structure
        entities = []
        for entity_id in structure:
            entity = structure[entity_id]
            uri = '{0}/{1}'.format(self.uri,
                                   entity_id)
            entities.append(
                {
                    'entity': entity_id,
                    'description': entity.get('description'),
                    'uri': uri
                }
            )
        return entities

    def json(self, data):
        return json.dumps(data, encoding='utf-8', ensure_ascii=False)
