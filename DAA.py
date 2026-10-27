import sys
import os

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.subs = []

def build_tree(structure, root_name):
    nodes = {}
    for manager, reports in structure.items():
        nodes.setdefault(manager, TreeNode(manager))
        for r in reports:
            nodes.setdefault(r, TreeNode(r))
            nodes[manager].subs.append(nodes[r])
    return nodes[root_name]

def get_comms_team(root):
    if not root:
        return []

    dp = {}
    best_sub_state1 = {}

    def dfs(u):
        if not u.subs:
            dp[u] = [1, float('inf'), 0]
            return

        for v in u.subs:
            dfs(v)

        dp_u_0 = 1 + sum(min(dp[v][0], dp[v][2]) for v in u.subs)
        dp_u_2 = sum(min(dp[v][0], dp[v][1]) for v in u.subs)
        base_sum = sum(min(dp[v][0], dp[v][1]) for v in u.subs)

        if any(dp[v][0] <= dp[v][1] for v in u.subs):
            dp_u_1 = base_sum
            for v in u.subs:
                if dp[v][0] <= dp[v][1]:
                    best_sub_state1[u] = v
                    break
        else:
            dp_u_1 = float('inf')
            best_child = None
            for v in u.subs:
                cost = base_sum - dp[v][1] + dp[v][0]
                if cost < dp_u_1:
                    dp_u_1 = cost
                    best_child = v
            best_sub_state1[u] = best_child

        dp[u] = [dp_u_0, dp_u_1, dp_u_2]

    dfs(root)
    team_members = set()

    def reconstruct(u, state):
        if state == 0:
            team_members.add(u.val)
            for v in u.subs:
                if dp[v][0] <= dp[v][2]:
                    reconstruct(v, 0)
                else:
                    reconstruct(v, 2)
        elif state == 2:
            for v in u.subs:
                if dp[v][0] <= dp[v][1]:
                    reconstruct(v, 0)
                else:
                    reconstruct(v, 1)
        elif state == 1:
            chosen_v = best_sub_state1.get(u)
            for v in u.subs:
                if v == chosen_v:
                    reconstruct(v, 0)
                else:
                    if dp[v][0] <= dp[v][1]:
                        reconstruct(v, 0)
                    else:
                        reconstruct(v, 1)

    if dp[root][0] <= dp[root][1]:
        reconstruct(root, 0)
    else:
        reconstruct(root, 1)

    return list(team_members)

if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            input_data = f.read().splitlines()
    else:
        print("Enter hierarchy (Manager: Sub1, Sub2) then press Ctrl+D:")
        input_data = sys.stdin.read().splitlines()

    hierarchy = {}
    for line in input_data:
        if not line.strip():
            continue
        parts = line.split(":")
        manager = parts[0].strip()
        if len(parts) > 1 and parts[1].strip():
            subs = [s.strip() for s in parts[1].split(",")]
        else:
            subs = []
        hierarchy[manager] = subs

    if not hierarchy:
        print("Error: No structure provided.")
        sys.exit(1)

    all_managers = set(hierarchy.keys())
    all_subs = set(v for sub_list in hierarchy.values() for v in sub_list)
    root_candidates = all_managers - all_subs

    if not root_candidates:
        print("Error: Cyclic structure detected or no root found.")
        sys.exit(1)

    root_name = list(root_candidates)[0]
    root_node = build_tree(hierarchy, root_name)
    team = get_comms_team(root_node)

    print(f"\nOptimal Communications Team: {team}")
