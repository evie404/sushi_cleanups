import bpy
from bpy.types import Context, Object
from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_HideAllEmpties(SushiBaseOperator):
    bl_idname = "sushi_cleanup.hide_all_empties"
    bl_label = "Hide All Empties"
    bl_description = "Hides all empties"

    sk_tags = {"ALL", "EMPTY", "UNIQUE", "HIDE", "DATA"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "EMPTY":
                continue

            obj.hide_set(True)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.objects) > 0


class SUSHI_CLEANUP_HideAllEmptiesExceptActive(SushiBaseOperator):
    bl_idname = "sushi_cleanup.hide_all_empties_except_active"
    bl_label = "Hide All non-Active Empties"
    bl_description = "Hides all empties except the active empty"

    sk_tags = {"ALL", "EMPTY", "UNIQUE", "HIDE", "DATA"}

    # TODO: debug
    def execute(self, context: Context):
        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "EMPTY":
                continue

            if obj == bpy.context.active_object:
                continue

            obj.hide_set(True)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.objects) > 0 and bpy.context.active_object.type == "EMPTY"
