from typing import Set

import bpy
from bpy.types import Context, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_unused_material_slots_all"
    bl_label = "Delete All Unused Material Slots"
    bl_description = "Deletes material slots with no vertices for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "MESH", "MATERIAL_SLOT" "UNUSED", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            _delete_unused_material_slots(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_material_slots_selected"
    bl_label = "Delete Unused Material Slots"
    bl_description = "Deletes material slots with no vertices for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "MESH", "MATERIAL_SLOT" "UNUSED", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        _delete_unused_material_slots(bpy.context.active_object)

        return {"FINISHED"}


def _delete_unused_material_slots(obj: Object) -> None:
    if not obj.material_slots:
        return

    previously_hidden = False

    if obj.hide_viewport:
        obj.hide_viewport = False
        previously_hidden = True

    bpy.ops.object.material_slot_delete_unused({"object": obj})

    if previously_hidden:
        obj.hide_viewport = True

    # context = bpy.context
    # scene = context.scene

    # bpy.ops.object.material_slot_delete_unused(
    #     {"object": scene.objects[0], "selected_objects": scene.objects}
    # )
