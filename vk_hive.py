import subprocess
import os
repositories = [
    "https://github.com/BinomialLLC/basis_universal",
    "https://github.com/DTolm/VkFFT",
    "https://github.com/g-truc/glm",
    "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator",
    "https://github.com/KhronosGroup/glslang",
    "https://github.com/KhronosGroup/SPIRV-Headers",
    "https://github.com/KhronosGroup/SPIRV-Tools",
    "https://github.com/KhronosGroup/Vulkan-Headers",
    "https://github.com/syoyo/tinygltf",
    "https://github.com/tinyobjloader/tinyobjloader",
]

try:
    os.mkdir("build")
except:
    pass

for repository in repositories:
    try:
        subprocess.Popen(["git", "clone", "--single-branch",
                          "--depth=1", repository], cwd="./build")
    except:
        pass