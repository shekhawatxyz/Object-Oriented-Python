import os

print("Adding .gitkeep files to empty directories...")

current_dir = os.getcwd()
for item in os.listdir(current_dir):
    full_path = os.path.join(current_dir, item)
    if os.path.isdir(full_path) and item.startswith("Chapter-"):
        # Check if directory is empty (contains no files or subdirectories)
        if not os.listdir(full_path):
            gitkeep_path = os.path.join(full_path, ".gitkeep")
            try:
                with open(gitkeep_path, "w") as f:
                    pass
                print(f"Added .gitkeep to: {item}")
            except Exception as e:
                print(f"Error adding .gitkeep to {item}: {e}")

print("")
print("Finished adding .gitkeep files.")
