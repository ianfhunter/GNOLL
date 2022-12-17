from platform import uname

from setuptools import setup


def in_wsl() -> bool:
    return "microsoft-standard" in uname().release


try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

except ImportError:
    bdist_wheel = None

if in_wsl():
    setup()
else:
    setup(cmdclass={"bdist_wheel": bdist_wheel}, )
