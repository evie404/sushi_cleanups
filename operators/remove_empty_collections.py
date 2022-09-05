from typing import Optional, Set

import bpy
from bpy.types import Collection, Context


class SUSHI_CLEANUP_RemoveEmptyCollections(bpy.types.Operator):
    bl_idname = "sushi_cleanup.remove_empty_collections"
    bl_label = "Remove Empty Collections"
    bl_description = "Removes collections with no children and collapses collections with only one collection children"
    bl_options = {"UNDO"}

    sk_tags = {"ALL", "COLLECTION", "EMPTY", "REMOVE"}

    def execute(self, context: Context) -> Set[str]:
        root = bpy.data.scenes["Scene"].collection

        self._remove_empty_collections(root)
        self._remove_redundant_collections(None, root)

        return {"FINISHED"}

    def _remove_empty_collections(self, root: Collection) -> None:
        for child in root.children:
            self._remove_empty_collections(child)

        if len(root.all_objects) == 0:
            bpy.data.collections.remove(root)
            return

    def _remove_redundant_collections(
        self, parent: Optional[Collection], root: Collection
    ) -> None:
        for child in root.children:
            self._remove_redundant_collections(root, child)

        if parent and len(root.objects) == 0:
            for child in root.children:
                parent.children.link(child)
                root.children.unlink(child)

            bpy.data.collections.remove(root)

            return
