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
from upc.genweb.kbpuc.interfaces import IInfoGeneral
from upc.genweb.kbpuc.config import PROJECTNAME
from zope.component import getMultiAdapter, getUtility

from datetime import datetime

from Products.ATContentTypes.content.document import ATDocumentSchema, ATDocument

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

#from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary

infogeneral_kbpuc_Schema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.TextField('text',
        required=False,
        searchable=True,
        storage = atapi.AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        #validators = ('isTidyHtml',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            i18n_domain='upc.genweb.kbpuc',
            label=_(u'label_info_contingut', default=u'Contingut'),
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload),
        schemata="default",
    ),

    atapi.LinesField(
        name='producte',
        widget=atapi.MultiSelectionWidget(
            format="select",
            label = _(u'label_producte', default=u'Producte'),
            description = _(u'label_producte_descr', default=u'Seleccionar el producte o productes relacionats'),
            i18n_domain='upc.genweb.kbpuc',
        ),
        languageIndependent=True,
        multiValued=False,
        schemata="default",
        vocabulary='getProductes',
        enforceVocabulary = True,
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

    atapi.StringField(
        name = 'categoria',
        required = False,
        searchable = False,
        languageIndependent=True,
        default = "getCategoria",
        widget = atapi.StringWidget(
            label = _(u'label_categoria', default=u'Categoria'),
            i18n_domain='upc.genweb.kbpuc',
            visible = {'view': 'hidden','edit': 'hidden'}
        ),
        schemata="default",
    ),

    atapi.StringField(
        name = 'registro',
        required = False,
        searchable = False,
        languageIndependent=True,
        default = "getRegistro",        
        widget = atapi.StringWidget(
            label = _(u'label_height', default=u'Registro'),
            i18n_domain='upc.genweb.kbpuc',
            visible = {'view': 'hidden','edit': 'hidden'}
        ),
        schemata="default",
    ),

))

schemata.finalizeATCTSchema(infogeneral_kbpuc_Schema, moveDiscussion=False)

infogeneral_kbpuc_Schema.changeSchemataForField('subject', 'default')
infogeneral_kbpuc_Schema.moveField('subject', after='text')

infogeneral_kbpuc_Schema.changeSchemataForField('relatedItems', 'default')
infogeneral_kbpuc_Schema.moveField('relatedItems', after='subject')

class InfoGeneral(ATDocument):
    """InfoGeneral KBPUC """

    portal_type = "InfoGeneral"
    schema = infogeneral_kbpuc_Schema

    implements(IInfoGeneral)
    
    security = ClassSecurityInfo()

    security.declarePublic('getServei')
    def getServei(self):
        return self.getParentNode().getParentNode().title

    security.declarePublic('getCategoria')
    def getCategoria(self):
        return self.getParentNode().title

    security.declarePublic('getRegistro')
    def getRegistro(self):
        portal_membership = getToolByName(self, 'portal_membership')
        if self.registro != 'getRegistro':
            user = portal_membership.getAuthenticatedMember().getUserName()
            fecha = datetime.now().ctime()
            tmp = self.registro
            tmp = tmp + user + ' ' + fecha + '@@@'
            return tmp
        return ''        

    def muestraRegistro(self):
        cad = self.registro.split('@@@')
        result = []
        for i in cad:
            if i != '':
                result.append(i)
        return result

    def getProductes(self):
        context = self.context
        ptool = getToolByName(context, 'portal_properties')
        kbpucprops = ptool.kbpuc_properties
        return kbpucprops.Productes.split('\n')
       
atapi.registerType(InfoGeneral, PROJECTNAME)

