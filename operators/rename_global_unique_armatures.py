import bpy
from bpy.types import Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RenameUniqueArmatures(SushiBaseOperator):
    bl_idname = "sushi_cleanup.rename_unique_armatures"
    bl_label = "Rename All Unique Armatures"
    bl_description = "Renames armatures to their users' name if it only has one user"

    sk_tags = {"ALL", "ARMATURE", "UNIQUE", "RENAME"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            if obj.type != "ARMATURE":
                continue

            if obj.data.users == 1:
                obj.data.name = obj.name

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.armatures) > 0
