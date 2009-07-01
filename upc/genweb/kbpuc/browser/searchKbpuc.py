from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getMultiAdapter, getUtility
from Products.CMFCore.utils import getToolByName
from upc.genweb.kbpuc.interfaces import IServei

from plone.memoize.instance import memoize


class searchKbpuc(BrowserView):
    __call__ = ViewPageTemplateFile('searchKbpuc.pt')   