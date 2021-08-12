import subprocess
import os

repositories = [
    "https://github.com/BinomialLLC/basis_universal",
    "https://github.com/DTolm/VkFFT",
    "https://github.com/g-truc/glm",
    "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator",
    "https://github.com/jarro2783/cxxopts",
    "https://github.com/KhronosGroup/glslang",
    "https://github.com/KhronosGroup/KTX-Software",
    "https://github.com/KhronosGroup/SPIRV-Headers",
    "https://github.com/KhronosGroup/SPIRV-Tools",
    "https://github.com/KhronosGroup/Vulkan-Headers",
    "https://github.com/matoya/libmatoya",
    "https://github.com/nlohmann/json",
    "https://github.com/syoyo/tinygltf",
    "https://github.com/taskflow/taskflow",
    "https://github.com/tinyobjloader/tinyobjloader",
]

try:
    os.mkdir("build")
except:
    pass

for repository in repositories:
    try:
        subprocess.run(
            [
                "git",
                "clone",
                "--recursive",
                "--single-branch",
                "--depth=1",
                "--shallow-submodules",
                repository,
            ],
            cwd="./build",
        )
    except:
        pass
