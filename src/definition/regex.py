REAL_NUMBER_PATTERN = r"-?(?:\d+\.?\d*|\.\d+)"
HEX_PATTERN = "[0-9a-f]"

SECOND_PATTERN = f"{REAL_NUMBER_PATTERN}s"
FRAME_PATTERN = f"{REAL_NUMBER_PATTERN}f"

PIXEL_PATTERN = f"{REAL_NUMBER_PATTERN}px"
RESOLUTION_WIDTH_PATTERN = f"{REAL_NUMBER_PATTERN}rw"
RESOLUTION_HEIGHT_PATTERN = f"{REAL_NUMBER_PATTERN}rh"
RESOLUTION_MIN_PATTERN = f"{REAL_NUMBER_PATTERN}rmin"
RESOLUTION_MAX_PATTERN = f"{REAL_NUMBER_PATTERN}rmax"

PERCENT_PATTERN = f"{REAL_NUMBER_PATTERN}%"

TIME_PATTERN = f"({SECOND_PATTERN}|{FRAME_PATTERN}|{PERCENT_PATTERN})"
GRAPHIC_PATTERN = f"({PIXEL_PATTERN}|{RESOLUTION_WIDTH_PATTERN}|{RESOLUTION_HEIGHT_PATTERN}|{RESOLUTION_MIN_PATTERN}|{RESOLUTION_MAX_PATTERN}|{PERCENT_PATTERN})"

HEX_COLOR_PATTERN = f"#({HEX_PATTERN}{{3}}|{HEX_PATTERN}{{4}}|{HEX_PATTERN}{{6}}|{HEX_PATTERN}{{8}})"
RGB_COLOR_PATTERN = fr"rgb\(\s*{REAL_NUMBER_PATTERN}\s*,\s*{REAL_NUMBER_PATTERN}\s*,\s*{REAL_NUMBER_PATTERN}\s*\)"
RGBA_COLOR_PATTERN = fr"rgba\(\s*{REAL_NUMBER_PATTERN}\s*,\s*{REAL_NUMBER_PATTERN}\s*,\s*{REAL_NUMBER_PATTERN}\s*,\s*{REAL_NUMBER_PATTERN}\s*\)"
COLOR_PATTERN = f"({HEX_COLOR_PATTERN}|{RGB_COLOR_PATTERN}|{RGBA_COLOR_PATTERN})"
