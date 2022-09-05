import bpy
from bpy.types import Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RenameUniqueArmatures(SushiBaseOperator):
    bl_idname = "sushi_cleanup.rename_unique_armatures"
    bl_label = "Rename All Single-User Armatures"
    bl_description = "Renames armatures data to use their object name"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "ARMATURE", "UNIQUE", "RENAME"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            if obj.type != "ARMATURE":
                continue

            if obj.data.users == 1:
                obj.data.name = obj.name

        return {"FINISHED"}
