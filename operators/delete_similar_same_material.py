from typing import List

import bpy
from bpy.types import Object

from sushi_cleanups.operators.sushi_base_operator import SushiMeshOperator


class SUSHI_CLEANUP_DeleteSameMaterialObjects(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_objects_of_same_material"
    bl_label = "Delete Objects with same Material"
    bl_description = "\n".join(
        [
            "Delete all objects that uses the selected mesh's materials in the same order.",
            "",
            "Requires material slots to be in the same order but does not require the same vertices for each slot",
        ]
    )

    sk_tags = {"SIMILAR", "MESH", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_mesh_objects_of_same_material(obj)


def _delete_mesh_objects_of_same_material(obj: Object) -> None:
    if not obj.material_slots:
        return

    objs_to_delete: List[Object] = []

    for other_obj in bpy.data.objects:
        other_obj: Object

        if other_obj.name == obj.name:
            continue

        if other_obj.type != "MESH":
            continue

        if not other_obj.material_slots:
            continue

        if len(other_obj.material_slots) != len(obj.material_slots):
            continue

        same_materials = True

        for i in range(0, len(other_obj.material_slots)):
            if not same_materials:
                break

            if other_obj.material_slots[i].material != obj.material_slots[i].material:
                same_materials = False

        if same_materials:
            objs_to_delete.append(other_obj)

    objs_to_delete.append(obj)

    for del_obj in objs_to_delete:
        print(f"{obj.name}: deleting `{del_obj.name}` with same materials...")
        bpy.data.objects.remove(del_obj)
