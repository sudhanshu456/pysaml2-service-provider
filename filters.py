# filters.py
import xml.dom.minidom
from markupsafe import Markup
from jinja2 import pass_context

def format_xml(value):
    """Formats the XML string for better readability."""
    xml_dom = xml.dom.minidom.parseString(value)
    pretty_xml = xml_dom.toprettyxml()
    return pretty_xml

@pass_context
def format_xml_filter(context, value):
    """Jinja filter to format the XML string for better readability."""
    formatted_xml = format_xml(value)
    return Markup(formatted_xml)