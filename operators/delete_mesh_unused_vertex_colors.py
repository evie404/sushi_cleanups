from typing import List

import bpy
from bpy.types import MeshLoopColor, MeshLoopColorLayer, Object

from .sushi_base_operator import SushiAllMeshOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteUnusedVertexColorsAll(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_vertex_colors_all"
    bl_label = "Delete All Unused Vertex Colors"
    bl_description = "Deletes non-active vertex colors for all objects"

    sk_tags = {"ALL", "MESH", "UNUSED", "VERTEX_COLOR", "DELETE", "EXPERIMENTAL"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_vertex_colors(obj)


class SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_vertex_colors_selected"
    bl_label = "Delete Unused Vertex Colors"
    bl_description = "Deletes non-active vertex colors for the selected object"

    sk_tags = {"SELECTED", "MESH", "UNUSED", "VERTEX_COLOR", "DELETE", "EXPERIMENTAL"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_vertex_colors(obj)


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
        obj.data.vertex_colors.remove(vertex_color)
