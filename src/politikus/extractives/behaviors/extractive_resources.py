# -*- coding: utf-8 -*-

from politikus.extractives import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.autoform import directives
from plone.app.z3cform.widget import SelectFieldWidget

class IExtractiveResourcesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IExtractiveResources(model.Schema):
    """
    """
    directives.widget(ExtractiveResources=SelectFieldWidget)
    ExtractiveResources = schema.List(
        title=_(u'Extractive Resources'),
        description=_(u'HS Code Extrative Resources'),
        default=[],
        value_type=schema.Choice(
            vocabulary='politikus.extractives.resources'
        ),
        required=False,
    )

    ExtractiveResourcesNote = schema.Text(
        title=_(u'Extractive Resource Notes'),
        description=_(u'Additional notes about resource'),
        required=False,
    )


@implementer(IExtractiveResources)
@adapter(IExtractiveResourcesMarker)
class ExtractiveResources(object):
    def __init__(self, context):
        self.context = context

    @property
    def ExtractiveResources(self):
        if safe_hasattr(self.context, 'ExtractiveResources'):
            return self.context.ExtractiveResources
        return None

    @ExtractiveResources.setter
    def ExtractiveResources(self, value):
        self.context.ExtractiveResources = value

    @property
    def ExtractiveResourceNotes(self):
        if safe_hasattr(self.context, 'ExtractiveResourceNotes'):
            return self.context.ExtractiveResourceNotes
        return None

    @ExtractiveResourceNotes.setter
    def ExtractiveResourceNotes(self, value):
        self.context.ExtractiveResourceNotes = value
