from typing import List, Set

import bpy
from bpy.types import Context, Mesh, MeshLoopColor, MeshLoopColorLayer, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteEmptyVertexColorsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_empty_vertex_colors_all"
    bl_label = "[Buggy] Delete All Empty Vertex Colors"
    bl_description = "Deletes vertex colors with only default colors for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_COLOR", "EMPTY", "MESH", "DELETE"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            _delete_vertex_colors(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_empty_vertex_colors_selected"
    bl_label = "[Buggy] Delete Empty Vertex Colors"
    bl_description = (
        "Deletes vertex colors with only default colors for the selected object"
    )
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_COLOR", "EMPTY", "MESH", "DELETE"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        _delete_vertex_colors(bpy.context.active_object)

        return {"FINISHED"}


def _delete_vertex_colors(obj: Object) -> None:
    vertex_colors_to_delete: List[MeshLoopColorLayer] = []
    mesh: Mesh = obj.data

    for vertex_color in mesh.vertex_colors:
        vertex_color: MeshLoopColorLayer

        zero_color_only = True

        for loop in vertex_color.data:
            loop: MeshLoopColor

            if not zero_color_only:
                continue

            if list(loop.color) == [0.0, 0.0, 0.0, 1.0]:
                continue

            zero_color_only = False

        if zero_color_only:
            vertex_colors_to_delete.append(vertex_color)

    for vertex_color in vertex_colors_to_delete:
        if vertex_color.name not in mesh.vertex_colors:
            continue

        print(f"{obj.name}: removing color map `{vertex_color.name}`")
        mesh.vertex_colors.delete(vertex_color)
