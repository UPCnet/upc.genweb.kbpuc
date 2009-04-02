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

    def getFriendlyKbpuctypes(self):
        return ['Servei','Faq','Categoria','Procediment','InfoGeneral']
   
    def getProducte(self):
        """Return a list of metadata fields from portal_catalog.
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Procediment',review_state='published')
        new_list=[]
        for f in mt:
            new_list.append(f.getProducte)
        return new_list

