from typing import Set

import bpy
from bpy.types import Armature, Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RemoveUnusedArmatures(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_unused_armatures"
    bl_label = "Remove All Unused Armatures"
    bl_description = "Removes armatures with no users"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "ARMATURE", "UNUSED", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        for armature in bpy.data.armatures:
            armature: Armature

            if armature.users == 0:
                bpy.data.armatures.remove(armature)

        return {"FINISHED"}
