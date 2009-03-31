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
from upc.genweb.kbpuc.interfaces import IFaq
from upc.genweb.kbpuc.config import PROJECTNAME

from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument
from Products.ATContentTypes.content.folder import ATFolderSchema, ATFolder

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

faq_kbpuc_Schema = ATFolderSchema.copy() + ATDocumentSchema.copy() + atapi.Schema((

))

schemata.finalizeATCTSchema(faq_kbpuc_Schema, moveDiscussion=False)

class Faq(ATDocument, ATFolder):
    """FAQ KBPUC """

    portal_type = "Faq"
    schema = faq_kbpuc_Schema

    implements(IFaq)

atapi.registerType(Faq, PROJECTNAME)

