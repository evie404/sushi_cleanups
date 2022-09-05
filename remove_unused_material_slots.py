from typing import Set

import bpy
from bpy.types import Context, Object

from sushi_cleanups.base_operation import SushiBaseOperation


class SUSHI_CLEANUP_RemoveUnusedMaterialSlotsAll(SushiBaseOperation):
    bl_idname = "sushi_cleanup.remove_unused_material_slots_all"
    bl_label = "Remove Unused Material Slots"
    bl_description = "Removes material slots with no vertices"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            _remove_unused_material_slots(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveUnusedMaterialSlotsSelected(SushiBaseOperation):
    bl_idname = "sushi_cleanup.remove_unused_material_slots_selected"
    bl_label = "Remove Unused Material Slots"
    bl_description = "Removes material slots with no vertices"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_mesh(context)
        if err:
            return err

        _remove_unused_material_slots(bpy.context.active_object)

        return {"FINISHED"}


def _remove_unused_material_slots(obj: Object) -> None:
    if not obj.material_slots:
        return

    previously_hidden = False

    if obj.hide_viewport:
        obj.hide_viewport = False
        previously_hidden = True

    bpy.ops.object.material_slot_remove_unused({"object": obj})

    if previously_hidden:
        obj.hide_viewport = True

    # context = bpy.context
    # scene = context.scene

    # bpy.ops.object.material_slot_remove_unused(
    #     {"object": scene.objects[0], "selected_objects": scene.objects}
    # )
