from typing import List, Set

import bpy
from bpy.types import Context, MeshUVLoop, MeshUVLoopLayer, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_RemoveEmptyUVMapsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_empty_uv_maps_all"
    bl_label = "Remove All Empty UV Maps"
    bl_description = "Removes UV maps with only default coordinates for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "UV_MAP", "EMPTY", "MESH", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object
            if obj.type == "MESH":
                _remove_empty_uv_maps(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveEmptyUVMapsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.remove_empty_uv_maps_selected"
    bl_label = "Remove Empty UV Maps"
    bl_description = (
        "Removes UV maps with only default coordinates for the selected object"
    )
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "UV_MAP", "EMPTY", "MESH", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        _remove_empty_uv_maps(bpy.context.active_object)

        return {"FINISHED"}


def _remove_empty_uv_maps(obj: Object) -> None:
    if len(obj.data.uv_layers) < 2:
        return

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

        print(f"[{obj.name}] Removing UV map `{uv_layer.name}`")
        obj.data.uv_layers.remove(uv_layer)
