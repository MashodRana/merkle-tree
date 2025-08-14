from lib.utils import hash_data, hash_file_content


def build_merkle_tree(items: list, is_file_paths: bool = False):
    if not items:
        return {
            "root": None,
            "tree_levels": None
        }

    nodes = []
    for item in items:
        if is_file_paths:
            node_data = {
                "hash": hash_file_content(item),
                "file_path": str(item)
            }
        else:
            node_data = {
                "hash": hash_data(item),
                "data": item
            }
        nodes.append(node_data)

    tree_levels = [nodes]
    current_level = nodes
    num_nodes = len(current_level)
    while num_nodes > 1:
        next_level = []
        for i in range(0, num_nodes, 2):
            left = current_level[i]
            if i + 1 < num_nodes:
                right = current_level[i+1]
            else:
                right = current_level[i]
            combined_hash = hash_data(left["hash"] + right["hash"])
            next_level.append({
                "hash": combined_hash,
                "left": left,
                "right": right
            })
        tree_levels.append(next_level)
        current_level = next_level
        num_nodes = len(current_level)
    return {
        "root": current_level[0],
        "tree_levels": tree_levels,
        "leaf_count": len(items)
    }
