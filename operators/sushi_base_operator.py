from typing import Optional, Set

import bpy
from bpy.types import Context


class SushiBaseOperator(bpy.types.Operator):
    sk_tags: Set[str]

    @classmethod
    def icon(cls) -> str:
        if "DELETE" in cls.sk_tags:
            return "TRASH"

        if "RENAME" in cls.sk_tags:
            return "GREASEPENCIL"

        if "SORT" in cls.sk_tags:
            return "SORTSIZE"

        return "NONE"


class SushiMeshOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "MESH"


class SushiArmatureOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "ARMATURE"
