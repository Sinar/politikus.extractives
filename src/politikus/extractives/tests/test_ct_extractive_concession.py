# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from politikus.extractives.content.extractive_concession import (
    IExtractiveConcession  # NOQA E501,,,
)
from politikus.extractives.testing import (
    POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING  # noqa,,,
)
from zope.component import createObject, queryUtility

import unittest


class ExtractiveConcessionIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_extractive_concession_schema(self):
        fti = queryUtility(IDexterityFTI, name='Extractive Concession')
        schema = fti.lookupSchema()
        self.assertEqual(IExtractiveConcession, schema)

    def test_ct_extractive_concession_fti(self):
        fti = queryUtility(IDexterityFTI, name='Extractive Concession')
        self.assertTrue(fti)

    def test_ct_extractive_concession_factory(self):
        fti = queryUtility(IDexterityFTI, name='Extractive Concession')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IExtractiveConcession.providedBy(obj),
            u'IExtractiveConcession not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_extractive_concession_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Extractive Concession',
            id='extractive_concession',
        )

        self.assertTrue(
            IExtractiveConcession.providedBy(obj),
            u'IExtractiveConcession not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('extractive_concession', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('extractive_concession', parent.objectIds())

    def test_ct_extractive_concession_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Extractive Concession')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_extractive_concession_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Extractive Concession')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'extractive_concession_id',
            title='Extractive Concession container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
