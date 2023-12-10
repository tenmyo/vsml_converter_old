from typing import Any, Optional

import ffmpeg

from style import Color

origin_background_processes = {}
origin_graphic_processes: dict[str, dict[str, Any]] = {}


def get_background_process(
    resolution_text: str, background_color: Optional[Color] = None
):
    global origin_background_process
    key = "{}/{}".format(
        resolution_text,
        "transparent" if background_color is None else background_color.value,
    )
    origin_background_process = origin_background_processes.get(key)
    if origin_background_process is None:
        origin_background_process = ffmpeg.input(
            "rgbtestsrc=s={}".format(resolution_text),
            f="lavfi",
        )
        if background_color is None:
            origin_background_process = ffmpeg.filter(
                origin_background_process, "geq", a=0, r=0, g=0, b=0
            )
        else:
            origin_background_process = ffmpeg.filter(
                origin_background_process,
                "geq",
                a=background_color.a_value,
                r=background_color.r_value,
                g=background_color.g_value,
                b=background_color.b_value,
            )
    background_processes = origin_background_process.split()
    origin_background_processes[key] = background_processes[1]
    return background_processes[0]


def get_graphical_process(src_path: str, exist_audio: bool, **option):
    global origin_graphic_processes
    origin_graphic_process = origin_graphic_processes.get(src_path)
    if origin_graphic_process is None:
        process = ffmpeg.input(src_path, **option)
        origin_graphic_process = {
            "video": process.video,
            "audio": process.audio if exist_audio else None,
        }
    video_graphic_processes = origin_graphic_process["video"].split()
    origin_graphic_processes[src_path] = {
        "video": video_graphic_processes[1],
        "audio": origin_graphic_process["audio"],
    }
    return {
        "video": video_graphic_processes[0],
        "audio": origin_graphic_process["audio"],
    }
