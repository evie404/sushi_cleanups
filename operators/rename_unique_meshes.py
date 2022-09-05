import bpy
from bpy.types import Context, Mesh, Object


class SUSHI_CLEANUP_RenameUniqueMeshes(bpy.types.Operator):
    bl_idname = "sushi_cleanup.rename_unique_meshes"
    bl_label = "Rename All Single-User Meshes"
    bl_description = "Renames meshes data to use their object name"
    bl_options = {"UNDO"}

    def execute(self, context: Context):
        mesh_objs = [obj for obj in bpy.data.objects if obj.type == "MESH"]

        for obj in mesh_objs:
            obj: Object
            mesh: Mesh = obj.data

            if mesh.users == 1:
                mesh.name = obj.name

        return {"FINISHED"}
