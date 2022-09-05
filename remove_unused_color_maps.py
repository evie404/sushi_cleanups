from typing import List, Set

import bpy
from bpy.types import Context, MeshLoopColor, MeshLoopColorLayer, Object


class SUSHI_CLEANUP_RemoveUnusedColorMaps(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_color_maps"
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

            color_maps_to_remove: List[MeshLoopColorLayer] = []

            for color_map in obj.data.vertex_colors:
                color_map: MeshLoopColor

                if color_map.active:
                    continue

                color_maps_to_remove.append(color_map)

            for color_map in color_maps_to_remove:
                if color_map.name not in obj.data.vertex_colors:
                    continue

                print(f"{obj.name}: removing unused color map `{color_map.name}`")
                obj.data.vertex_colors.remove(color_map)

        return {"FINISHED"}
