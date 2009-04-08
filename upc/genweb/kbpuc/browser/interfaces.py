import zope.schema
from zope.interface import Interface, Attribute
from Products.CMFPlone import PloneMessageFactory as _

class IkbpucControlPanel(Interface):
    Processos = zope.schema.Text(title=u"Processos", description=u"Els processos associats als elements de la KBPUC")
    EquipsResolutors = zope.schema.Text(title=u"Equips Resolutors", description=u"Els equips resolutors dels tiquets")
    Productes = zope.schema.Text(title=u"Productes", description=u"Els productes associats als elements de la KBPUC")