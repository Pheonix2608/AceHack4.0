from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="microsoft/DialoGPT-small",  # The model you want to download
    local_dir="F:/DialoGPT-small",       # Your custom save location
    local_dir_use_symlinks=False         # Ensures actual copy, not symlink
)
