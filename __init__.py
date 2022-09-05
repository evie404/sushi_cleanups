from typing import List, Type

bl_info = {
    "name": "Sushi Cleanups",
    "author": "SushiKitty",
    "version": (0, 1, 1),
    "blender": (2, 92, 0),
    "description": "Scripts to clean up data and objects. Useful when cleaning up imported data from other programs.",
    "location": "View3D > Sidebar > Sushi Cleanups",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Object",
}

# Script reloading (if the user calls 'Reload Scripts' from Blender)
# https://github.com/KhronosGroup/glTF-Blender-IO/blob/04e26bef903543d08947c5a9a5fea4e787b68f17/addons/io_scene_gltf2/__init__.py#L32-L54
# http://www.apache.org/licenses/LICENSE-2.0
def reload_package(module_dict_main: dict) -> None:  # type: ignore[type-arg]
    print("[Sushi Cleanups] Reloading...")
    # Lazy import to minimize initialization before reload_package()
    import importlib
    from pathlib import Path
    from typing import Any, Dict

    def reload_package_recursive(
        current_dir: Path, module_dict: Dict[str, Any]
    ) -> None:
        for path in current_dir.iterdir():
            if "__init__" in str(path) or path.stem not in module_dict:
                continue

            if path.is_file() and path.suffix == ".py":
                importlib.reload(module_dict[path.stem])
            elif path.is_dir():
                reload_package_recursive(path, module_dict[path.stem].__dict__)

    reload_package_recursive(Path(__file__).parent, module_dict_main)

    print("[Sushi Cleanups] Reloading...")


if "bpy" in locals():
    print("[Sushi Cleanups] Triggering Reload")

    reload_package(locals())


def all_classes() -> List[Type]:
    from sushi_cleanups.operators.groups import ALL_OPERATIONS
    from sushi_cleanups.preferences import SushiCleanupsAddonPreferences
    from sushi_cleanups.ui import UI_CLASSES

    return [SushiCleanupsAddonPreferences] + list(ALL_OPERATIONS) + list(UI_CLASSES)


def register():
    import bpy

    for cls in all_classes():
        print(f"[Sushi Cleanups] Registering {cls}...")
        bpy.utils.register_class(cls)


def unregister():
    import bpy

    for cls in all_classes():
        print(f"[Sushi Cleanups] Unregistering {cls}...")
        bpy.utils.unregister_class(cls)


# if __name__ == "__main__":
#     register()
