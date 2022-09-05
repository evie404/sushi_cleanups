from typing import Optional, Set

import bpy
from bpy.types import Context


class SushiBaseOperation(bpy.types.Operator):
    def check_for_armature(self, context: Context) -> Optional[Set[str]]:
        if not bpy.context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select an armature object.")
            return {"CANCELLED"}

        obj = bpy.context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        return None

    def check_for_mesh(self, context: Context) -> Optional[Set[str]]:
        if not bpy.context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a mesh object.")
            return {"CANCELLED"}

        obj = bpy.context.active_object

        if not (obj and obj.type == "MESH"):
            self.report({"ERROR_INVALID_CONTEXT"}, "Selected object is not a mesh.")

            return {"CANCELLED"}

        return None
