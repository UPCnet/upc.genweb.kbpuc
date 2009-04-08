# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.component import adapts
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.schema import Bool
from zope.schema import Choice
from zope.component import getUtility

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone.app.controlpanel.form import ControlPanelForm
from plone.app.controlpanel.widgets import DropdownChoiceWidget

from zope.app.form.browser import ListSequenceWidget

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from plone.fieldsets.fieldsets import FormFieldsets

from upc.genweb.kbpuc.browser.interfaces import IkbpucControlPanel

from Products.CMFPlone.utils import safe_unicode

class KbpucControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IkbpucControlPanel)

    def __init__(self, context):
        super(KbpucControlPanelAdapter, self).__init__(context)
        ptool = getToolByName(context, 'portal_properties')
        self.props = ptool.site_properties
        self.context = ptool.kbpuc_properties
    
    Processos = ProxyFieldProperty(IkbpucControlPanel['Processos'])
    EquipsResolutors = ProxyFieldProperty(IkbpucControlPanel['EquipsResolutors'])
    Productes = ProxyFieldProperty(IkbpucControlPanel['Productes'])

class KbpucControlPanel(ControlPanelForm):

    form_fields = FormFields(IkbpucControlPanel)
    #form_fields['Processos'].custom_widget = ListSequenceWidget
    
    label = _("Configuracio CC UPCnet")
    description = _("Parametres de configuracio dels camps de lespai")
    form_name = _("Configuracio CC UPCnet")
