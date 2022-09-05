from typing import Dict

import bpy
from bpy.types import Context

from .operations import OPERATIONS_ALL, OPERATIONS_SELECTED
from .operators.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_PT_Selected(bpy.types.Panel):
    bl_category = "Sushi Cleanups"
    bl_label = "Delete from Active Object"
    bl_idname = "SUSHI_CLEANUP_PT_Selected"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        op_map: Dict[str, SushiBaseOperator] = {}

        for op in OPERATIONS_SELECTED:
            op_map[op.bl_idname] = op

        for op_name in sorted(op_map.keys()):
            col.operator(op_name, icon=op_map[op_name].icon())

    # @classmethod
    # def poll(cls, context):
    #     return context.object and context.object.type in {"MESH", "ARMATURE"}


class SUSHI_CLEANUP_PT_All(bpy.types.Panel):
    bl_category = "Sushi Cleanups"
    bl_label = "Delete from All Objects"
    bl_idname = "SUSHI_CLEANUP_PT_All"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        op_map: Dict[str, SushiBaseOperator] = {}

        for op in OPERATIONS_ALL:
            op_map[op.bl_idname] = op

        for op_name in sorted(op_map.keys()):
            col.operator(op_name, icon=op_map[op_name].icon())


UI_CLASSES = [SUSHI_CLEANUP_PT_All, SUSHI_CLEANUP_PT_Selected]
