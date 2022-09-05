import bpy
from bpy.types import Context, Object
from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_HideAllArmatures(SushiBaseOperator):
    bl_idname = "sushi_cleanup.hide_all_armatures"
    bl_label = "Hide All Armatures"
    bl_description = "Hides all armatures"

    sk_tags = {"ALL", "ARMATURE", "UNIQUE", "HIDE", "DATA"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "ARMATURE":
                continue

            obj.hide_set(True)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.armatures) > 0


class SUSHI_CLEANUP_HideAllArmaturesExceptActive(SushiBaseOperator):
    bl_idname = "sushi_cleanup.hide_all_armatures_except_active"
    bl_label = "Hide All non-Active Armatures"
    bl_description = "Hides all armatures except the active armature"

    sk_tags = {"ALL", "ARMATURE", "UNIQUE", "HIDE", "DATA"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "ARMATURE":
                continue

            if obj == bpy.context.active_object:
                continue

            obj.hide_set(True)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return (
            len(bpy.data.armatures) > 0 and bpy.context.active_object.type == "ARMATURE"
        )
