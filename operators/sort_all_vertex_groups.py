from typing import Set

import bpy
from bpy.types import Context, Object

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_SortVertexGroups(SushiBaseOperator):
    bl_idname = "sushi_cleanup.sort_vertex_groups"
    bl_label = "Sort All Vertex Groups By Name"
    bl_description = "Sort vertex groups by names for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_GROUP", "EMPTY", "MESH", "SORT"}

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
