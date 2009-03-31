from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getMultiAdapter, getUtility
from Products.CMFCore.utils import getToolByName
from upc.genweb.kbpuc.interfaces import IServei

from plone.memoize.instance import memoize

class ServeiView(BrowserView):
    """Default view of a fitxa
    """

    # This template will be used to render the view. An implicit variable
    # 'view' will be available in this template, referring to an instance
    # of this class. The variable 'context' will refer to the cinema folder
    # being rendered.

    __call__ = ViewPageTemplateFile('servei-view.pt')

# Buscador de servicios
class cercaServeis(BrowserView):
    __call__ = ViewPageTemplateFile('cerca-serveis.pt')

