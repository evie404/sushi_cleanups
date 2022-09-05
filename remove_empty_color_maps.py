from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object


class SUSHI_CLEANUP_RemoveEmptyColorMaps(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_empty_color_maps"
    bl_label = "Remove Empty Color Maps"
    bl_description = "Removes color maps with only default colors."
    bl_options = {"UNDO"}

    # TODO: debug
    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            color_maps_to_remove: List[MeshLoopColorLayer] = []

            for color_map in obj.data.vertex_colors:
                color_map: MeshLoopColorLayer

                zero_color_only = True

                for loop in color_map.data:
                    loop: MeshLoopColor

                    if not zero_color_only:
                        continue

                    if list(loop.color) == [0.0, 0.0, 0.0, 1.0]:
                        continue

                    zero_color_only = False

                if zero_color_only:
                    color_maps_to_remove.append(color_map)

            for color_map in color_maps_to_remove:
                if color_map.name not in obj.data.vertex_colors:
                    continue

                print(f"{obj.name}: removing color map `{color_map.name}`")
                obj.data.vertex_colors.remove(color_map)

        return {"FINISHED"}
