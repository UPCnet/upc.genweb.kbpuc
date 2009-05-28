# -*- coding: utf-8 -*-

"""Definition of the Procediment content type
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
from datetime import datetime

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

#from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary

procediment_kbpuc_Schema = ATDocumentSchema.copy() + atapi.Schema((

    atapi.TextField('informacio',
        required=False,
        searchable=True,
        storage = atapi.AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        #validators = ('isTidyHtml',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            i18n_domain='upc.genweb.kbpuc',
            label=_(u'label_informacio_entrada', default=u'Informació entrada'),
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload),
        schemata="default",
    ),

    atapi.LinesField(
        name='producte',
        widget=atapi.MultiSelectionWidget(
            format="select",
            label = _(u'label_producte', default=u'Producte'),
            i18n_domain='upc.genweb.kbpuc',
        ),
        languageIndependent=True,
        multiValued=False,
        schemata="default",
        vocabulary='getProductes',
        enforceVocabulary = True,
        
    ),

    atapi.StringField(
        name='tipus_document',
        required = False,
        widget=atapi.MultiSelectionWidget(
            label = _(u'tipus_document', default=u'Procés'),
            format = 'checkbox',
            i18n_domain='upc.genweb.kbpuc',
        ),
        languageindependent=True,
        vocabulary='getProcessos',
        schemata="default",
    ),

    atapi.LinesField('equip',
        required=False,
        vocabulary='getEquips',
        enforceVocabulary=True,
        widget=atapi.InAndOutWidget(
            label="Equips a qui assignar el tiquet",
            label_msgid="lista_equips",
            description="",
            description_msgid="lista_equips_description",
            i18n_domain = "upc.genweb.kbpuc"),                  
    ),

    atapi.TextField('text',
        required=False,
        searchable=True,
        storage = atapi.AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        #validators = ('isTidyHtml',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
            i18n_domain='upc.genweb.kbpuc',
            label=_(u'label_procediment', default=u'Procediment'),
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload),
        schemata="default",
    ),

    atapi.StringField(
        name = 'registro_p',
        required = False,
        searchable = False,
        languageIndependent=True,
        default = 'getRegistro_p',        
        widget = atapi.StringWidget(
            label = _(u'label_height', default=u'Registro'),
            i18n_domain='upc.genweb.kbpuc',
            visible = {'edit': 'hidden'}
        ),
        schemata="default",
    ),

))

schemata.finalizeATCTSchema(procediment_kbpuc_Schema, moveDiscussion=False)

procediment_kbpuc_Schema.changeSchemataForField('subject', 'default')
procediment_kbpuc_Schema.moveField('subject', after='title')

procediment_kbpuc_Schema.moveField('text', after='equip')

procediment_kbpuc_Schema.changeSchemataForField('relatedItems', 'default')
procediment_kbpuc_Schema.moveField('relatedItems', after='registro_p')
procediment_kbpuc_Schema['description'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

class Procediment(ATDocument):
    """Procediment KBPUC """

    portal_type = "Procediment"
    schema = procediment_kbpuc_Schema

    implements(IProcediment)

    security = ClassSecurityInfo()

    security.declarePublic('getRegistro_p')
    def getRegistro_p(self):
        portal_membership = getToolByName(self, 'portal_membership')
        if self.registro_p != 'getRegistro_p':
            user = portal_membership.getAuthenticatedMember().getUserName()
            fecha = datetime.now().ctime()
            tmp = self.registro_p
            tmp = tmp + user + ' ' + fecha + '@@@'
            return tmp
        return ''

    def muestraRegistro_p(self):
        cad = self.registro_p.split('@@@')
        result = []
        for i in cad:
            if i != '':
                result.append(i)
        return result

    def getProcessos(self):
        context = self.context
        ptool = getToolByName(context, 'portal_properties')
        kbpucprops = ptool.kbpuc_properties
        return kbpucprops.Processos.split('\n')

    def getProductes(self):
        context = self.context
        ptool = getToolByName(context, 'portal_properties')
        kbpucprops = ptool.kbpuc_properties
        return kbpucprops.Productes.split('\n')

    def getEquips(self):
        context = self.context
        ptool = getToolByName(context, 'portal_properties')
        kbpucprops = ptool.kbpuc_properties
        return kbpucprops.EquipsResolutors.split('\n')

atapi.registerType(Procediment, PROJECTNAME)

