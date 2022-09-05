from typing import List

import bpy
from bpy.types import EditBone, Object

from .sushi_base_operator import SushiBonesOperator


class SUSHI_CLEANUP_BoneParentToActive(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bone_parent_to_active"
    bl_label = "Parent to Active"
    bl_description = "Set selected bones' parents' as the active bone"

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(
        self, _: Object, parent: EditBone, selected: List[EditBone]
    ) -> None:
        _set_active_as_parent(parent, selected)


def _set_active_as_parent(parent: EditBone, selected: List[EditBone]) -> None:
    for bone in selected:
        if bone.name == parent.name:
            continue

        bone.parent = parent
