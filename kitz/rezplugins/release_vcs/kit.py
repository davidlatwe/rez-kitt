
import os
from rezplugins.release_vcs import git


class KitReleaseVCS(git.GitReleaseVCS):

    schema_dict = {
        "allow_no_upstream": bool}

    @classmethod
    def name(cls):
        return "kit"

    def __init__(self, pkg_root, vcs_root=None):
        self.is_kit = self.is_valid_kit_root(pkg_root)
        super(KitReleaseVCS, self).__init__(pkg_root, vcs_root=vcs_root)

    @classmethod
    def is_valid_root(cls, path):
        return os.path.isdir(os.path.join(path, ".git"))

    @classmethod
    def is_valid_kit_root(cls, path):
        return os.path.isfile(os.path.join(path, ".kit"))

    @classmethod
    def find_vcs_root(cls, path):
        result = super(KitReleaseVCS, cls).find_vcs_root(path)
        if result is not None:
            vcs_path, levels_up = result
            if cls.is_valid_kit_root(path):
                return vcs_path, -1  # pop-up
            else:
                return vcs_path, 9999  # or, back down

    def git(self, *nargs):
        if self.is_kit and nargs[0] in {"log", "diff-index"}:
            nargs = list(nargs) + ["--", "*"]
        return self._cmd(self.executable, *nargs)


def register_plugin():
    return KitReleaseVCS
