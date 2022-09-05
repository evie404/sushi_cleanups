from typing import Dict, List

import bpy
from bpy.types import EditBone, Object

from .sushi_base_operator import SushiBonesOperator


class SUSHI_CLEANUP_BonePrintList(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bones_print_list"
    bl_label = "Print Bones as List"
    bl_description = "Print currently selected bones to console as a list"

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(self, _o: Object, _p: EditBone, selected: List[EditBone]) -> None:
        bone_names: List[str] = []

        for bone in selected:
            bone_names.append(bone.name)

        print(f"{bone_names}")


class SUSHI_CLEANUP_BonePrintDict(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bones_print_dict"
    bl_label = "Print Bones as Dict"
    bl_description = "Print currently selected bones to console as a map"

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(self, _o: Object, _p: EditBone, selected: List[EditBone]) -> None:
        selected_bones: Dict[str, str] = {}

        for bone in selected:
            selected_bones[bone.name] = ""

        print(f"{selected_bones}")
