import webcolors

class Colors(object):

    @staticmethod
    def name_to_color(name, opacity=0):
        try:
            r, g, b = webcolors.name_to_rgb(name)
        except ValueError:
            r, g, b = 0, 0, 0

        return Colors._format_color(r, g, b, opacity)

    @staticmethod
    def hex_to_color(hex_string, opacity=0):
        r, g, b = webcolors.hex_to_rgb(hex_string)
        return Colors._format_color(r, g, b, opacity)

    @staticmethod
    def _format_color(r, g, b, opacity):
        alpha = 255 * (opacity / 100)
        return '{0} {1} {2} {3}'.format(r, g, b, alpha)