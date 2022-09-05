from typing import Dict, Set

import bpy
from bpy.types import Context, Object


class SUSHI_CLEANUP_RemoveEmptyVertexGroups(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_empty_vertex_groups"
    bl_label = "Remove Empty Vertex Groups"
    bl_description = "Removes vertex groups with no vertices."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                self._remove_empty_vertex_groups(obj)

        return {"FINISHED"}

    def _remove_empty_vertex_groups(self, obj: Object) -> None:
        vertex_groups_before = len(obj.vertex_groups)
        vertex_groups_removed = 0

        obj.update_from_editmode()

        used_vertex_groups: Dict[str, bool] = {}

        for v in obj.data.vertices:
            for g in v.groups:
                if g.weight > 0.0:
                    used_vertex_groups[obj.vertex_groups[g.group].name] = True

        for vertex_group in obj.vertex_groups:
            if vertex_group.name not in used_vertex_groups:
                obj.vertex_groups.remove(vertex_group)
                vertex_groups_removed = vertex_groups_removed + 1

        vertex_groups_after = len(obj.vertex_groups)

        print(
            f"{obj.name}: removed {vertex_groups_removed} vertex groups ({vertex_groups_before} -> {vertex_groups_after})"
        )
