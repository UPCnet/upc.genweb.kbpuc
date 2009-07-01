from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getMultiAdapter, getUtility
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize


class searchKbpuc(BrowserView):
    __call__ = ViewPageTemplateFile('searchKbpuc.pt')   

    def datahandler(self, data):
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei')

        results = []
        res = []

        for serv in mt:
            for dt in data:
                if dt.portal_type != 'Servei':
                     if dt.portal_type == 'Categoria':
                          if dt.getObject().getParentNode().UID() == serv.getObject().UID():
                              results.append(dt)
                     else:
                          if dt.getObject().getParentNode().getParentNode().UID() == serv.getObject().UID():
                              results.append(dt)
            res.append(results)
        return res
