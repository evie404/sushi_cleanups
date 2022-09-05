from typing import List

import bpy
from bpy.types import MeshUVLoopLayer, Object

from .sushi_base_operator import SushiAllMeshOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteUnusedUVMapsAll(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_uv_maps_all"
    bl_label = "Delete All Unused UV Maps"
    bl_description = "Deletes unused UV maps for all objects"

    sk_tags = {"ALL", "MESH", "UNUSED", "UV_MAP", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_uv_maps(obj)


class SUSHI_CLEANUP_DeleteUnusedUVMapsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_unused_uv_maps_selected"
    bl_label = "Delete Unused UV Maps"
    bl_description = "Deletes unused UV maps for the selected object"

    sk_tags = {"SELECTED", "MESH", "UNUSED", "UV_MAP", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_unused_uv_maps(obj)


def _delete_unused_uv_maps(obj: Object) -> None:
    if len(obj.data.uv_layers) < 2:
        return

    uv_layers_to_delete: List[MeshUVLoopLayer] = []

    for uv_layer in obj.data.uv_layers:
        uv_layer: MeshUVLoopLayer

        if uv_layer.active:
            continue

        uv_layers_to_delete.append(uv_layer)

    for uv_layer in uv_layers_to_delete:
        if uv_layer.name not in obj.data.uv_layers:
            continue

        print(f"[{obj.name}] Removing unused UV map `{uv_layer.name}`")
        obj.data.uv_layers.remove(uv_layer)
