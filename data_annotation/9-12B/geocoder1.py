import geocoder
import time


def get_current_location():
    print("Entered in get_current_location function")
    time.sleep(3)

    try:
        g = geocoder.ip('me')  # Try IP geolocation first
        print(f"Current location is {g.latlng}")
        return g.lat, g.lng
    except (geocoder.GeocoderError, ValueError):
        # Handle potential errors (e.g., no internet connection, invalid data)
        print("Error: Unable to retrieve current location. Using default values (None, None).")
        return None, None


def check_location_in_boundary(lat, lon, min_lat, max_lat, min_lon, max_lon):
    print("Entered in check_location_boundary function")
    time.sleep(3)
    print(f"Geo Values are \nmin lat: {min_lat} \ncurrent lat: {lat} \nmax lat: {max_lat}"
          f"\nmin long: {min_lon} \ncurrent long: {lon} \nmax lon : {max_lon} ")

    time.sleep(5)
    min_lat = float(min_lat)
    max_lat = float(max_lat)
    min_lon = float(min_lon)
    max_lon = float(max_lon)

    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def calculate_relative_boundary_points(current_lat, current_lon, boundary_params):
    """
    Calculates the relative geo points of the boundary relative to the current location.

    Args:
        current_lat (float): Current latitude of the robot.
        current_lon (float): Current longitude of the robot.
        boundary_params (tuple): Boundary parameters (min_lat, max_lat, min_lon, max_lon).

    Returns:
        tuple: A tuple containing relative latitudes and longitudes of the boundary points.
    """
    min_lat, max_lat, min_lon, max_lon = boundary_params
    min_lat_rel, max_lat_rel = min_lat - current_lat, max_lat - current_lat
    min_lon_rel, max_lon_rel = min_lon - current_lon, max_lon - current_lon
    return min_lat_rel, max_lat_rel, min_lon_rel, max_lon_rel


def monitor_location(boundary_params, check_interval=10):
    print("Entered in monitor_location function")
    time.sleep(3)

    min_lat, max_lat, min_lon, max_lon = boundary_params
    current_lat, current_lon = get_current_location()

    if current_lat is None or current_lon is None:
        print("Error: Could not retrieve current location.")
        return

    # Calculate relative boundary points
    relative_min_lat, relative_max_lat, relative_min_lon, relative_max_lon = calculate_relative_boundary_points(
        current_lat, current_lon, boundary_params
    )

    # Print the relative boundary points
    print(
        f"Relative Boundary Points:\n"
        f"  - Min Lat: {relative_min_lat:.4f}\n"
        f"  - Max Lat: {relative_max_lat:.4f}\n"
        f"  - Min Lon: {relative_min_lon:.4f}\n"
        f"  - Max Lon: {relative_max_lon:.4f}\n"
    )

    # Check if the current location is within the boundary
    if check_location_in_boundary(current_lat, current_lon, min_lat, max_lat, min_lon, max_lon):
        print("Good: Robot within bouTRgndary. Executing move function.")
        # Replace with your actual move function (for testing, this will print a message)
        # move_robot()
    else:
        print("Warning: Robot outside boundary. Taking corrective action.")


# Example usage
boundary_params = (19.10292, 19.10295, 78.10253, 78.10260)
monitor_location(boundary_params)