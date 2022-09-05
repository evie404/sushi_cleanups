from typing import List, Set

import bpy
from bpy.types import Context, MeshUVLoopLayer, Object

from .sushi_base_operator import SushiBaseOperator, SushiMeshOperator


class SUSHI_CLEANUP_RemoveUnusedUVMapsAll(SushiBaseOperator):
    bl_idname = "sushi_cleanup.remove_unused_uv_maps_all"
    bl_label = "Remove All Unused UV Maps"
    bl_description = "Removes unused UV maps for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "MESH", "UNUSED", "UV_MAP", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        for obj in bpy.data.objects:
            if obj.type == "MESH":
                _remove_unused_uv_maps(obj)

        return {"FINISHED"}


class SUSHI_CLEANUP_RemoveUnusedUVMapsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.remove_unused_uv_maps_selected"
    bl_label = "Remove Unused UV Maps"
    bl_description = "Removes unused UV maps for the selected object"
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "MESH", "UNUSED", "UV_MAP", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        _remove_unused_uv_maps(bpy.context.active_object)

        return {"FINISHED"}


def _remove_unused_uv_maps(obj: Object) -> None:
    if len(obj.data.uv_layers) < 2:
        return

    uv_layers_to_remove: List[MeshUVLoopLayer] = []

    for uv_layer in obj.data.uv_layers:
        uv_layer: MeshUVLoopLayer

        if uv_layer.active:
            continue

        uv_layers_to_remove.append(uv_layer)

    for uv_layer in uv_layers_to_remove:
        if uv_layer.name not in obj.data.uv_layers:
            continue

        print(f"[{obj.name}] Removing unused UV map `{uv_layer.name}`")
        obj.data.uv_layers.remove(uv_layer)
