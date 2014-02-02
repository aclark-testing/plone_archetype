from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from zope.interface import Interface
from zope.interface import implements
from zope import schema

example_type_schema = atapi.Schema()

ExampleTypeSchema = schemata.ATContentTypeSchema.copy()
ExampleTypeSchema += example_type_schema


class IExampleType(Interface):
    """ 
    """ 
    newfield = schema.TextLine()


class ExampleType(base.ATCTContent):
    """
    """
    implements(IExampleType)


schemata.finalizeATCTSchema(ExampleTypeSchema)
atapi.registerType(ExampleType, 'ExampleType')
