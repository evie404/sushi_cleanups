from typing import Set

import bpy
from bpy.types import Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DeleteUnusedMaterials(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_unused_materials"
    bl_label = "Delete All Unused Materials"
    bl_description = "Deletes materials with no users"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "MATERIAL", "UNUSED", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for material in bpy.data.materials:
            if not material.users:
                bpy.data.materials.delete(material)

        return {"FINISHED"}
