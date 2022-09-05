from typing import List, Set

from bpy.types import Operator

from .operators.delete_empty_bone_groups import (
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
)
from .operators.delete_empty_collections import SUSHI_CLEANUP_DeleteEmptyCollections
from .operators.delete_empty_uv_maps import (
    SUSHI_CLEANUP_DeleteEmptyUVMapsAll,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
)
from .operators.delete_empty_vertex_colors import (
    SUSHI_CLEANUP_DeleteEmptyVertexColorsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
)
from .operators.delete_empty_vertex_groups import (
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
)
from .operators.delete_unused_armatures import SUSHI_CLEANUP_DeleteUnusedArmatures
from .operators.delete_unused_material_slots import (
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
)
from .operators.delete_unused_materials import SUSHI_CLEANUP_DeleteUnusedMaterials
from .operators.delete_unused_meshes import SUSHI_CLEANUP_DeleteUnusedMeshes
from .operators.delete_unused_uv_maps import (
    SUSHI_CLEANUP_DeleteUnusedUVMapsAll,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
)
from .operators.delete_unused_vertex_colors import (
    SUSHI_CLEANUP_DeleteUnusedVertexColorsAll,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
)
from .operators.rename_unique_armatures import SUSHI_CLEANUP_RenameUniqueArmatures
from .operators.rename_unique_meshes import SUSHI_CLEANUP_RenameUniqueMeshes
from .operators.rename_unique_user_materials import (
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
)
from .operators.sort_all_vertex_groups import SUSHI_CLEANUP_SortVertexGroups

OPERATIONS_ALL: Set[Operator] = {
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyCollections,
    SUSHI_CLEANUP_DeleteEmptyUVMapsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll,
    SUSHI_CLEANUP_DeleteUnusedArmatures,
    SUSHI_CLEANUP_DeleteUnusedMaterials,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_DeleteUnusedMeshes,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsAll,
    SUSHI_CLEANUP_DeleteUnusedUVMapsAll,
    SUSHI_CLEANUP_RenameUniqueArmatures,
    SUSHI_CLEANUP_RenameUniqueMeshes,
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
    SUSHI_CLEANUP_SortVertexGroups,
}

OPERATIONS_SELECTED: Set[Operator] = {
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
}

OPERATION_CLASSES: List[Operator] = list(OPERATIONS_ALL) + list(OPERATIONS_SELECTED)
