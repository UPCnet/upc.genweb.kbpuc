from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from upc.genweb.kbpuc import kbpucMessageFactory as _

# -*- extra stuff goes here -*-

class IServei(Interface):
    """A Servei Content Type
    """

class IFaq(Interface):
    """A faq Content Type
    """

