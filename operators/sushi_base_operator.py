from typing import Set

import bpy
from bpy.types import Context


class SushiBaseOperator(bpy.types.Operator):
    sk_tags: Set[str]


class SushiMeshOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "MESH"


class SushiArmatureOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "ARMATURE"
