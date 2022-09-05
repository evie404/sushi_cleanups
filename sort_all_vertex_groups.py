from typing import Set

import bpy
from bpy.types import Context, Object


class SUSHI_CLEANUP_SortVertexGroups(bpy.types.Operator):
    bl_idname = "sushi_cleanup.sort_vertex_groups"
    bl_label = "Sort Vertex Groups"
    bl_description = "Sort vertex groups by names."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        bpy.context.view_layer.objects.active = None

        for obj in bpy.data.objects:
            obj: Object

            if not obj.type == "MESH":
                continue

            if len(obj.vertex_groups) < 1:
                continue

            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

            bpy.ops.object.vertex_group_sort()

        return {"FINISHED"}
