# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from politikus.extractives import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ExtractivesView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('extractives_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(ExtractivesView, self).__call__()
