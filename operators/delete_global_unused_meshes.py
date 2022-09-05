from typing import Set

import bpy
from bpy.types import Context, Mesh

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DeleteUnusedMeshes(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_unused_meshes"
    bl_label = "Delete All Unused Meshes"
    bl_description = "Deletes meshes with no users"

    sk_tags = {"ALL", "MESH", "UNUSED", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        for mesh in bpy.data.meshes:
            mesh: Mesh

            if mesh.users == 0:
                bpy.data.meshes.remove(mesh)

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.meshes) > 0
