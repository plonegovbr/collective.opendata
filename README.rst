collective.opendata
===================

.. contents:: Content
   :depth: 2

Introduction
------------

A generic implementation of a pluggable open data package for Plone.

.. figure:: https://raw.github.com/plonegovbr/collective.opendata/master/open-data.png
  :align: center
  :height: 416px
  :width: 545px
  :alt: The Plone Open Data API.

  The Plone Open Data API.

Features
--------

This package have by default two (02) open data pluggable as the following:

CMS
...

A plugin for information about the CMS used in this portal.

* **site_info:** Information about a portal.

This plugin generate a JSON format from the base API URL: http://localhost:8080/Plone/apidata/cms

::

    [{
        "uri": "http://localhost:8080/Plone/apidata/cms/site_info",
        "description": "Information about a portal",
        "entity": "site_info"
    }]

A JSON format for Information site, like this:

::

  {
    "software": "collective.opendata",
    "description": "",
    "software_version": "0.1",
    "title": "Site"
  }

Content Metadata
................

A plugin for content information.

* **News Item:** Dublin Core info for News Item.

* **Image:** Dublin Core info for Image.

* **File:** Dublin Core info for File.

* **Folder:** Dublin Core info for Folder.

* **Document:** Dublin Core info for Document.

* **Event:** Dublin Core info for Event.

This plugin generate a JSON format from the base API URL: http://localhost:8080/Plone/apidata/content

::

  [
    {
      "uri": "http://localhost:8080/Plone/apidata/content/News Item",
      "description": "Dublin Core info for News Item",
      "entity": "News Item"
    },
    {
      "uri": "http://localhost:8080/Plone/apidata/content/Image",
      "description": "Dublin Core info for Image",
      "entity": "Image"
    },
    {
      "uri": "http://localhost:8080/Plone/apidata/content/File",
      "description": "Dublin Core info for File",
      "entity": "File"
    },
    {
      "uri": "http://localhost:8080/Plone/apidata/content/Folder",
      "description": "Dublin Core info for Folder",
      "entity": "Folder"
    },
    {
      "uri": "http://localhost:8080/Plone/apidata/content/Document",
      "description": "Dublin Core info for Document",
      "entity": "Document"
    },
    {
      "uri": "http://localhost:8080/Plone/apidata/content/Event",
      "description": "Dublin Core info for Event",
      "entity": "Event"
    }
  ]

A JSON format for Folder content type, like this:

::

  [
    {
      "title": "News",
      "identifier": "http://localhost:8080/Plone/news",
      "uid": "07997a0ee8f14414bfcf8c146cc865f2",
      "uri": "http://localhost:8080/Plone/apidata/content/Folder/07997a0ee8f14414bfcf8c146cc865f2"
    },
    {
      "title": "Events",
      "identifier": "http://localhost:8080/Plone/events",
      "uid": "bf5aafa2c7224eb5935d174c1a9a43ff",
      "uri": "http://localhost:8080/Plone/apidata/content/Folder/bf5aafa2c7224eb5935d174c1a9a43ff"
    },
    {
      "title": "Users",
      "identifier": "http://localhost:8080/Plone/Members",
      "uid": "761536d101414a47bc0e5494f51d97f1",
      "uri": "http://localhost:8080/Plone/apidata/content/Folder/761536d101414a47bc0e5494f51d97f1"
    }
  ]


Creation
--------

This product was created by the PloneGov-BR community in a sprint at Interlegis:

http://www.softwarelivre.gov.br/plone

Special thanks to Érico Andrei!


Translations
------------

This product has been translated into

- Portuguese (thanks, Jean Ferri)
- Spanish (thanks, Leonardo J. Caballero G.)


Contribute
----------

- Issue Tracker: http://github.com/plonegovbr/collective.opendata/issues

- Source Code: http://github.com/plonegovbr/collective.opendata

- Website: http://plone.org.br

Support
-------

If you are having issues, please let us know, submit a ticket with the report http://github.com/plonegovbr/collective.opendata/issues

License
-------

The project is licensed under the GNU General Public License v2 (GPLv2).

----

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/plonegovbr/collective.opendata.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/plonegovbr/collective.opendata

.. image:: https://coveralls.io/repos/plonegovbr/collective.opendata/badge.png?branch=master
    :alt: Coveralls badge
    :target: https://coveralls.io/r/plonegovbr/collective.opendata
