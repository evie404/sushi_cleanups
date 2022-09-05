from typing import Callable, Set

import bpy
from bpy.types import Context, Object


class SushiBaseOperator(bpy.types.Operator):
    bl_options = {"UNDO"}

    sk_tags: Set[str]

    @classmethod
    def icon(cls) -> str:
        if "DELETE" in cls.sk_tags:
            return "TRASH"

        if "RENAME" in cls.sk_tags:
            return "GREASEPENCIL"

        if "SORT" in cls.sk_tags:
            return "SORTSIZE"

        if "COPY" in cls.sk_tags:
            return "DUPLICATE"

        return "NONE"


class SushiFromToOperator(SushiBaseOperator):
    sk_obj_type: str
    sk_from_to_exec: Callable[[Object, Object], None]

    def execute(self, context: Context) -> Set[str]:
        for obj in context.selected_objects:
            if obj == context.active_object:
                continue

            self.sk_from_to_exec(context.active_object, obj)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return context.active_object and len(context.selected_objects) > 1


class SushiAllOperator(SushiBaseOperator):
    sk_obj_type: str
    sk_obj_exec: Callable[[Object], None]

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type == self.sk_obj_type:
                self.sk_obj_exec(obj)

        return {"FINISHED"}


class SushiSelectedOperator(SushiBaseOperator):
    sk_obj_type: str
    sk_obj_exec: Callable[[Object], None]

    def execute(self, context: Context) -> Set[str]:
        self.sk_obj_exec(context.active_object)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return context.active_object and context.active_object.type == cls.sk_obj_type


class SushiAllMeshOperator(SushiAllOperator):
    sk_obj_type = "MESH"

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.meshes) > 0


class SushiMeshOperator(SushiSelectedOperator):
    sk_obj_type = "MESH"


class SushiAllArmatureOperator(SushiAllOperator):
    sk_obj_type = "ARMATURE"

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.armatures) > 0


class SushiArmatureOperator(SushiSelectedOperator):
    sk_obj_type = "ARMATURE"
