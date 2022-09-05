from typing import Dict

import bpy
from bpy.types import Context, Operator

from sushi_cleanups.operations import OPERATIONS


class SUSHI_CLEANUP_PT_UI(bpy.types.Panel):
    bl_category = "Sushi Cleanups"
    bl_label = "Cleanups"
    bl_idname = "SUSHI_CLEANUP_PT_UI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        op_map: Dict[str, Operator] = {}

        for op in OPERATIONS:
            op_map[op.bl_idname] = op

        for op_name in sorted(op_map.keys()):
            col.operator(op_name)
