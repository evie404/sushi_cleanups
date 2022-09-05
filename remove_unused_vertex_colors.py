from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object


class SUSHI_CLEANUP_RemoveUnusedVertexColors(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_vertex_colors"
    bl_label = "Remove Unused Color Maps"
    bl_description = "Removes color maps with only default colors."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            if len(obj.data.vertex_colors) < 2:
                continue

            vertex_colors_to_remove: List[MeshLoopColorLayer] = []

            for vertex_color in obj.data.vertex_colors:
                vertex_color: MeshLoopColor

                if vertex_color.active:
                    continue

                vertex_colors_to_remove.append(vertex_color)

            for vertex_color in vertex_colors_to_remove:
                if vertex_color.name not in obj.data.vertex_colors:
                    continue

                print(f"{obj.name}: removing unused color map `{vertex_color.name}`")
                obj.data.vertex_colors.remove(vertex_color)

        return {"FINISHED"}
