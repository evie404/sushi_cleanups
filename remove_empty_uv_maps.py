from typing import List, Set

import bpy
from bpy.types import Context, MeshUVLoop, MeshUVLoopLayer, Object


class SUSHI_CLEANUP_RemoveEmptyUVMaps(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_empty_uv_maps"
    bl_label = "Remove Empty UV Maps"
    bl_description = "Removes UV maps with only default coordinates."
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

                zero_one_uv_only = True

                for loop in uv_layer.data:
                    loop: MeshUVLoop

                    if not zero_one_uv_only:
                        continue

                    if (loop.uv[0] == 0.0 or loop.uv[0] == 1.0) and (
                        loop.uv[1] == 0.0 or loop.uv[1] == 1.0
                    ):
                        continue

                    zero_one_uv_only = False

                if zero_one_uv_only:
                    uv_layers_to_remove.append(uv_layer)

            for uv_layer in uv_layers_to_remove:
                if uv_layer.name not in obj.data.uv_layers:
                    continue

                print(f"{obj.name}: removing UV map `{uv_layer.name}`")
                obj.data.uv_layers.remove(uv_layer)

        return {"FINISHED"}
