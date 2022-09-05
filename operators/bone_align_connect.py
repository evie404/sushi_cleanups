from typing import List, Set

import bpy
from bpy.types import EditBone, Object

from .sushi_base_operator import SushiBonesOperator


class SUSHI_CLEANUP_BoneAlignConnectParentsHead(SushiBonesOperator):
    bl_idname = "sushi_cleanup.bone_align_connect_parent_head"
    bl_label = "Connect to Parents' Tail"
    bl_description = (
        "Set selected bones to be connected to their parents aligned to their head"
    )

    sk_tags = {"BONE", "ARMATURE"}

    def sk_bones_exec(self, _o: Object, _p: EditBone, selected: List[EditBone]) -> None:
        root_bones: List[EditBone] = []
        selected_set: Set[EditBone] = set(selected)

        for bone in selected:
            if is_root(bone, selected):
                root_bones.append(bone)

        for bone in root_bones:
            _align_connect_to_parents_head_from_root(bone, selected_set)


def is_root(bone: EditBone, selected: Set[EditBone]) -> bool:
    if not bone.parent:
        return True

    return bone.parent not in selected


def _is_leaf(bone: EditBone, selected: Set[EditBone]) -> bool:
    if not bone.children or len(bone.children) == 0:
        return True

    for child in bone.children:
        if child in selected:
            return False

    return True


# does not work
def _align_connect_to_parents_head_from_root(
    root: EditBone, selected: Set[EditBone]
) -> None:
    for child in root.children:
        if child not in selected:
            continue

        _align_connect_to_parents_head_from_root(child, selected)

        if child.use_connect:
            continue

        child.tail = child.head
        child.head = root.head
        child.use_connect = True


def _align_connect_to_parents_head_from_leaf(
    leaf: EditBone, selected: Set[EditBone]
) -> None:
    if leaf.parent not in selected:
        return

    leaf.tail = leaf.head
    leaf.head = leaf.parent.head

    _align_connect_to_parents_head_from_leaf(leaf.parent, selected)
