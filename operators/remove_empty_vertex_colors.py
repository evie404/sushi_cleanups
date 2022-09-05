from typing import List, Set

import bpy
from bpy.types import Context, Mesh, MeshLoopColor, MeshLoopColorLayer, Object

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RemoveEmptyVertexColorsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_vertex_colors_all"
    bl_label = "[Buggy] Remove All Empty Vertex Colors"
    bl_description = "Removes vertex colors with only default colors for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_COLOR", "EMPTY", "MESH", "REMOVE"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            _remove_vertex_colors(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveEmptyVertexColorsSelected(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_vertex_colors_selected"
    bl_label = "[Buggy] Remove Empty Vertex Colors"
    bl_description = (
        "Removes vertex colors with only default colors for the selected object"
    )
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_COLOR", "EMPTY", "MESH", "REMOVE"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_mesh(context)
        if err:
            return err

        obj = bpy.context.active_object
        _remove_vertex_colors(obj)

        return {"FINISHED"}


def _remove_vertex_colors(obj: Object) -> None:
    vertex_colors_to_remove: List[MeshLoopColorLayer] = []
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
            vertex_colors_to_remove.append(vertex_color)

    for vertex_color in vertex_colors_to_remove:
        if vertex_color.name not in mesh.vertex_colors:
            continue

        print(f"{obj.name}: removing color map `{vertex_color.name}`")
        mesh.vertex_colors.remove(vertex_color)
