from typing import Dict, Set

import bpy
from bpy.types import Context, Mesh, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_empty_vertex_groups_all"
    bl_label = "Delete All Empty Vertex Groups"
    bl_description = "Deletes vertex groups with no vertices for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_GROUP", "EMPTY", "MESH", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                _delete_empty_vertex_groups(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_empty_vertex_groups_selected"
    bl_label = "Delete Empty Vertex Groups"
    bl_description = "Deletes vertex groups with no vertices for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "VERTEX_GROUP", "EMPTY", "MESH", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        _delete_empty_vertex_groups(bpy.context.active_object)

        return {"FINISHED"}


def _delete_empty_vertex_groups(obj: Object) -> None:
    vertex_groups_before = len(obj.vertex_groups)
    vertex_groups_deleted = 0

    obj.update_from_editmode()

    used_vertex_groups: Dict[str, bool] = {}

    mesh: Mesh = obj.data

    for v in mesh.vertices:
        for g in v.groups:
            if g.weight > 0.0:
                used_vertex_groups[obj.vertex_groups[g.group].name] = True

    for vertex_group in obj.vertex_groups:
        if vertex_group.name not in used_vertex_groups:
            obj.vertex_groups.delete(vertex_group)
            vertex_groups_deleted = vertex_groups_deleted + 1

    vertex_groups_after = len(obj.vertex_groups)

    print(
        f"[{obj.name}] Deleted {vertex_groups_deleted} vertex groups ({vertex_groups_before} -> {vertex_groups_after})"
    )
