import geocoder
import time


def get_current_location():
    """Gets the current location using IP geolocation."""
    print("Entered in get_current_location function")
    time.sleep(3)

    try:
        g = geocoder.ip('me')  # Try IP geolocation first
        if g.latlng and len(g.latlng) == 2:  # Ensure we got valid coordinates
            print(f"Current location is {g.latlng}")
            return g.latlng[0], g.latlng[1]
        else:
            print("Error: Invalid location data received.")
            return None, None

    except Exception as e:
        # Handle potential errors (e.g., no internet connection, invalid data)
        print(f"Error: Unable to retrieve current location. {e}")
        print("Using default values (None, None).")
        return None, None


def check_location_in_boundary(lat, lon, min_lat, max_lat, min_lon, max_lon):
    """Checks if a given location is within a specified boundary."""
    print("Entered in check_location_boundary function")
    time.sleep(3)
    print(
        f"Geo Values are \nmin lat: {min_lat} \ncurrent lat: {lat} \nmax lat: {max_lat}"
        f"\nmin long: {min_lon} \ncurrent long: {lon} \nmax lon : {max_lon} "
    )

    time.sleep(2)

    # Handle potential None values for lat and lon (from get_current_location)
    if lat is None or lon is None:
        print("Error: Cannot check location. Invalid coordinates (None).")
        return False

    try:
        min_lat = float(min_lat)
        max_lat = float(max_lat)
        min_lon = float(min_lon)
        max_lon = float(max_lon)
    except ValueError:
        print("error converting to float from str. check the inputs")
        return False

    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def calculate_relative_boundary_points(current_lat, current_lon, boundary_params):
    """Calculates the relative geo points of the boundary relative to the current location."""
    min_lat, max_lat, min_lon, max_lon = boundary_params

    # Handle potential None
    if current_lat is None or current_lon is None:
        print("Error: Cannot calculate relative boundary. Invalid coordinates (None).")
        return None, None, None, None

    min_lat_rel, max_lat_rel = min_lat - current_lat, max_lat - current_lat
    min_lon_rel, max_lon_rel = min_lon - current_lon, max_lon - current_lon
    return min_lat_rel, max_lat_rel, min_lon_rel, max_lon_rel


def monitor_location(boundary_params, check_interval=10):
    """Monitors the location and checks if it's within the defined boundary."""
    print("Entered in monitor_location function")
    time.sleep(3)
    min_lat, max_lat, min_lon, max_lon = boundary_params

    current_lat, current_lon = get_current_location()

    relative_min_lat, relative_max_lat, relative_min_lon, relative_max_lon = calculate_relative_boundary_points(
        current_lat, current_lon, boundary_params
    )
    time.sleep(3)

    # Print the relative boundary points
    if not (
            relative_min_lat is None or relative_max_lat is None or relative_max_lon is None or relative_min_lon is None):
        print(
            f"Relative Boundary Points:\n"
            f"  - Min Lat: {relative_min_lat:.6f}\n"
            f"  - Max Lat: {relative_max_lat:.6f}\n"
            f"  - Min Lon: {relative_min_lon:.6f}\n"
            f"  - Max Lon: {relative_max_lon:.6f}\n"
        )
    else:
        print("Unable to print relative boundary points.")
        return False

    if check_location_in_boundary(current_lat, current_lon, min_lat, max_lat, min_lon, max_lon):
        print("Good: Robot within boundary.")
        time.sleep(2)
        return True  # Robot is inside the boundary
    else:
        print("Warning: Robot outside boundary.")
        time.sleep(2)
        return False  # Robot is outside the boundary


# Example usage in your main function:
if __name__ == "__main__":
    boundary_params = (19.10292, 19.10295, 78.10253, 78.10260)  # Example boundary

    if monitor_location(boundary_params):
        # Robot is within the boundary
        print("Good: Robot within boundary. Executing move function (or other actions).")
        # Replace the following with your actual move function or robot control logic
        # move_robot()
    else:
        # Robot is outside the boundary, handle accordingly
        print("Warning: Robot outside boundary. Taking corrective actions.")
        # Add your corrective actions or robot control logic here
