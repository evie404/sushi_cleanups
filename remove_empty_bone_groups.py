from typing import Dict, Set

import bpy
from bpy.types import Context

from .base_operation import SushiBaseOperation


class SUSHI_CLEANUP_RemoveEmptyBoneGroups(SushiBaseOperation):
    bl_idname = "sushi_cleanup.remove_empty_bone_groups"
    bl_label = "Remove Empty Bone Groups"
    bl_description = "Removes bone groups with no vertices."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        err = self.check_for_armature(context)
        if err:
            return err

        armobj = bpy.context.active_object

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

        return {"FINISHED"}
