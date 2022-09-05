from bpy.props import BoolProperty
from bpy.types import AddonPreferences, Context

from sushi_cleanups.version import ADDON_NAME


class SushiCleanupsAddonPreferences(AddonPreferences):
    bl_idname = ADDON_NAME

    enable_experimental_features: BoolProperty(
        name="Enable Experimental Features",
        default=False,
        description="Enable features that are still in development and testing",
    )

    def draw(self, context: Context):
        layout = self.layout

        layout.prop(self, "enable_experimental_features")
