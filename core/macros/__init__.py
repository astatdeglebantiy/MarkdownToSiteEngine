from core.macros.base import BaseMacro, MacroRegistry
from core.macros.common import DateMacro, LoremMacro
from core.macros.posts import PostsListMacro


def create_default_registry() -> MacroRegistry:
    registry = MacroRegistry()

    registry.register(DateMacro())
    registry.register(LoremMacro())
    registry.register(PostsListMacro())

    return registry


default_macro_registry = create_default_registry()
