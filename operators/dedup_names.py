from typing import Dict

import bpy
from bpy.types import ID, Context

from .sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DedupNames(SushiBaseOperator):
    bl_idname = "sushi_cleanup.dedup_names"
    bl_label = "Dedup All Names"
    bl_description = "\n".join(
        [
            "Renames all objects/data blocks if they are the only instance of the same name.",
            "Currently works for armature, camera, collection, curve, light, material, mesh, object, particle, and text data",
        ]
    )
    sk_tags = {"ALL", "RENAME"}

    # TODO: debug
    def execute(self, context: Context):
        dedup_names(bpy.data.armatures)
        dedup_names(bpy.data.cameras)
        dedup_names(bpy.data.collections)
        dedup_names(bpy.data.curves)
        dedup_names(bpy.data.lights)
        dedup_names(bpy.data.materials)
        dedup_names(bpy.data.meshes)
        dedup_names(bpy.data.objects)
        dedup_names(bpy.data.particles)
        dedup_names(bpy.data.texts)

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


def dedup_names(collection: Dict[str, ID]) -> None:
    for instance in collection:
        instance: ID

        orig_name = original_name_of(instance.name)
        if orig_name == instance.name:
            continue

        if orig_name not in collection:
            instance.name = orig_name
