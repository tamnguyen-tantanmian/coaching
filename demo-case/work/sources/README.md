# Sources

The original data of the Discover stage. This folder is split in two so that real data never mixes with what the AI reads:

| Folder | Holds | Does the AI tool read it? | Goes to GitHub? |
|---|---|---|---|
| `_raw-private/` | Original data, not anonymised | **No** | **No** |
| `anonymised/` | The anonymised version, with IDs | Yes | Yes (private repo) |

The flow: raw, you anonymise it yourself, then save it into `anonymised/`. Details are in the README of each folder.
