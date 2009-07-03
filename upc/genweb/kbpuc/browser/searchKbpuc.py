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
        mt = portal_catalog.searchResults(portal_type = 'Servei', sort_on='sortable_title', sort_order='ascending')        

        results = []       
        res = []        
          
        for serv in mt:            
            c = '0'                    
#            results.append(serv.Title);
            for dt in data:               
                if dt.portal_type != 'Servei':
                        
                     if dt.portal_type == 'Categoria':
                          if c == '0':
                             results.append(serv) 
                             c = '1' 
                          if dt.getObject().getParentNode().UID() == serv.getObject().UID():                          
                             results.append(dt)   
                          else:
                              continue                           
                     else:
                          if dt.getObject().getParentNode().getParentNode().UID() == serv.getObject().UID():                               
                              results.append(dt)             
            #import pdb; pdb.set_trace() 
            res.append(results)                
#            res.sort()                           
        return res

#    def serveis(self, data):
#        portal_catalog = getToolByName(self, 'portal_catalog')
#        mt = portal_catalog.searchResults(portal_type = 'Servei')    
#
#        new_list=[]
#        for f in mt:
#            new_list.append(f.Title)
#        new_list.sort()
#        
#        return new_list
        