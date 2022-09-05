from typing import Set

import bpy
from bpy.types import Armature, Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DeleteUnusedArmatures(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_unused_armatures"
    bl_label = "Delete All Unused Armatures"
    bl_description = "Deletes armature data with no users"

    sk_tags = {"ALL", "ARMATURE", "UNUSED", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for armature in bpy.data.armatures:
            armature: Armature

            if armature.users == 0:
                bpy.data.armatures.remove(armature)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.armatures) > 0
