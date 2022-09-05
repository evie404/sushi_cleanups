from typing import Set

from sushi_cleanups.operators.bone_align_connect import (
    SUSHI_CLEANUP_BoneAlignConnectParentsHead,
)
from sushi_cleanups.operators.bone_connect import (
    SUSHI_CLEANUP_BoneSetConnected,
    SUSHI_CLEANUP_BoneUnsetConnected,
)
from sushi_cleanups.operators.bone_parent_to_active import (
    SUSHI_CLEANUP_BoneParentToActive,
)
from sushi_cleanups.operators.bone_print import (
    SUSHI_CLEANUP_BonePrintDict,
    SUSHI_CLEANUP_BonePrintList,
)
from sushi_cleanups.operators.copy_object_custom_properties import (
    SUSHI_CLEANUP_CopyCustomPropertiesToSelected,
    SUSHI_CLEANUP_CopyCustomPropertiesWithDriversToSelected,
)
from sushi_cleanups.operators.dedup_names import SUSHI_CLEANUP_DedupNames
from sushi_cleanups.operators.delete_armature_empty_bone_groups import (
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
)
from sushi_cleanups.operators.delete_global_empty_collections import (
    SUSHI_CLEANUP_DeleteEmptyCollections,
)
from sushi_cleanups.operators.delete_global_unused_armatures import (
    SUSHI_CLEANUP_DeleteUnusedArmatures,
)
from sushi_cleanups.operators.delete_global_unused_materials import (
    SUSHI_CLEANUP_DeleteUnusedMaterials,
)
from sushi_cleanups.operators.delete_global_unused_meshes import (
    SUSHI_CLEANUP_DeleteUnusedMeshes,
)
from sushi_cleanups.operators.delete_mesh_empty_uv_maps import (
    SUSHI_CLEANUP_DeleteEmptyUVMapsAll,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
)
from sushi_cleanups.operators.delete_mesh_empty_vertex_colors import (
    SUSHI_CLEANUP_DeleteEmptyVertexColorsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
)
from sushi_cleanups.operators.delete_mesh_empty_vertex_groups import (
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
)
from sushi_cleanups.operators.delete_mesh_unused_material_slots import (
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
)
from sushi_cleanups.operators.delete_mesh_unused_uv_maps import (
    SUSHI_CLEANUP_DeleteUnusedUVMapsAll,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
)
from sushi_cleanups.operators.delete_mesh_unused_vertex_colors import (
    SUSHI_CLEANUP_DeleteUnusedVertexColorsAll,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
)
from sushi_cleanups.operators.delete_similar_same_material import (
    SUSHI_CLEANUP_DeleteSameMaterialObjects,
)
from sushi_cleanups.operators.delete_similar_same_mesh import (
    SUSHI_CLEANUP_DeleteSameMeshObjects,
)
from sushi_cleanups.operators.rename_global_unique_armatures import (
    SUSHI_CLEANUP_RenameUniqueArmatures,
)
from sushi_cleanups.operators.rename_global_unique_meshes import (
    SUSHI_CLEANUP_RenameUniqueMeshes,
)
from sushi_cleanups.operators.rename_global_unique_user_materials import (
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
)
from sushi_cleanups.operators.sort_global_all_vertex_groups import (
    SUSHI_CLEANUP_SortVertexGroups,
)
from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator

ALL_OPERATIONS: Set[SushiBaseOperator] = {
    SUSHI_CLEANUP_DedupNames,
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyBoneGroupsSelected,
    SUSHI_CLEANUP_DeleteEmptyCollections,
    SUSHI_CLEANUP_DeleteEmptyUVMapsAll,
    SUSHI_CLEANUP_DeleteEmptyUVMapsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexColorsSelected,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsAll,
    SUSHI_CLEANUP_DeleteEmptyVertexGroupsSelected,
    SUSHI_CLEANUP_DeleteSameMaterialObjects,
    SUSHI_CLEANUP_DeleteSameMeshObjects,
    SUSHI_CLEANUP_DeleteUnusedArmatures,
    SUSHI_CLEANUP_DeleteUnusedMaterials,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsAll,
    SUSHI_CLEANUP_DeleteUnusedMaterialSlotsSelected,
    SUSHI_CLEANUP_DeleteUnusedMeshes,
    SUSHI_CLEANUP_DeleteUnusedUVMapsAll,
    SUSHI_CLEANUP_DeleteUnusedUVMapsSelected,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsAll,
    SUSHI_CLEANUP_DeleteUnusedVertexColorsSelected,
    SUSHI_CLEANUP_RenameUniqueArmatures,
    SUSHI_CLEANUP_RenameUniqueMeshes,
    SUSHI_CLEANUP_RenameUniqueUserMaterials,
    SUSHI_CLEANUP_SortVertexGroups,
    SUSHI_CLEANUP_CopyCustomPropertiesToSelected,
    SUSHI_CLEANUP_CopyCustomPropertiesWithDriversToSelected,
    SUSHI_CLEANUP_BoneParentToActive,
    SUSHI_CLEANUP_BoneSetConnected,
    SUSHI_CLEANUP_BoneUnsetConnected,
    SUSHI_CLEANUP_BoneAlignConnectParentsHead,
    SUSHI_CLEANUP_BonePrintDict,
    SUSHI_CLEANUP_BonePrintList,
}

DELETE_ALL: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "ALL" in x.sk_tags and "DELETE" in x.sk_tags
}

DELETE_SELECTED: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "SELECTED" in x.sk_tags and "DELETE" in x.sk_tags
}

DELETE_SIMILAR: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "SIMILAR" in x.sk_tags and "DELETE" in x.sk_tags
}

RENAME_ALL: Set[SushiBaseOperator] = {
    x
    for x in ALL_OPERATIONS
    if "ALL" in x.sk_tags and "RENAME" in x.sk_tags and "DATA" not in x.sk_tags
}

RENAME_ALL_DATA: Set[SushiBaseOperator] = {
    x
    for x in ALL_OPERATIONS
    if "ALL" in x.sk_tags and "RENAME" in x.sk_tags and "DATA" in x.sk_tags
}


RENAME_SELECTED: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "SELECTED" in x.sk_tags and "RENAME" in x.sk_tags
}

SORT_ALL: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "ALL" in x.sk_tags and "SORT" in x.sk_tags
}

SORT_SELECTED: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "SELECTED" in x.sk_tags and "SORT" in x.sk_tags
}

COPY_FROM_TO: Set[SushiBaseOperator] = {
    x for x in ALL_OPERATIONS if "COPY" in x.sk_tags and "FROM_TO" in x.sk_tags
}

BONE_ALL: Set[SushiBaseOperator] = {x for x in ALL_OPERATIONS if "BONE" in x.sk_tags}
