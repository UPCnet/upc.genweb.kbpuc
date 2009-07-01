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
   
    def getProductes(self):
        context = self.context
        ptool = getToolByName(context, 'portal_properties')
        kbpucprops = ptool.kbpuc_properties
        return kbpucprops.Productes.split('\n')


    def getProducte(self):
        """Return a list of metadata fields from portal_catalog.
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Procediment')
        new_list=[]
        for f in mt:
            new_list.append(f.getProducte)
        return new_list

    def listServ(self):
        """Return a list of metadata fields from portal_catalog.
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',sort_on='Date')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        new_list.sort()
        return new_list

    def getCategoria(self):
        """Return a list of metadata fields from portal_catalog.
        """     
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Categoria')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)        
        new_list.sort()
        return new_list

