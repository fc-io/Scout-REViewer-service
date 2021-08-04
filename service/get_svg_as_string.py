def get_svg_as_string(path_to_svg):
    with open(path_to_svg, 'r') as svg_file:
        svg = svg_file.read()

    return svg
