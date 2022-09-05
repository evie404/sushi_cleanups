import bpy
from bpy.types import Object

from .sushi_base_operator import SushiAllMeshOperator


class SUSHI_CLEANUP_SortVertexGroups(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.sort_vertex_groups"
    bl_label = "Sort All Vertex Groups By Name"
    bl_description = "Sort vertex groups by names for all objects"

    sk_tags = {"ALL", "VERTEX_GROUP", "EMPTY", "MESH", "SORT"}

    def sk_obj_exec(self, obj: Object) -> None:
        if len(obj.vertex_groups) < 1:
            return

        previously_hidden = False

        if obj.hide_viewport:
            obj.hide_viewport = False
            previously_hidden = True

        bpy.ops.object.vertex_group_sort(
            {
                "active_object": obj,
                "edit_object": obj,
                "editable_objects": [obj],
                "object": obj,
                "selected_objects": [obj],
            }
        )

        if previously_hidden:
            obj.hide_viewport = True
