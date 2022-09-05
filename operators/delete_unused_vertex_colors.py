from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteUnusedVertexColorsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_unused_vertex_colors_all"
    bl_label = "Delete All Unused Vertex Colors"
    bl_description = "Deletes non-active vertex colors for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "MESH", "UNUSED", "VERTEX_COLOR", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type == "MESH":
                _delete_unused_vertex_colors(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_vertex_colors_selected"
    bl_label = "Delete Unused Vertex Colors"
    bl_description = "Deletes non-active vertex colors for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "MESH", "UNUSED", "VERTEX_COLOR", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        _delete_unused_vertex_colors(bpy.context.active_object)

        return {"FINISHED"}


def _delete_unused_vertex_colors(obj: Object) -> None:
    if len(obj.data.vertex_colors) < 2:
        return

    vertex_colors_to_delete: List[MeshLoopColorLayer] = []

    for vertex_color in obj.data.vertex_colors:
        vertex_color: MeshLoopColor

        if vertex_color.active:
            continue

        vertex_colors_to_delete.append(vertex_color)

    for vertex_color in vertex_colors_to_delete:
        if vertex_color.name not in obj.data.vertex_colors:
            continue

        print(f"[{obj.name}] Removing unused vertex colors `{vertex_color.name}`")
        obj.data.vertex_colors.delete(vertex_color)
