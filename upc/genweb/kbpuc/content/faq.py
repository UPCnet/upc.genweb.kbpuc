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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from AccessControl import ClassSecurityInfo

faq_kbpuc_Schema = ATDocumentSchema.copy() + atapi.Schema((

     atapi.LinesField('servicios',
                required=False,
                vocabulary='listaServicios',
                enforceVocabulary=True,
                widget=atapi.InAndOutWidget(
                        label="Llista de Serveis",
                        label_msgid="upc.genweb.kbpuc.llista_serveis",
                        description="Seleccionar els serveis de la llista.",
                        description_msgid="upc.genweb.kbpuc.llista_serveis_descr",
                        i18n_domain = "upc.genweb.kbpuc"),
     ),

    atapi.StringField(
        name = 'servei',
        required = False,
        searchable = False,
        languageIndependent=True,
        default = "getServei",
        widget = atapi.StringWidget(
            label = _(u'label_servei', default=u'Servei'),
            i18n_domain='upc.genweb.kbpuc',
            visible = {'view': 'hidden','edit': 'hidden'}
        ),
        schemata="default",
    ),


))

schemata.finalizeATCTSchema(faq_kbpuc_Schema, moveDiscussion=False)

class Faq(ATDocument):
    """FAQ KBPUC """

    portal_type = "Faq"
    schema = faq_kbpuc_Schema

    implements(IFaq)

    security = ClassSecurityInfo()

    security.declareProtected(View, 'listaServicios')
    def listaServicios(self):
        """Return a list of metadata fields from portal_catalog.
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',sort_on='Date')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        new_list.sort()
        return new_list

    def serviciosEnlace(self):
        serveis = self.servicios
        new = []
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',review_state='published')

        for i in serveis:
            for j in mt:
                if i==j.Title:
                    new.append(dict(titol = j.Title,
                                    url = j.getURL()
                              ))
        return new

    security.declarePublic('getServei')
    def getServei(self):
        return self.getParentNode().getParentNode().title


atapi.registerType(Faq, PROJECTNAME)

