from typing import List, Set

import bpy
from bpy.types import Context, MeshUVLoopLayer, Object


class SUSHI_CLEANUP_RemoveUnusedUVMaps(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_uv_maps"
    bl_label = "Remove Unused UV Maps"
    bl_description = "Removes unused UV maps."
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type != "MESH":
                continue

            if len(obj.data.uv_layers) < 2:
                continue

            uv_layers_to_remove: List[MeshUVLoopLayer] = []

            for uv_layer in obj.data.uv_layers:
                uv_layer: MeshUVLoopLayer

                if uv_layer.active:
                    continue

                uv_layers_to_remove.append(uv_layer)

            for uv_layer in uv_layers_to_remove:
                if uv_layer.name not in obj.data.uv_layers:
                    continue

                print(f"{obj.name}: removing unused UV map `{uv_layer.name}`")
                obj.data.uv_layers.remove(uv_layer)

        return {"FINISHED"}
