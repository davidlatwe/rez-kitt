
# Rez's default package path excluded
local_packages_path = "~/rez/kitt/install"
release_packages_path = "~/rez/kitt/release"
packages_path = [
    local_packages_path,
    release_packages_path,
]


platform_map = {
    "os": {
        r"windows-6.1(.*)": r"windows-7",
        r"windows-6.2(.*)": r"windows-8",
        r"windows-6.3(.*)": r"windows-8.1",
        r"windows-10(.*)": r"windows-10.0",
    },
}
