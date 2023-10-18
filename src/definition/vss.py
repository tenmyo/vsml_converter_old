from . import regex

PROPERTY_LIST = [
    "object-length",
    "source-loop",
    "playback-speed",
    "time-margin",
    "time-margin-start",
    "time-margin-end",
    "time-padding",
    "time-padding-start",
    "time-padding-end",
    "order",
    "layer",
    "opacity",
    "width",
    "min-width",
    "max-width",
    "height",
    "min-height",
    "max-height",
    "background-color",
    "object-fit",
    "chroma-key",
    "magnification",
    "rotate",
    "border",
    "border-color",
    "border-style",
    "border-width",
    "border-bottom",
    "border-bottom-color",
    "border-bottom-style",
    "border-bottom-width",
    "border-left",
    "border-left-color",
    "border-left-style",
    "border-left-width",
    "border-right",
    "border-right-color",
    "border-right-style",
    "border-right-width",
    "border-top",
    "border-top-color",
    "border-top-style",
    "border-top-width",
    "position",
    "display",
    "top",
    "left",
    "bottom",
    "right",
    "flex-direction",
    "flex-wrap",
    "align-content",
    "justify-content",
    "align-items",
    "margin",
    "margin-top",
    "margin-left",
    "margin-bottom",
    "margin-right",
    "padding",
    "padding-top",
    "padding-left",
    "padding-bottom",
    "padding-right",
    "border-radius",
    "border-bottom-left-radius",
    "border-bottom-right-radius",
    "border-top-left-radius",
    "border-top-right-radius",
    "visibility",
    "box-shadow",
    "audio-volume",
    "audio-system",
    "font-color",
    "font-border",
    "font-border-color",
    "font-border-width",
    "font",
    "font-family",
    "font-size",
    "font-stretch",
    "font-style",
    "font-weight",
    "text-align",
    "text-decoration",
    "text-decoration-color",
    "text-decoration-line",
    "text-decoration-style",
    "text-decoration-thickness",
    "text-orientation",
    "text-overflow",
    "text-shadow",
    "line-height",
    "letter-spacing",
    "word-break",
]

COLOR_LIST = [
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "black",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "green",
    "greenyellow",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightsteelblue",
    "lightyellow",
    "lime",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen",
]

SECOND_PATTERN = "{}s".format(regex.REAL_NUMBER_PATTERN)
FRAME_PATTERN = "{}f".format(regex.REAL_NUMBER_PATTERN)

PIXEL_PATTERN = "{}px".format(regex.REAL_NUMBER_PATTERN)
RESOLUTION_WIDTH_PATTERN = "{}rw".format(regex.REAL_NUMBER_PATTERN)
RESOLUTION_HEIGHT_PATTERN = "{}rh".format(regex.REAL_NUMBER_PATTERN)
RESOLUTION_MIN_PATTERN = "{}rmin".format(regex.REAL_NUMBER_PATTERN)
RESOLUTION_MAX_PATTERN = "{}rmax".format(regex.REAL_NUMBER_PATTERN)

PERCENT_PATTERN = "{}%".format(regex.REAL_NUMBER_PATTERN)

TIME_PATTERN = "({}|{}|{})".format(
    SECOND_PATTERN, FRAME_PATTERN, PERCENT_PATTERN
)
GRAPHIC_PATTERN = "({}|{}|{}|{}|{}|{})".format(
    PIXEL_PATTERN,
    RESOLUTION_WIDTH_PATTERN,
    RESOLUTION_HEIGHT_PATTERN,
    RESOLUTION_MIN_PATTERN,
    RESOLUTION_MAX_PATTERN,
    PERCENT_PATTERN,
)

HEX_COLOR_PATTERN = "#({0}{{3}}|{0}{{4}}|{0}{{6}}|{0}{{8}})".format(
    regex.HEX_PATTERN
)
RGB_COLOR_PATTERN = r"rgb\(\s*{0}\s*,\s*{0}\s*,\s*{0}\s*\)".format(
    regex.REAL_NUMBER_PATTERN
)
RGBA_COLOR_PATTERN = r"rgba\(\s*{0}\s*,\s*{0}\s*,\s*{0}\s*,\s*{0}\s*\)".format(
    regex.REAL_NUMBER_PATTERN
)
PURE_COLOR_PATTERN = "|".join(COLOR_LIST)
COLOR_PATTERN = "({}|{}|{}|{})".format(
    PURE_COLOR_PATTERN,
    HEX_COLOR_PATTERN,
    RGB_COLOR_PATTERN,
    RGBA_COLOR_PATTERN,
)

STYLE_VALUE_PATTERN = {
    "object-length": "(fit|source|{})".format(TIME_PATTERN),
    "source-loop": "(true|false)",
    "playback-speed": PERCENT_PATTERN,
    "time-margin": r"{0}(\s+{0})?".format(TIME_PATTERN),
    "time-margin-start": TIME_PATTERN,
    "time-margin-end": TIME_PATTERN,
    "time-padding": r"{0}(\s+{0})?".format(TIME_PATTERN),
    "time-padding-start": TIME_PATTERN,
    "time-padding-end": TIME_PATTERN,
    "order": "(sequence|parallel)",
    "layer": "(single|multi)",
    "opacity": "({}|{})".format(regex.REAL_NUMBER_PATTERN, PERCENT_PATTERN),
    "width": GRAPHIC_PATTERN,
    "min-width": "",
    "max-width": "",
    "height": GRAPHIC_PATTERN,
    "min-height": "",
    "max-height": "",
    "background-color": COLOR_PATTERN,
    "object-fit": "",
    "chroma-key": "",
    "magnification": "",
    "rotate": "",
    "border": "",
    "border-color": "",
    "border-style": "",
    "border-width": "",
    "border-bottom": "",
    "border-bottom-color": "",
    "border-bottom-style": "",
    "border-bottom-width": "",
    "border-left": "",
    "border-left-color": "",
    "border-left-style": "",
    "border-left-width": "",
    "border-right": "",
    "border-right-color": "",
    "border-right-style": "",
    "border-right-width": "",
    "border-top": "",
    "border-top-color": "",
    "border-top-style": "",
    "border-top-width": "",
    "position": "",
    "display": "",
    "top": "",
    "left": "",
    "bottom": "",
    "right": "",
    "flex-direction": "",
    "flex-wrap": "",
    "align-content": "",
    "justify-content": "",
    "align-items": "",
    "margin": r"{0}(\s+{0}){{0,3}}".format(GRAPHIC_PATTERN),
    "margin-top": GRAPHIC_PATTERN,
    "margin-left": GRAPHIC_PATTERN,
    "margin-bottom": GRAPHIC_PATTERN,
    "margin-right": GRAPHIC_PATTERN,
    "padding": r"{0}(\s+{0}){{0,3}}".format(GRAPHIC_PATTERN),
    "padding-top": GRAPHIC_PATTERN,
    "padding-left": GRAPHIC_PATTERN,
    "padding-bottom": GRAPHIC_PATTERN,
    "padding-right": GRAPHIC_PATTERN,
    "border-radius": "",
    "border-bottom-left-radius": "",
    "border-bottom-right-radius": "",
    "border-top-left-radius": "",
    "border-top-right-radius": "",
    "visibility": "",
    "box-shadow": "",
    "audio-volume": PERCENT_PATTERN,
    "audio-system": "(monaural|stereo)",
    "font-color": COLOR_PATTERN,
    "font-border": r"({0}\s+{1}|{1}\s+{0})".format(
        COLOR_PATTERN, PIXEL_PATTERN
    ),
    "font-border-color": COLOR_PATTERN,
    "font-border-width": PIXEL_PATTERN,
    "font": "",
    "font-family": ".+",
    "font-size": GRAPHIC_PATTERN,
    "font-stretch": "",
    "font-style": "(normal|italic)",
    "font-weight": "(normal|bold)",
    "text-align": "",
    "text-decoration": "",
    "text-decoration-color": "",
    "text-decoration-line": "",
    "text-decoration-style": "",
    "text-decoration-thickness": "",
    "text-orientation": "",
    "text-overflow": "",
    "text-shadow": "",
    "line-height": "",
    "letter-spacing": "",
    "word-break": "",
}
