from typing import List, Set

import bpy
from bpy.types import Context, MeshUVLoop, MeshUVLoopLayer, Object

from .sushi_base_operator import SushiAllMeshOperator, SushiMeshOperator


class SUSHI_CLEANUP_DeleteEmptyUVMapsAll(SushiAllMeshOperator):
    bl_idname = "sushi_cleanup.delete_empty_uv_maps_all"
    bl_label = "[Buggy] Delete All Empty UV Maps"
    bl_description = "Deletes UV maps with only default coordinates for all objects"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "UV_MAP", "EMPTY", "MESH", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_empty_uv_maps(obj)


class SUSHI_CLEANUP_DeleteEmptyUVMapsSelected(SushiMeshOperator):
    bl_idname = "sushi_cleanup.delete_empty_uv_maps_selected"
    bl_label = "[Buggy] Delete Empty UV Maps"
    bl_description = (
        "Deletes UV maps with only default coordinates for the selected object"
    )
    bl_options = {"UNDO"}

    sk_tags = {"SELECTED", "UV_MAP", "EMPTY", "MESH", "DELETE"}

    def sk_obj_exec(self, obj: Object) -> None:
        _delete_empty_uv_maps(obj)


def _delete_empty_uv_maps(obj: Object) -> None:
    if len(obj.data.uv_layers) < 2:
        return

    uv_layers_to_delete: List[MeshUVLoopLayer] = []

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
            uv_layers_to_delete.append(uv_layer)

    for uv_layer in uv_layers_to_delete:
        if uv_layer.name not in obj.data.uv_layers:
            continue

        print(f"[{obj.name}] Removing UV map `{uv_layer.name}`")
        obj.data.uv_layers.remove(uv_layer)
