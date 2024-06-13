

import socket
import json

# Dictionary of popular movies and their ratings
movie_data = {
    "The Shawshank Redemption": 9.3,
    "The Godfather": 9.2,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Schindler's List": 8.9,
    "Pulp Fiction": 8.9
}


def get_movies():
    # Return a list of popular movies and their ratings in a JSON format
    return json.dumps(movie_data)


def get_response(request):
    # Implement the GET protocol
    if request.startswith('GET /movies HTTP/1.1'):
        status = '200 OK'
        headers = 'Content-Type: application/json'
        body = get_movies()
    else:
        status = '404 Not Found'
        headers = 'Content-Type: text/html'
        body = b'<h1>Error 404: Page Not Found</h1>'

    response = f"HTTP/1.1 {status}\r\n{headers}\r\n\r\n{body}"
    return response.encode('utf-8')


def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  # Choose a port number (12345 in this example)
    print(f"Starting server on {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    server_socket.listen()

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        response = get_response(request)
        client_connection.sendall(response)
        client_connection.close()


if __name__ == "__main__":
    main()