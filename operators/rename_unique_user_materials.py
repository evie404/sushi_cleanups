from typing import Dict, List, Set

import bpy
from bpy.types import Context, Material, Object


class SUSHI_CLEANUP_RenameUniqueUserMaterials(bpy.types.Operator):
    bl_idname = "sushi_cleanup.rename_unique_user_materials"
    bl_label = "Rename All Single-User Materials"
    bl_description = "Renames materials that only have one user to their user's name"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        material_users: Dict[Material, List[Object]] = {}

        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "MESH":
                continue

            if not obj.material_slots or len(obj.material_slots) != 1:
                continue

            material = obj.material_slots[0].material

            if material not in material_users:
                material_users[material] = []

            material_users[material].append(obj)

        for material, users in material_users.items():
            if len(users) != 1:
                continue

            # if material has an unique user, rename to name of object
            material.name = users[0].name

        return {"FINISHED"}
