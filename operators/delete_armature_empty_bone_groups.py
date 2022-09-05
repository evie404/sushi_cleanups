from typing import Dict

import bpy
from bpy.types import Object

from .sushi_base_operator import SushiAllArmatureOperator, SushiArmatureOperator


class SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll(SushiAllArmatureOperator):
    bl_idname = "sushi_cleanup.delete_empty_bone_groups_all"
    bl_label = "Delete All Empty Bone Groups"
    bl_description = "Deletes bone groups with no vertices for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "BONE_GROUP", "EMPTY", "ARMATURE", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_empty_bone_groups(obj)


class SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected(SushiArmatureOperator):
    bl_idname = "sushi_cleanup.delete_empty_bone_groups_selected"
    bl_label = "Delete Empty Bone Groups"
    bl_description = "Deletes bone groups with no vertices for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "BONE_GROUP", "EMPTY", "ARMATURE", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_empty_bone_groups(obj)


def _delete_empty_bone_groups(armobj: Object) -> None:
    print(f"[{armobj.name}] Removing empty bone groups (Start)")

    bone_groups_with_bones: Dict[str, None] = {}

    for pose_bone in armobj.pose.bones:
        if not pose_bone.bone_group:
            continue

        bone_groups_with_bones[pose_bone.bone_group.name] = None

    bone_groups_to_delete = []

    for bone_group in armobj.pose.bone_groups:
        if bone_group.name not in bone_groups_with_bones:
            bone_groups_to_delete.append(bone_group)

    for bone_group in bone_groups_to_delete:
        armobj.pose.bone_groups.remove(bone_group)

    print(f"[{armobj.name}] Removing empty bone groups (Finished)")
