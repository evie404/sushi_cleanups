from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object

from sushi_cleanups.base_operation import SushiBaseOperation


class SUSHI_CLEANUP_RemoveEmptyColorMapsAll(SushiBaseOperation):
    bl_idname = "sushi_cleanup.remove_empty_color_maps_all"
    bl_label = "Remove Empty Color Maps (Buggy)"
    bl_description = "Removes color maps with only default colors."
    bl_options = {"UNDO"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            _remove_color_maps(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveEmptyColorMapsSelected(SushiBaseOperation):
    bl_idname = "sushi_cleanup.remove_empty_color_maps_selected"
    bl_label = "Remove Empty Color Maps (Buggy)"
    bl_description = "Removes color maps with only default colors."
    bl_options = {"UNDO"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_mesh(context)
        if err:
            return err

        obj = bpy.context.active_object
        _remove_color_maps(obj)

        return {"FINISHED"}


def _remove_color_maps(obj: Object) -> None:
    color_maps_to_remove: List[MeshLoopColorLayer] = []

    for color_map in obj.data.vertex_colors:
        color_map: MeshLoopColorLayer

        zero_color_only = True

        for loop in color_map.data:
            loop: MeshLoopColor

            if not zero_color_only:
                continue

            if list(loop.color) == [0.0, 0.0, 0.0, 1.0]:
                continue

            zero_color_only = False

        if zero_color_only:
            color_maps_to_remove.append(color_map)

    for color_map in color_maps_to_remove:
        if color_map.name not in obj.data.vertex_colors:
            continue

        print(f"{obj.name}: removing color map `{color_map.name}`")
        obj.data.vertex_colors.remove(color_map)
