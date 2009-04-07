# -*- coding: utf-8 -*-

"""Definition of the servei content type
"""

from zope.interface import implements, directlyProvides
from AccessControl import ClassSecurityInfo
from DateTime import DateTime

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from Products.Archetypes.atapi import Schema

from Products.Archetypes import atapi
from Products.Archetypes.public import DisplayList
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf
from Products.validation import V_REQUIRED

from upc.genweb.kbpuc import kbpucMessageFactory as _
from upc.genweb.kbpuc.interfaces import ICategoria
from upc.genweb.kbpuc.config import PROJECTNAME

from Products.ATContentTypes.content.folder import ATFolderSchema, ATFolder
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

categoria_kbpuc_Schema = ATFolderSchema.copy() + atapi.Schema((

))

schemata.finalizeATCTSchema(categoria_kbpuc_Schema, moveDiscussion=False)

class Categoria(ATFolder):
    """Categoria KBPUC """

    portal_type = "Categoria"
    schema = categoria_kbpuc_Schema

    implements(ICategoria)
    
    security = ClassSecurityInfo()
       
    security.declarePublic('getCategoria')
    def getCategoria(self):
        return self.getParentNode().title

atapi.registerType(Categoria, PROJECTNAME)

