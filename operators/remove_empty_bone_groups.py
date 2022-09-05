from typing import Dict, Set

import bpy
from bpy.types import Context, Object

from .sushi_base_operator import SushiArmatureOperator, SushiBaseOperator


class SUSHI_CLEANUP_RemoveEmptyBoneGroupsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_bone_groups_all"
    bl_label = "Remove All Empty Bone Groups"
    bl_description = "Removes bone groups with no vertices for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "BONE_GROUP", "EMPTY", "ARMATURE", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            if obj.type == "ARMATURE":
                _remove_empty_bone_groups(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveEmptyBoneGroupsSelected(SushiArmatureOperator):
    bl_idname = "sushi_cleanup.remove_empty_bone_groups_selected"
    bl_label = "Remove Empty Bone Groups"
    bl_description = "Removes bone groups with no vertices for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "BONE_GROUP", "EMPTY", "ARMATURE", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_armature(context)
        if err:
            return err

        _remove_empty_bone_groups(bpy.context.active_object)

        return {"FINISHED"}


def _remove_empty_bone_groups(armobj: Object) -> None:
    print(f"[{armobj.name}] Removing empty bone groups (Start)")

    bone_groups_with_bones: Dict[str, None] = {}

    for pose_bone in armobj.pose.bones:
        if not pose_bone.bone_group:
            continue

        bone_groups_with_bones[pose_bone.bone_group.name] = None

    bone_groups_to_remove = []

    for bone_group in armobj.pose.bone_groups:
        if bone_group.name not in bone_groups_with_bones:
            bone_groups_to_remove.append(bone_group)

    for bone_group in bone_groups_to_remove:
        armobj.pose.bone_groups.remove(bone_group)

    print(f"[{armobj.name}] Removing empty bone groups (Finished)")
