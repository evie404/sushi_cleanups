from typing import Callable, Optional, Set

import bpy
from bpy.types import Context, Object


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


class SushiAllOperator(SushiBaseOperator):
    sk_obj_type: str
    sk_obj_exec: Callable[[Object], None]

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type == self.sk_obj_type:
                self.sk_obj_exec(obj)

        return {"FINISHED"}


class SushiAllMeshOperator(SushiAllOperator):
    sk_obj_type = "MESH"


class SushiMeshOperator(SushiBaseOperator):
    def execute(self, context: Context) -> Set[str]:
        self.sk_obj_exec(context.active_object)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "MESH"


class SushiArmatureOperator(SushiBaseOperator):
    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == "ARMATURE"
