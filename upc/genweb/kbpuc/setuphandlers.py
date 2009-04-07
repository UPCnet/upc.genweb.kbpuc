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
        keywords = [ (u"DRAC-Curriculum", u"DRAC-Curriculum"),
                     (u"DRAC-Activitats", u"DRAC-Activitats"),
                     (u"DRAC-Consultes", u"DRAC Consultes Generals"),
                     (u"Fenix ", u"Fenix"),
                     (u"Directori ", u"Directori/Intranet"),
                     (u"Sense", u"Sense servei"),
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
        typologies = [ (u"ATIC", u"ATIC"),
                       (u"DRAC-1", u"Suport DRAC 1er nivell"),
                       (u"DRAC-OTRDI", u"Suport DRAC 2on nivell (OTRDI)"),
                       (u"DRAC-CTT", u"Suport DRAC 2on nivell (CTT)"),
                       (u"DRAC-SP", u"Suport DRAC 2on nivell (SP)"),
                       (u"DRAC-CTT", u"Suport DRAC 2on nivell (CTT)"),                       
                       (u"DRAC-Biblioteques", u"Suport DRAC 2on nivell (Biblioteques)"),
                       (u"PS", u"Projectes software"),
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
        typologies = [ (u"RIN", u"RIN-Resoldre Incidències"),
                       (u"AUS", u"AUS-Atendre usuaris"),
                       (u"PTI", u"PTI-Petició"),
                       ]
        for typology in typologies:
            object = _createObjectByType('SimpleVocabularyTerm', tipus_vocabulary, typology[0])
            object.setTitle(typology[1])
            object.setLanguage('ca')
            object.reindexObject()        
    except:
        pass  

