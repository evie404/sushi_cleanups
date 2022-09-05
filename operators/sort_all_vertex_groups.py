import bpy
from bpy.types import Object

from .sushi_base_operator import SushiAllMeshOperator


class SUSHI_CLEANUP_SortVertexGroups(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.sort_vertex_groups"
    bl_label = "Sort All Vertex Groups By Name"
    bl_description = "Sort vertex groups by names for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "VERTEX_GROUP", "EMPTY", "MESH", "SORT"}

    def sk_obj_exec(self, obj: Object) -> None:
        bpy.context.view_layer.objects.active = None

        if len(obj.vertex_groups) < 1:
            return

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        bpy.ops.object.vertex_group_sort()
