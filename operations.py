from typing import List, Set

from bpy.types import Operator

from sushi_cleanups.remove_empty_bone_groups import (
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsAll,
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsSelected,
)
from sushi_cleanups.remove_empty_collections import SUSHI_CLEANUP_RemoveEmptyCollections
from sushi_cleanups.remove_empty_uv_maps import (
    SUSHI_CLEANUP_RemoveEmptyUVMapsAll,
    SUSHI_CLEANUP_RemoveEmptyUVMapsSelected,
)
from sushi_cleanups.remove_empty_vertex_colors import (
    SUSHI_CLEANUP_RemoveEmptyVertexColorsAll,
    SUSHI_CLEANUP_RemoveEmptyVertexColorsSelected,
)
from sushi_cleanups.remove_empty_vertex_groups import (
    SUSHI_CLEANUP_RemoveEmptyVertexGroupsAll,
    SUSHI_CLEANUP_RemoveEmptyVertexGroupsSelected,
)
from sushi_cleanups.remove_unused_armatures import SUSHI_CLEANUP_RemoveUnusedArmatures
from sushi_cleanups.remove_unused_material_slots import (
    SUSHI_CLEANUP_RemoveUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_RemoveUnusedMaterialSlotsSelected,
)
from sushi_cleanups.remove_unused_materials import SUSHI_CLEANUP_RemoveUnusedMaterials
from sushi_cleanups.remove_unused_meshes import SUSHI_CLEANUP_RemoveUnusedMeshes
from sushi_cleanups.remove_unused_uv_maps import (
    SUSHI_CLEANUP_RemoveUnusedUVMapsAll,
    SUSHI_CLEANUP_RemoveUnusedUVMapsSelected,
)
from sushi_cleanups.remove_unused_vertex_colors import (
    SUSHI_CLEANUP_RemoveUnusedVertexColorsAll,
    SUSHI_CLEANUP_RemoveUnusedVertexColorsSelected,
)
from sushi_cleanups.rename_unique_armatures import SUSHI_CLEANUP_RenameUniqueArmatures
from sushi_cleanups.rename_unique_meshes import SUSHI_CLEANUP_RenameUniqueMeshes
from sushi_cleanups.rename_unique_user_materials import (
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
)
from sushi_cleanups.sort_all_vertex_groups import SUSHI_CLEANUP_SortVertexGroups

OPERATIONS_ALL: Set[Operator] = {
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsAll,
    SUSHI_CLEANUP_RemoveEmptyCollections,
    SUSHI_CLEANUP_RemoveEmptyUVMapsAll,
    SUSHI_CLEANUP_RemoveEmptyVertexColorsAll,
    SUSHI_CLEANUP_RemoveEmptyVertexGroupsAll,
    SUSHI_CLEANUP_RemoveUnusedArmatures,
    SUSHI_CLEANUP_RemoveUnusedMaterials,
    SUSHI_CLEANUP_RemoveUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_RemoveUnusedMeshes,
    SUSHI_CLEANUP_RemoveUnusedVertexColorsAll,
    SUSHI_CLEANUP_RemoveUnusedUVMapsAll,
    SUSHI_CLEANUP_RenameUniqueArmatures,
    SUSHI_CLEANUP_RenameUniqueMeshes,
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
    SUSHI_CLEANUP_SortVertexGroups,
}

OPERATIONS_SELECTED: Set[Operator] = {
    SUSHI_CLEANUP_RemoveEmptyBoneGroupsSelected,
    SUSHI_CLEANUP_RemoveEmptyUVMapsSelected,
    SUSHI_CLEANUP_RemoveEmptyVertexColorsSelected,
    SUSHI_CLEANUP_RemoveEmptyVertexGroupsSelected,
    SUSHI_CLEANUP_RemoveUnusedMaterialSlotsSelected,
    SUSHI_CLEANUP_RemoveUnusedUVMapsSelected,
    SUSHI_CLEANUP_RemoveUnusedVertexColorsSelected,
}

OPERATION_CLASSES: List[Operator] = list(OPERATIONS_ALL) + list(OPERATIONS_SELECTED)
