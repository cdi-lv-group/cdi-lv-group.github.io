__all__ = ["run_sync"]


def __getattr__(name):
    if name == "run_sync":
        from .pipeline import run_sync

        return run_sync
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
