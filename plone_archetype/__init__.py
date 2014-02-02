from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

example_type_schema = atapi.Schema()

ExampleTypeSchema = schemata.ATContentTypeSchema.copy()
ExampleTypeSchema += example_type_schema


class ExampleType(base.ATCTContent):
    """
    """


schemata.finalizeATCTSchema(ExampleTypeSchema)
atapi.registerType(ExampleType, 'ExampleType')
