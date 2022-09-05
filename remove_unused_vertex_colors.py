from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object

from sushi_cleanups.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RemoveUnusedVertexColorsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_unused_vertex_colors_all"
    bl_label = "Remove All Unused Vertex Colors"
    bl_description = "Removes non-active vertex colors"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type == "MESH":
                _remove_unused_vertex_colors(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveUnusedVertexColorsSelected(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_unused_vertex_colors_selected"
    bl_label = "Remove Unused Vertex Colors"
    bl_description = "Removes non-active vertex colors"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_mesh(context)
        if err:
            return err

        _remove_unused_vertex_colors(bpy.context.active_object)

        return {"FINISHED"}


def _remove_unused_vertex_colors(obj: Object) -> None:
    if len(obj.data.vertex_colors) < 2:
        return

    vertex_colors_to_remove: List[MeshLoopColorLayer] = []

    for vertex_color in obj.data.vertex_colors:
        vertex_color: MeshLoopColor

        if vertex_color.active:
            continue

        vertex_colors_to_remove.append(vertex_color)

    for vertex_color in vertex_colors_to_remove:
        if vertex_color.name not in obj.data.vertex_colors:
            continue

        print(f"[{obj.name}] Removing unused vertex colors `{vertex_color.name}`")
        obj.data.vertex_colors.remove(vertex_color)
