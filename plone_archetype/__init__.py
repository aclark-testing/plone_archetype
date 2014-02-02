from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.CMFCore import utils
from zope.interface import Interface
from zope.interface import implements
from zope import schema


PROJECT_NAME = 'Example type'


def initialize(context):
    """
    """

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECT_NAME),
        PROJECT_NAME)


    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (PROJECT_NAME, atype.portal_type),
            content_types=(atype, ),
            permission='ExampleType: Add Example Type',
            extra_constructors=(constructor,),
            ).initialize(context)
