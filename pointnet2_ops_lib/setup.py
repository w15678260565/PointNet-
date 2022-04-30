import glob
import os
import os.path as osp

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
#
# this_dir = osp.dirname(osp.abspath(__file__))
# _ext_src_root = osp.join("pointnet2_ops", "_ext-src")
# _ext_sources = glob.glob(osp.join(_ext_src_root, "src", "*.cpp")) + glob.glob(
#     osp.join(_ext_src_root, "src", "*.cu")
# )
# _ext_headers = glob.glob(osp.join(_ext_src_root, "include", "*"))
#
# requirements = ["torch>=1.4"]
#
# exec(open(osp.join("pointnet2_ops", "_version.py")).read())
#
# os.environ["TORCH_CUDA_ARCH_LIST"] = "3.7+PTX;5.0;6.0;6.1;6.2;7.0;7.5"
# setup(
#     name="pointnet2_ops",
#     version=__version__,
#     author="Erik Wijmans",
#     packages=find_packages(),
#     install_requires=requirements,
#     ext_modules=[
#         CUDAExtension(
#             name="pointnet2_ops._ext",
#             sources=_ext_sources,
#             extra_compile_args={
#                 "cxx": ["-O3"],
#                 "nvcc": ["-O3", "-Xfatbin", "-compress-all"],
#             },
#             include_dirs=[osp.join(this_dir, _ext_src_root, "include")],
#         )
#     ],
#     cmdclass={"build_ext": BuildExtension},
#     include_package_data=True,
# )

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import glob
import os

_ext_src_root = "_ext_src"
_ext_sources = glob.glob("{}/src/*.cpp".format(_ext_src_root)) + glob.glob(
    "{}/src/*.cu".format(_ext_src_root)
)
_ext_headers = glob.glob("{}/include/*".format(_ext_src_root))

headers = "-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), '_ext_src', 'include')

setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension(
            name='pointnet2._ext',
            sources=_ext_sources,
            extra_compile_args={
                "cxx": ["-O2", headers],
                "nvcc": ["-O2", headers]
            },
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
