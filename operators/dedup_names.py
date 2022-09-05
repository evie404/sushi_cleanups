import bpy
from bpy.types import Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DedupNames(SushiBaseOperator):
    bl_idname = "sushi_cleanup.dedup_names"
    bl_label = "Dedup All Names"
    bl_description = "Renames all objects/data blocks if they are the only instance of the same name.\nCurrently works for objects, collections, mesh data, armature data, and material data"

    sk_tags = {"ALL", "RENAME"}

    # TODO: debug
    def execute(self, context: Context):
        dedup_object_names()
        dedup_collection_names()
        dedup_mesh_names()
        dedup_armature_names()
        dedup_material_names()

        return {"FINISHED"}


def is_duplicated_blender_name(name: str) -> bool:
    parts = name.split(".")

    if len(parts) < 2:
        return False

    if len(parts[-1]) != 3:
        return False

    return parts[-1].isnumeric()


def is_duplicated_daz_name(name: str) -> bool:
    if not name.endswith(")"):
        return False

    parts = name[:-1].split(" (")

    if len(parts) < 2:
        return False

    return parts[-1].isnumeric()


def is_duplicated_daz_mesh_name(name: str) -> bool:
    parts = name.split("-")

    if len(parts) < 2:
        return False

    return parts[-1].isnumeric()


def is_duplicated_name(name: str) -> bool:
    return is_duplicated_blender_name(name) or is_duplicated_daz_name(name)


def original_blender_name_of(name: str) -> str:
    if not is_duplicated_blender_name(name):
        return name

    parts = name.split(".")

    return ".".join(parts[:-1])


def original_daz_name_of(name: str) -> str:
    if not is_duplicated_daz_name(name):
        return name

    parts = name[:-1].split(" (")

    return " (".join(parts[:-1])


def original_daz_mesh_name_of(name: str) -> str:
    if not is_duplicated_daz_mesh_name(name):
        return name

    parts = name[:-1].split("-")

    return "-".join(parts[:-1]) + "-1"


def original_name_of(name: str) -> str:
    if is_duplicated_blender_name(name):
        return original_blender_name_of(name)

    if is_duplicated_daz_name(name):
        return original_daz_name_of(name)

    if is_duplicated_daz_mesh_name(name):
        return original_daz_mesh_name_of(name)

    return name


def dedup_object_names() -> None:
    for obj in bpy.data.objects:
        orig_name = original_name_of(obj.name)
        if orig_name == obj.name:
            continue

        if orig_name not in bpy.data.objects:
            obj.name = orig_name


def dedup_collection_names() -> None:
    for collection in bpy.data.collections:
        orig_name = original_name_of(collection.name)
        if orig_name == collection.name:
            continue

        if orig_name not in bpy.data.collections:
            collection.name = orig_name


def dedup_mesh_names() -> None:
    for mesh in bpy.data.meshes:
        orig_name = original_name_of(mesh.name)
        if orig_name == mesh.name:
            continue

        if orig_name not in bpy.data.meshes:
            mesh.name = orig_name


def dedup_armature_names() -> None:
    for armature in bpy.data.armatures:
        orig_name = original_name_of(armature.name)
        if orig_name == armature.name:
            continue

        if orig_name not in bpy.data.armatures:
            armature.name = orig_name


def dedup_material_names() -> None:
    for material in bpy.data.materials:
        orig_name = original_name_of(material.name)

        print(f"{material.name}: original name is `{orig_name}`")

        if orig_name == material.name:
            print(f"{material.name}: is original")
            continue

        if orig_name not in bpy.data.materials:
            print(
                f"{material.name}: original does not exist. renaming to `{orig_name}`"
            )
            material.name = orig_name
