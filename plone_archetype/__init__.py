from Products.Archetypes import atapi
from Products.CMFCore import utils


PROJECT_NAME = 'Example type'


def initialize(context):
    """
    """

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(PROJECT_NAME),
        PROJECT_NAME)


    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
