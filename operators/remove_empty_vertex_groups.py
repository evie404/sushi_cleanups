from typing import Dict, Set

import bpy
from bpy.types import Context, Mesh, Object

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RemoveEmptyVertexGroupsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_vertex_groups_all"
    bl_label = "Remove All Empty Vertex Groups"
    bl_description = "Removes vertex groups with no vertices for all objects"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                _remove_empty_vertex_groups(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveEmptyVertexGroupsSelected(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_vertex_groups_selected"
    bl_label = "Remove Empty Vertex Groups"
    bl_description = "Removes vertex groups with no vertices for the selected object"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_mesh(context)
        if err:
            return err

        obj = bpy.context.active_object
        _remove_empty_vertex_groups(obj)

        return {"FINISHED"}


def _remove_empty_vertex_groups(obj: Object) -> None:
    vertex_groups_before = len(obj.vertex_groups)
    vertex_groups_removed = 0

    obj.update_from_editmode()

    used_vertex_groups: Dict[str, bool] = {}

    mesh: Mesh = obj.data

    for v in mesh.vertices:
        for g in v.groups:
            if g.weight > 0.0:
                used_vertex_groups[obj.vertex_groups[g.group].name] = True

    for vertex_group in obj.vertex_groups:
        if vertex_group.name not in used_vertex_groups:
            obj.vertex_groups.remove(vertex_group)
            vertex_groups_removed = vertex_groups_removed + 1

    vertex_groups_after = len(obj.vertex_groups)

    print(
        f"[{obj.name}] Removed {vertex_groups_removed} vertex groups ({vertex_groups_before} -> {vertex_groups_after})"
    )
