def generate_command(scene, target_object):
    if target_object not in scene:
        raise ValueError(f"Target object '{target_object}' not found in the scene.")

    target_pos = scene[target_object]
    other_objects = {k: v for k, v in scene.items() if k != target_object}

    # Find the nearest object
    nearest_object = min(other_objects,
                         key=lambda x: ((scene[x][0] - target_pos[0]) ** 2 + (scene[x][1] - target_pos[1]) ** 2) ** 0.5)

    # Determine relative position
    dx = target_pos[0] - scene[nearest_object][0]
    dy = target_pos[1] - scene[nearest_object][1]

    if dx > 0 and dy > 0:
        direction = "top-right"
    elif dx > 0 and dy < 0:
        direction = "bottom-right"
    elif dx < 0 and dy > 0:
        direction = "top-left"
    elif dx < 0 and dy < 0:
        direction = "bottom-left"
    elif dx == 0 and dy > 0:
        direction = "above"
    elif dx == 0 and dy < 0:
        direction = "below"
    elif dx > 0 and dy == 0:
        direction = "to the right of"
    else:
        direction = "to the left of"

    # Generate command
    command = f"Grab the item {direction} the {nearest_object}. It's crucial for our current task and needs immediate retrieval."

    return command


scene = {
    "SourMilkDrink": (28, 75),
    "SweetMilkDrink": (-2, 55),
    "Coffee": (2, 57)
}
target_object = "SourMilkDrink"
print(generate_command(scene, target_object))
