from typing import List

import bpy
from bpy.types import Object

from .sushi_base_operator import SushiMeshOperator


class SUSHI_CLEANUP_DeleteSameMeshObjects(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_objects_of_same_mesh"
    bl_label = "Delete Objects with the same Mesh"
    bl_description = "Delete Objects that uses the same mesh data"

    sk_tags = {"SIMILAR", "MESH", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_mesh_objects_of_same_data(obj)


def _delete_mesh_objects_of_same_data(obj: Object) -> None:
    objs_to_delete: List[Object] = []

    for other_obj in bpy.data.objects:
        other_obj: Object

        if other_obj.name == obj.name:
            continue

        if other_obj.type != "MESH":
            continue

        if obj.data == other_obj.data:
            objs_to_delete.append(other_obj)

    objs_to_delete.append(obj)

    for del_obj in objs_to_delete:
        print(f"{obj.name}: deleting `{del_obj.name}` with same materials...")
        bpy.data.objects.remove(del_obj)
