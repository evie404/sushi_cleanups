from typing import Set

import bpy
from bpy.types import Context, Mesh


class SUSHI_CLEANUP_RemoveUnusedMeshes(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_unused_meshes"
    bl_label = "Remove All Unused Meshes"
    bl_description = "Removes meshes with no users"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        for mesh in bpy.data.meshes:
            mesh: Mesh

            if mesh.users == 0:
                bpy.data.meshes.remove(mesh)

        return {"FINISHED"}
