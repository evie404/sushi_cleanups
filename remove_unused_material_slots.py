from typing import Set

import bpy
from bpy.types import Context, Object


class SUSHI_CLEANUP_RemoveUnusedMaterialSlots(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_material_slots"
    bl_label = "Remove Unused Material Slots"
    bl_description = "Removes material slots with no vertices."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if not obj.material_slots:
                continue

            print(obj.name)
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

        return {"FINISHED"}
