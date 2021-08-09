import xml.etree.ElementTree as ET

# This adds the viewBox attribute to allow for dynamic scaling when the SVG is
# added to HTML pages. This will make the generated SVG diverge from the output
# of running REViewer directly. It's however probably an oversight to not have
# a viewBox in the first place.

# A possible performance improvement would be to not do a write here and instead
# pass on the data.

def add_viewbox_to_svg(root):
    width = root.attrib['width']
    height = root.attrib['height']
    root.set('viewBox', f'0 0 {width} {height}')

def modify_svg(path_to_svg):
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    tree = ET.parse(path_to_svg)
    root = tree.getroot()
    add_viewbox_to_svg(root)
    tree.write(path_to_svg)
