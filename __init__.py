rld = False

if "bpy" in locals():
    import imp

    rld = True


bl_info = {
    "name": "Sushi Cleanups",
    "author": "SushiKitty",
    "version": (0, 0, 1),
    "blender": (2, 92, 0),
    # "location": "File > Import > OWM",
    "description": "Small scripts to clean up data and objects",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    # "category": "Import-Export",
}

# if rld:
#     imp.reload(update_bones)

import bpy

from sushi_cleanups.operations import OPERATIONS_ALL, OPERATIONS_SELECTED
from sushi_cleanups.ui import UI_CLASSES

CLASSES = list(OPERATIONS_SELECTED) + list(OPERATIONS_ALL) + list(UI_CLASSES)


def register():
    for cls in CLASSES:
        print(f"registering {cls}...")
        bpy.utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        print(f"unregistering {cls}...")
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
