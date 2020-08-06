from wagtail.core import hooks
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core.rich_text import LinkHandler
from django.utils.html import escape


# register bootstrap sample output
@hooks.register("register_rich_text_features")
def register_sample_output_styling(features):
    """ add the <samp> tag to RTE """
    feature_name =  "samp"
    type_ = "SAMP"
    tag = "samp"

    control = {
        "type": type_,
        "icon": 'fa-terminal',
        "description": "Sample Output",
        "style":{"background-color":"#F2F2F2","border-radius":"5px","padding":"3px"}
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_:tag}}
    }
    
    features.register_converter_rule("contentstate",feature_name, db_conversion)

    # register to all rich text editors by default
    features.default_features.append(feature_name)

# register bootstrap input
@hooks.register("register_rich_text_features")
def register_input_styling(features):
    """ add the <kbd> tag to RTE """
    feature_name = "kbd"
    type_ = "KBD"
    tag = "kbd"

    control = {
        "type": type_,
        "icon": 'fa-keyboard-o',
        "description": "Keyboard Input",
        "style":{"background-color":"black", "color":"white", "border-radius":"5px", "padding":"3px"}
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_:tag}}
    }
    
    features.register_converter_rule("contentstate",feature_name, db_conversion)

    # register to all rich text editors by default
    features.default_features.append(feature_name)

# register bootstrap variable
@hooks.register("register_rich_text_features")
def register_variable_styling(features):
    """ add the <var> tag to RTE """
    feature_name = "var"
    type_ = "VAR"
    tag = "var"

    control = {
        "type": type_,
        "icon": 'fa-plus',
        "description": "Variable",
        "style":{"font-style":"italic"}
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_:tag}}
    }
    
    features.register_converter_rule("contentstate",feature_name, db_conversion)

    # register to all rich text editors by default
    features.default_features.append(feature_name)



class NoFollowExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        return '<a href="%s" rel="nofollow">' % escape(href)

@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type(NoFollowExternalLinkHandler)