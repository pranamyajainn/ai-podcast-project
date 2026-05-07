# Models

Only lightweight model repository pointers belong in Git.

Tracked:

- `models/MuseTalk` as a Git submodule

Not tracked:

- model weights
- checkpoints
- generated samples
- caches

Initialize submodules:

```bash
git submodule update --init --recursive
```

Download MuseTalk weights on the CUDA machine:

```bash
cd models/MuseTalk
bash download_weights.sh
```
