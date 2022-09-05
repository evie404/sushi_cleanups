from typing import Dict

import bpy
from bpy.types import FCurve, Object

from .sushi_base_operator import SushiFromToOperator


class SUSHI_CLEANUP_CopyCustomPropertiesToSelected(SushiFromToOperator):
    bl_idname = "sushi_cleanup.copy_custom_properties"
    bl_label = "Copy Custom properties"
    bl_description = (
        "Copies custom properties from the active object to the selected objects"
    )

    sk_tags = {"CUSTOM_PROPERTY", "OBJECT", "COPY", "FROM_TO"}

    def sk_from_to_exec(self, from_obj: Object, to_obj: Object) -> None:
        _copy_custom_properties(from_obj, to_obj, False)


class SUSHI_CLEANUP_CopyCustomPropertiesWithDriversToSelected(SushiFromToOperator):
    bl_idname = "sushi_cleanup.copy_custom_properties_with_drivers"
    bl_label = "Copy Custom properties with Drivers"
    bl_description = "Copies custom properties and associated drivers from the active object to the selected objects"

    sk_tags = {"CUSTOM_PROPERTY", "OBJECT", "COPY", "FROM_TO", "DRIVER"}

    def sk_from_to_exec(self, from_obj: Object, to_obj: Object) -> None:
        _copy_custom_properties(from_obj, to_obj, True)


def _copy_custom_properties(
    from_obj: Object, to_obj: Object, copy_drivers: bool
) -> None:
    print(f"[{from_obj.name}] Copying custom properties to {to_obj.name} (Start)")

    # for key in from_obj.id_properties_ensure().keys():
    #     if not is_ui_prop(from_obj, key):
    #         continue

    from_props = from_obj.id_properties_ensure()

    to_obj.id_properties_ensure().clear()
    to_obj.id_properties_ensure().update(from_props)

    if copy_drivers:
        for driver in from_obj.animation_data.drivers:
            driver: FCurve
            if not driver.data_path.startswith('["'):
                continue

            if not driver.data_path.endswith('"]'):
                continue

            to_obj.animation_data.drivers.from_existing(src_driver=driver)

    print(f"[{from_obj.name}] Copying custom properties to {to_obj.name} (Finished)")


def is_ui_prop(obj: Object, key: str) -> bool:
    if key not in obj:
        return False

    try:
        return obj.id_properties_ui(key)
    except TypeError:
        return False
