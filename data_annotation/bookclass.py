class VideoCatalogEntry:
    def __init__(self, title, director, release_year, genre, format, duration):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.format = format  # DVD, Blu-ray, Digital, etc.
        self.duration = duration  # In minutes

        # Optional fields (add as needed)
        self.actors = []  # List of actor names
        self.rating = None  # MPAA rating, TV rating, etc.
        self.summary = None  # Short plot synopsis
        self.tags = []      # Keywords for search/filtering
        self.language = None

    def __str__(self):
        """Provides a basic string representation for display."""
        return f"{self.title} ({self.release_year}) - Directed by {self.director}"

    # Add methods for updating/modifying the catalog entry later if needed.

# my_video = VideoCatalogEntry("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", "Blu-ray", 142)
# my_video.actors = ["Tim Robbins", "Morgan Freeman"]
# my_video.rating = "R"
# my_video.tags = ["prison", "friendship", "hope"]
#
# print(my_video)
# # Output: The Shawshank Redemption (1994) - Directed by Frank Darabont

from datetime import datetime, timedelta

class VideoInventory:
    def __init__(self):
        self.catalog = {}  # Key: Video title, Value: VideoCatalogEntry
        self.rented_videos = {}  # Key: Video title, Value: (Renter name, Due date)

    def add_video(self, video: VideoCatalogEntry):
        """Adds a video to the inventory."""
        self.catalog[video.title] = video

    def rent_video(self, title, renter_name):
        """Marks a video as rented and sets a due date (e.g., 7 days from now)."""
        if title in self.catalog and title not in self.rented_videos:
            due_date = datetime.now() + timedelta(days=7)  # Adjust rental period as needed
            self.rented_videos[title] = (renter_name, due_date)
        else:
            raise ValueError("Video not available or already rented.")

    def return_video(self, title):
        """Marks a video as returned."""
        if title in self.rented_videos:
            del self.rented_videos[title]
        else:
            raise ValueError("Video not currently rented.")

    def is_available(self, title):
        """Checks if a video is available for rent."""
        return title in self.catalog and title not in self.rented_videos

    def list_available_videos(self):
        """Lists all videos currently available for rent."""
        for title, video in self.catalog.items():
            if self.is_available(title):
                print(video)

    def list_rented_videos(self):
        """Lists all rented videos, including renter names and due dates."""
        for title, (renter, due_date) in self.rented_videos.items():
            print(f"{self.catalog[title]} - Rented by {renter}, Due: {due_date}")

inventory = VideoInventory()
# ... Add videos using the VideoCatalogEntry class from the previous response
my_video = VideoCatalogEntry("The Shawshank Redemption", "Frank Darabont", 1994, "Drama", "Blu-ray", 142)
inventory.add_video(my_video)
inventory.rent_video("The Shawshank Redemption", "Alice")
inventory.list_available_videos()
inventory.list_rented_videos()