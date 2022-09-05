import bpy
from bpy.types import Context


class SUSHI_CLEANUP_RenameArmatures(bpy.types.Operator):
    bl_idname = "sushi_cleanup.rename_armatures"
    bl_label = "Rename Armatures"
    bl_description = "Renames armatures data to use their object name"
    bl_options = {"UNDO"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            if obj.type != "ARMATURE":
                continue

            if not obj.data.name.startswith("Armature"):
                continue

            obj.data.name = obj.name

        return {"FINISHED"}
