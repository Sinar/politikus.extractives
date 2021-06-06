# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from politikus.extractives.testing import (
    POLITIKUS_EXTRACTIVES_FUNCTIONAL_TESTING,
    POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING,
)
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_extractives_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='extractives-view'
        )
        self.assertTrue(view.__name__ == 'extractives-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in extractives-view'
        # )

    def test_extractives_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='extractives-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = POLITIKUS_EXTRACTIVES_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
