# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import politikus.extractives


class PolitikusExtractivesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=politikus.extractives)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'politikus.extractives:default')


POLITIKUS_EXTRACTIVES_FIXTURE = PolitikusExtractivesLayer()


POLITIKUS_EXTRACTIVES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLITIKUS_EXTRACTIVES_FIXTURE,),
    name='PolitikusExtractivesLayer:IntegrationTesting',
)


POLITIKUS_EXTRACTIVES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLITIKUS_EXTRACTIVES_FIXTURE,),
    name='PolitikusExtractivesLayer:FunctionalTesting',
)


POLITIKUS_EXTRACTIVES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLITIKUS_EXTRACTIVES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolitikusExtractivesLayer:AcceptanceTesting',
)
