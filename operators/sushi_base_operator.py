from typing import Optional, Set

import bpy
from bpy.types import Context


class SushiBaseOperator(bpy.types.Operator):
    sk_tags: Set[str]

    @classmethod
    def icon(cls) -> Optional[str]:
        if "REMOVE" in cls.sk_tags:
            return "TRASH"

        if "RENAME" in cls.sk_tags:
            return "GREASEPENCIL"

        return None


class SushiMeshOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "MESH"


class SushiArmatureOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "ARMATURE"
