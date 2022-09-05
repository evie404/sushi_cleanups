import bpy
from bpy.types import Object

from .sushi_base_operator import SushiAllMeshOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_material_slots_all"
    bl_label = "Delete All Unused Material Slots"
    bl_description = "Deletes material slots with no vertices for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "MESH", "MATERIAL_SLOT" "UNUSED", "DELETE"}

    # TODO: debug
    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_material_slots(obj)


class SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_material_slots_selected"
    bl_label = "Delete Unused Material Slots"
    bl_description = "Deletes material slots with no vertices for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "MESH", "MATERIAL_SLOT" "UNUSED", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_material_slots(obj)


def _delete_unused_material_slots(obj: Object) -> None:
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

    # bpy.ops.object.material_slot_delete_unused(
    #     {"object": scene.objects[0], "selected_objects": scene.objects}
    # )
