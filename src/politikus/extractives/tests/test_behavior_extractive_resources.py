# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from politikus.extractives.behaviors.extractive_resources import (
    IExtractiveResourcesMarker,
)
from politikus.extractives.testing import (
    POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING  # noqa,
)
from zope.component import getUtility

import unittest


class ExtractiveResourcesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_extractive_resources(self):
        behavior = getUtility(IBehavior, 'politikus.extractives.extractive_resources')
        self.assertEqual(
            behavior.marker,
            IExtractiveResourcesMarker,
        )
