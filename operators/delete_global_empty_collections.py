from typing import Optional, Set

import bpy
from bpy.types import Collection, Context

from sushi_cleanups.operators.sushi_base_operator import SushiBaseOperator


class SUSHI_CLEANUP_DeleteEmptyCollections(SushiBaseOperator):
    bl_idname = "sushi_cleanup.delete_empty_collections"
    bl_label = "Delete Empty Collections"
    bl_description = "Deletes collections with no children and collapses collections with only one collection children"

    sk_tags = {"ALL", "COLLECTION", "EMPTY", "DELETE"}

    def execute(self, context: Context) -> Set[str]:
        root = bpy.data.scenes["Scene"].collection

        self._delete_empty_collections(root)
        self._delete_redundant_collections(None, root)

        return {"FINISHED"}

    def _delete_empty_collections(self, root: Collection) -> None:
        for child in root.children:
            self._delete_empty_collections(child)

        if len(root.all_objects) == 0:
            bpy.data.collections.remove(root)
            return

    def _delete_redundant_collections(
        self, parent: Optional[Collection], root: Collection
    ) -> None:
        for child in root.children:
            self._delete_redundant_collections(root, child)

        if parent and len(root.objects) == 0:
            for child in root.children:
                parent.children.link(child)
                root.children.unlink(child)

            bpy.data.collections.remove(root)

            return

    @classmethod
    def poll(cls, context: Context):
        return len(bpy.data.collections) > 0
