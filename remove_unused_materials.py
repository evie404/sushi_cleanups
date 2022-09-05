from typing import Set

import bpy
from bpy.types import Context


class SUSHI_CLEANUP_RemoveUnusedMaterials(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_materials"
    bl_label = "Remove Unused Materials"
    bl_description = "Removes materials with no users."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for material in bpy.data.materials:
            if not material.users:
                bpy.data.materials.remove(material)

        return {"FINISHED"}
