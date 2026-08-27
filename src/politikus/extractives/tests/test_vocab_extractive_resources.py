# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from politikus.extractives.testing import (
    POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING  # noqa,,,
)
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory, IVocabularyTokenized

import unittest


class ExtractiveResourcesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocab_extractive_resources(self):
        vocab_name = 'politikus.extractives.resources'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        terms = list(vocabulary)
        self.assertTrue(len(terms) > 0)
