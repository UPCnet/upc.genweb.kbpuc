# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class InfoGeneralView(BrowserView):
    """Default view of a Informacio General
    """

    # This template will be used to render the view. An implicit variable
    # 'view' will be available in this template, referring to an instance
    # of this class. The variable 'context' will refer to the cinema folder
    # being rendered.

    __call__ = ViewPageTemplateFile('info-general-view.pt')
