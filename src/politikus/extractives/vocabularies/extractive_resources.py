# -*- coding: utf-8 -*-

from plone.dexterity.interfaces import IDexterityContent
# from plone import api
from politikus.extractives import _
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class ExtractiveResources(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem(u'282570', _(u'''
            Molybdenum oxides and hydroxides
            ''')),
            VocabItem(u'273', _(u'''
            Stone, sand and gravel
            ''')),
            VocabItem(u'270111', _(u'''
            Coal; anthracite, whether or not pulverised, but not
            agglomerated
            ''')),
            VocabItem(u'270112', _(u'''
            Coal; bituminous, whether or not pulverised, but not
            agglomerated ''')),
            VocabItem(u'2505', _(u''' Sands of all kinds; natural,
            whether or not coloured, other than metal-bearing sands of
            chapter 26 ''')),
            VocabItem(u'281', _(u'''
            Iron ore and concentrates
            ''')),
            VocabItem(u'2833', _(u'''
            Bauxite and concentrates of aluminium
            ''')),
            VocabItem(u'2871', _(u'''
            Copper ore and concentrates; copper matte; cement copper
            ''')),
            VocabItem(u'7103', _(u'''
            Precious (excluding diamond) and semi-precious stone;
            worked, graded, not strung, mounted, set; ungraded precious
            (excluding diamond) and semi-precious stone, temporarily
            strung for convenience of transport ''')),
            VocabItem(u'7108', _(u'''
            Gold (including gold plated with platinum) unwrought or in
            semi-manufactured forms, or in powder form
            ''')),
            VocabItem(u'710310', _(u'''
            Stones; precious (other than diamonds) and semi-precious
            stones, unworked or simply sawn or roughly shaped, not
            strung, mounted or set
            ''')),
            VocabItem(u'2521', _(u'''
            Limestone flux; limestone and other calcareous stone, of a kind used for the manufacture of lime or cement
            ''')),
        ]

        # Fix context if you are using the vocabulary in DataGridField.
        # See https://github.com/collective/collective.z3cform.datagridfield/issues/31:  # NOQA: 501
        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


ExtractiveResourcesFactory = ExtractiveResources()
