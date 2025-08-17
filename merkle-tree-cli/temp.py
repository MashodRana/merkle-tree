from lib.utils import hash_data


words = ["Say", "you", "want", "to", "prove", "to", "someone", "that", "File", "A", "is", "part", "of", "the", "dataset", "without", "giving", "all", "files"]

def build_merkle_tree(words):
    leaf_nodes = [
        {"hash": hash_data(w), "data": w} for w in words
    ]
    tree = [leaf_nodes]
    clevel = leaf_nodes
    nnodes = len(clevel)
    while nnodes>1:
        next_level = []
        for i in range(0, nnodes, 2):
            left = clevel[i]
            if i+1 < nnodes:
                right = clevel[i + 1]
            else:
                right = clevel[i]
            next_level.append({
                "hash": hash_data(left["hash"]+right["hash"]),
                "left": left,
                "right": right
            })
        tree.append(next_level)
        clevel = next_level
        nnodes = len(clevel)
    return {
        "root": clevel[0],
        "tree": tree,
        "leaf_nodes": leaf_nodes
    }

info = build_merkle_tree(words)
print(info["root"]["hash"])

def get_merkle_proof(thash, tree, leaf_nodes) -> list[str]:
    """Generate Merkle proof for a file."""
    index = None
    for i, leaf_node in enumerate(leaf_nodes):
        if leaf_node["hash"]==thash:
            index = i
            break
    if index is None:
        return None

    proof = []
    cindex = index
    for i in range(0, len(tree)-1, 1):
        clevel = tree[i]
        is_right_node = cindex % 2
        sibling_index = cindex-1 if is_right_node else cindex+1
        if sibling_index < len(clevel):
            proof.append({
                "hash": clevel[sibling_index]["hash"],
                "position": "left" if is_right_node else "right"
            })
        else:
            proof.append({
                "hash": clevel[cindex]["hash"],
                "position": "left" if is_right_node else "right"
            })
        cindex = cindex // 2
    return proof

thash = hash_data("someone")
print(thash)
ptree = get_merkle_proof(thash=thash, tree=info["tree"], leaf_nodes=info["leaf_nodes"])
print(ptree)

def verify_merkle_proof(thash, ptree):
    chash = thash
    for node in ptree:
        if node["position"]=="right":
            chash = hash_data(chash + node["hash"])
        else:
            chash = hash_data(node["hash"]+chash)
    return chash

print(verify_merkle_proof(thash, ptree=ptree))