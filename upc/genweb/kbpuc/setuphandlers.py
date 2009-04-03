# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from Products.ATVocabularyManager.config import TOOL_TITLE
from Products.CMFPlone.utils import _createObjectByType
from DateTime import DateTime

def setupVarious(context):

    # Only run step if a flag file is present (e.g. not an extension profile)
    if context.readDataFile('upc.genwebupc.kbpuc_various.txt') is None:
        return
        
    # Add additional setup code here
    portal = context.getSite()

    voctool = getToolByName(portal, 'portal_vocabularies')
    try:
        producte_vocabulary = _createObjectByType('SimpleVocabulary', voctool, 'producte_vocabulary')
        keywords = [ (u"Intranet", u"30400 - Servei Intranet UPCnet"),
                     (u"Genweb", u"30430 - Servei de GenWeb 3.0"),
                     (u"Correu", u"23233 - Correu K2"),
                     (u"Xarxa", u"99999 - Xarxa Troncal UPC"),
                     ]
        for keyword in keywords:
            object = _createObjectByType('SimpleVocabularyTerm', producte_vocabulary, keyword[0])
            object.setTitle(keyword[1])
            object.setLanguage('ca')            
            object.reindexObject()
    except:
        pass
       

    try:
        equips_vocabulary = _createObjectByType('SimpleVocabulary', voctool, 'equips_vocabulary')
        typologies = [ (u"bo-aps", u"BackOffice Aplicacions i Serveis Finals"),
                       (u"bo-inf", u"BackOffice Infrastructures"),
                       (u"bo-mirr", u"BackOffice Monitorització i Resposta Ràpida"),
                       (u"pt", u"Projectes Tecnològics"),
                       (u"fo", u"FrontOffice"),
                       ]
        for typology in typologies:
            object = _createObjectByType('SimpleVocabularyTerm', equips_vocabulary, typology[0])
            object.setTitle(typology[1])
            object.setLanguage('ca')
            object.reindexObject()        
    except:
        pass      
    
    try:
        tipus_vocabulary = _createObjectByType('SimpleVocabulary', voctool, 'tipus_vocabulary')
        typologies = [ (u"RIN", u"RIN - Resoldre Incidències"),
                       (u"AUS", u"AUS - Atendre usuaris"),
                       (u"PTI", u"PTI - Petició"),
                       ]
        for typology in typologies:
            object = _createObjectByType('SimpleVocabularyTerm', tipus_vocabulary, typology[0])
            object.setTitle(typology[1])
            object.setLanguage('ca')
            object.reindexObject()        
    except:
        pass  

