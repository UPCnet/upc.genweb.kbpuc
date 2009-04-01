# -*- coding: utf-8 -*-

"""Definition of the faq content type
"""

from zope.interface import implements, directlyProvides
from AccessControl import ClassSecurityInfo
from DateTime import DateTime

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent

from Products.Archetypes import atapi
from Products.Archetypes.public import DisplayList
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.configuration import zconf
from Products.validation import V_REQUIRED

from upc.genweb.kbpuc import kbpucMessageFactory as _
from upc.genweb.kbpuc.interfaces import IProcediment
from upc.genweb.kbpuc.config import PROJECTNAME

from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

procediment_kbpuc_Schema = ATDocumentSchema.copy() + atapi.Schema((

))

schemata.finalizeATCTSchema(procediment_kbpuc_Schema, moveDiscussion=False)

class Procediment(ATDocument):
    """FAQ KBPUC """

    portal_type = "Procediment"
    schema = procediment_kbpuc_Schema

    implements(IProcediment)

atapi.registerType(Procediment, PROJECTNAME)

