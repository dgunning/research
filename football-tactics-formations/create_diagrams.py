#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Generate ASCII diagrams for football formations.
Creates visual representations of various tactical formations.
"""

def create_formation_diagram(formation_name, positions):
    """
    Create an ASCII diagram for a football formation.

    Args:
        formation_name: Name of the formation (e.g., "4-4-2")
        positions: Dict with keys as lines (0=GK, 1=DEF, 2=MID, 3=ATT)
                   and values as lists of player positions
    """
    width = 50
    height = 24

    # Create empty field
    field = [[' ' for _ in range(width)] for _ in range(height)]

    # Draw field boundaries
    for i in range(height):
        field[i][0] = '|'
        field[i][width-1] = '|'

    for j in range(width):
        field[0][j] = '-'
        field[height-1][j] = '-'

    # Corners
    field[0][0] = '+'
    field[0][width-1] = '+'
    field[height-1][0] = '+'
    field[height-1][width-1] = '+'

    # Draw halfway line
    halfway = height // 2
    for j in range(1, width-1):
        field[halfway][j] = '-'

    # Draw center circle
    center_x = width // 2
    field[halfway][center_x] = 'o'

    # Place players
    # GK at bottom
    if 'GK' in positions:
        gk_y = height - 3
        gk_x = width // 2
        field[gk_y][gk_x] = 'G'

    # Defenders
    if 'DEF' in positions:
        def_y = height - 7
        def_count = len(positions['DEF'])
        spacing = width // (def_count + 1)
        for i, player in enumerate(positions['DEF']):
            x = spacing * (i + 1)
            field[def_y][x] = player

    # Midfielders
    if 'MID' in positions:
        mid_y = height - 13
        mid_count = len(positions['MID'])
        spacing = width // (mid_count + 1)
        for i, player in enumerate(positions['MID']):
            x = spacing * (i + 1)
            field[mid_y][x] = player

    # Additional midfield line (for formations with multiple mid lines)
    if 'MID2' in positions:
        mid2_y = height - 10
        mid2_count = len(positions['MID2'])
        spacing = width // (mid2_count + 1)
        for i, player in enumerate(positions['MID2']):
            x = spacing * (i + 1)
            field[mid2_y][x] = player

    # Attacking midfielders
    if 'ATT_MID' in positions:
        att_mid_y = height - 16
        att_mid_count = len(positions['ATT_MID'])
        spacing = width // (att_mid_count + 1)
        for i, player in enumerate(positions['ATT_MID']):
            x = spacing * (i + 1)
            field[att_mid_y][x] = player

    # Forwards
    if 'FWD' in positions:
        fwd_y = height - 19
        fwd_count = len(positions['FWD'])
        spacing = width // (fwd_count + 1)
        for i, player in enumerate(positions['FWD']):
            x = spacing * (i + 1)
            field[fwd_y][x] = player

    # Convert to string
    diagram = f"\n{formation_name} Formation:\n"
    diagram += "Attacking Direction: ↑\n\n"
    for row in field:
        diagram += ''.join(row) + '\n'

    return diagram


# Define all formations
formations = {
    "4-4-2": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D', 'D'],
        "MID": ['M', 'M', 'M', 'M'],
        "FWD": ['F', 'F']
    },
    "4-3-3": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D', 'D'],
        "MID": ['M', 'M', 'M'],
        "FWD": ['W', 'F', 'W']
    },
    "3-5-2": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D'],
        "MID": ['W', 'M', 'M', 'M', 'W'],
        "FWD": ['F', 'F']
    },
    "4-2-3-1": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D', 'D'],
        "MID": ['M', 'M'],
        "ATT_MID": ['W', 'A', 'W'],
        "FWD": ['F']
    },
    "4-3-2-1": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D', 'D'],
        "MID": ['M', 'M', 'M'],
        "ATT_MID": ['A', 'A'],
        "FWD": ['F']
    },
    "4-1-2-1-2": {
        "GK": ["GK"],
        "DEF": ['D', 'D', 'D', 'D'],
        "MID": ['M'],
        "MID2": ['M', 'M'],
        "ATT_MID": ['A'],
        "FWD": ['F', 'F']
    }
}

# Generate all diagrams
all_diagrams = ""
for formation, positions in formations.items():
    all_diagrams += create_formation_diagram(formation, positions)
    all_diagrams += "\n" + "="*50 + "\n"

print(all_diagrams)

# Save to file
with open('formation_diagrams.txt', 'w') as f:
    f.write(all_diagrams)

print("\nDiagrams saved to formation_diagrams.txt")
