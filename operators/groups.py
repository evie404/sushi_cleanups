from typing import Set

from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator

from .delete_empty_bone_groups import (
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
)
from .delete_empty_collections import SUSHI_CLEANUP_DeleteEmptyCollections
from .delete_empty_uv_maps import (
    SUSHI_CLEANUP_DeleteEmptyUVMapsAll,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
)
from .delete_empty_vertex_colors import (
    SUSHI_CLEANUP_DeleteEmptyVertexColorsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
)
from .delete_empty_vertex_groups import (
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
)
from .delete_unused_armatures import SUSHI_CLEANUP_DeleteUnusedArmatures
from .delete_unused_material_slots import (
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
)
from .delete_unused_materials import SUSHI_CLEANUP_DeleteUnusedMaterials
from .delete_unused_meshes import SUSHI_CLEANUP_DeleteUnusedMeshes
from .delete_unused_uv_maps import (
    SUSHI_CLEANUP_DeleteUnusedUVMapsAll,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
)
from .delete_unused_vertex_colors import (
    SUSHI_CLEANUP_DeleteUnusedVertexColorsAll,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
)
from .rename_unique_armatures import SUSHI_CLEANUP_RenameUniqueArmatures
from .rename_unique_meshes import SUSHI_CLEANUP_RenameUniqueMeshes
from .rename_unique_user_materials import SUSHI_CLEANUP_RenameUniqueUserMaterials
from .sort_all_vertex_groups import SUSHI_CLEANUP_SortVertexGroups

OPERATIONS_ALL: Set[SushiBaseOperator] = {
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
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
}
