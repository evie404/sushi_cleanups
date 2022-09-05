from typing import Dict, Set

import bpy
from bpy.types import Context

from .operators.groups import (
    DELETE_ALL,
    DELETE_SELECTED,
    DELETE_SIMILAR,
    RENAME_ALL_DATA,
    RENAME_SELECTED,
    SORT_ALL,
    SORT_SELECTED,
)
from .operators.sushi_base_operator import SushiBaseOperator


class SushiBasePanel(bpy.types.Panel):
    sk_operators: Set[SushiBaseOperator]

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        op_map: Dict[str, SushiBaseOperator] = {}

        for op in self.sk_operators:
            op_map[op.bl_idname] = op

        for bl_idname in sorted(op_map.keys()):
            op = op_map[bl_idname]
            label = (
                op.bl_label.replace("Delete All ", "")
                .replace("Rename All", "")
                .replace("Sort All", "")
                .replace("Delete ", "")
                .replace("Rename", "")
                .replace("Sort", "")
            )

            col.operator(op.bl_idname, text=label, icon=op.icon())

    @classmethod
    def poll(cls, context: Context) -> bool:
        return len(cls.sk_operators) > 0


class SUSHI_CLEANUP_PT_Delete_Similar(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Delete Similar to Active Object"
    bl_idname = "SUSHI_CLEANUP_PT_Delete_Similar"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = DELETE_SIMILAR


class SUSHI_CLEANUP_PT_Delete_Selected(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Delete from Active Object"
    bl_idname = "SUSHI_CLEANUP_PT_Delete_Selected"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = DELETE_SELECTED


class SUSHI_CLEANUP_PT_Delete_All(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Delete from All Objects"
    bl_idname = "SUSHI_CLEANUP_PT_Delete_All"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = DELETE_ALL


class SUSHI_CLEANUP_PT_Rename_Selected(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Rename Active Object"
    bl_idname = "SUSHI_CLEANUP_PT_Rename_Selected"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = RENAME_SELECTED


class SUSHI_CLEANUP_PT_Rename_All_Data(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Rename All Data Blocks"
    bl_idname = "SUSHI_CLEANUP_PT_Rename_All_Data"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = RENAME_ALL_DATA


class SUSHI_CLEANUP_PT_Sort_Selected(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Sort in Active Object"
    bl_idname = "SUSHI_CLEANUP_PT_Sort_Selected"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = SORT_SELECTED


class SUSHI_CLEANUP_PT_Sort_All(SushiBasePanel):
    bl_category = "Sushi Cleanups"
    bl_label = "Sort in All Objects"
    bl_idname = "SUSHI_CLEANUP_PT_Sort_All"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    sk_operators = SORT_ALL


UI_CLASSES = [
    SUSHI_CLEANUP_PT_Delete_All,
    SUSHI_CLEANUP_PT_Delete_Selected,
    SUSHI_CLEANUP_PT_Delete_Similar,
    SUSHI_CLEANUP_PT_Rename_All_Data,
    SUSHI_CLEANUP_PT_Rename_Selected,
    SUSHI_CLEANUP_PT_Sort_All,
    SUSHI_CLEANUP_PT_Sort_Selected,
]
