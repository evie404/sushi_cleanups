import bpy
from bpy.types import Context, Mesh, Object

from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_RenameUniqueMeshes(SushiBaseOperator):
    bl_idname = "sushi_cleanup.rename_unique_meshes"
    bl_label = "Rename All Unique Meshes"
    bl_description = "Renames meshes to their users' name if it only has one user"

    sk_tags = {"ALL", "MESH", "UNIQUE", "RENAME", "DATA"}

    def execute(self, context: Context):
        mesh_objs = [obj for obj in bpy.data.objects if obj.type == "MESH"]

        for obj in mesh_objs:
            obj: Object
            mesh: Mesh = obj.data

            if mesh.users == 1:
                mesh.name = obj.name

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.meshes) > 0
