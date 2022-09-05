from typing import Dict

import bpy
from bpy.types import Context, Operator

from .operations import OPERATIONS_ALL, OPERATIONS_SELECTED


class SUSHI_CLEANUP_PT_Selected(bpy.types.Panel):
    bl_category = "Sushi Cleanups"
    bl_label = "Cleanups (Selected Object)"
    bl_idname = "SUSHI_CLEANUP_PT_Selected"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        ob = bpy.context.active_object
        if not ob:
            return

        col = self.layout.column()

        op_map: Dict[str, Operator] = {}

        for op in OPERATIONS_SELECTED:
            op_map[op.bl_idname] = op

        for op_name in sorted(op_map.keys()):
            col.operator(op_name)


class SUSHI_CLEANUP_PT_All(bpy.types.Panel):
    bl_category = "Sushi Cleanups"
    bl_label = "Cleanups (All Objects)"
    bl_idname = "SUSHI_CLEANUP_PT_All"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        op_map: Dict[str, Operator] = {}

        for op in OPERATIONS_ALL:
            op_map[op.bl_idname] = op

        for op_name in sorted(op_map.keys()):
            col.operator(op_name)


UI_CLASSES = [SUSHI_CLEANUP_PT_All, SUSHI_CLEANUP_PT_Selected]
