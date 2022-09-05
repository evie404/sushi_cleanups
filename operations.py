from typing import Set

from bpy.types import Operator

from sushi_cleanups.remove_empty_bone_groups import (
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsAll,
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsSelected,
)
from sushi_cleanups.remove_empty_collections import SUSHI_CLEANUP_RemoveEmptyCollections
from sushi_cleanups.remove_empty_color_maps import (
    SUSHI_CLEANUP_RemoveEmptyColorMapsAll,
    SUSHI_CLEANUP_RemoveEmptyColorMapsSelected,
)
from sushi_cleanups.remove_empty_uv_maps import SUSHI_CLEANUP_RemoveEmptyUVMaps
from sushi_cleanups.remove_empty_vertex_groups import (
    SUSHI_CLEANUP_RemoveEmptyVertexGroups,
)
from sushi_cleanups.remove_unused_color_maps import SUSHI_CLEANUP_RemoveUnusedColorMaps
from sushi_cleanups.remove_unused_material_slots import (
    SUSHI_CLEANUP_RemoveUnusedMaterialSlots,
)
from sushi_cleanups.remove_unused_materials import SUSHI_CLEANUP_RemoveUnusedMaterials
from sushi_cleanups.remove_unused_meshes import SUSHI_CLEANUP_RemoveUnusedMeshes
from sushi_cleanups.rename_armatures import SUSHI_CLEANUP_RenameArmatures
from sushi_cleanups.rename_meshes import SUSHI_CLEANUP_RenameMeshes
from sushi_cleanups.rename_unique_user_materials import (
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
)
from sushi_cleanups.sort_all_vertex_groups import SUSHI_CLEANUP_SortVertexGroups

OPERATIONS_ALL: Set[Operator] = {
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsAll,
    SUSHI_CLEANUP_RemoveEmptyCollections,
    SUSHI_CLEANUP_RemoveEmptyColorMapsAll,
    SUSHI_CLEANUP_RemoveEmptyUVMaps,
    SUSHI_CLEANUP_RemoveEmptyVertexGroups,
    SUSHI_CLEANUP_RemoveUnusedColorMaps,
    SUSHI_CLEANUP_RemoveUnusedMaterialSlots,
    SUSHI_CLEANUP_RemoveUnusedMaterials,
    SUSHI_CLEANUP_RemoveUnusedMeshes,
    SUSHI_CLEANUP_RenameArmatures,
    SUSHI_CLEANUP_RenameMeshes,
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
    SUSHI_CLEANUP_SortVertexGroups,
}

OPERATIONS_SELECTED: Set[Operator] = {
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsSelected,
    SUSHI_CLEANUP_RemoveEmptyColorMapsSelected,
}
