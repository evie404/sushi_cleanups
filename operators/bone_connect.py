from typing import List

import bpy
from bpy.types import EditBone, Object

from sushi_cleanups.operators.sushi_base_operator import SushiBonesOperator


class SUSHI_CLEANUP_BoneSetConnected(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bone_set_connected"
    bl_label = "Set Connected"
    bl_description = "Set selected bones to be connected to their parents"

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(self, _o: Object, _p: EditBone, selected: List[EditBone]) -> None:
        _set_connected(selected, True)


class SUSHI_CLEANUP_BoneUnsetConnected(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bone_unset_connected"
    bl_label = "Unet Connected"
    bl_description = "Unset selected bones to be connected to their parents"

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(self, _o: Object, _p: EditBone, selected: List[EditBone]) -> None:
        _set_connected(selected, False)


def _set_connected(selected: List[EditBone], connected: bool) -> None:
    for bone in selected:
        bone.use_connect = connected
