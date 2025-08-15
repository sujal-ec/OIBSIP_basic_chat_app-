# Text-Based Chat Application

A simple command-line chat application that allows two or more users to exchange messages in real-time using a client-server model built with Python sockets.

## Features

- **Real-time messaging**: Users can send and receive messages instantly.
- **Username support**: Each user can set a unique username for better identification.
- **Message history**: The application stores and displays the history of messages exchanged during the session.
- **Typing indicators**: Get notified when other users are typing (optional implementation).
- **User list**: View currently connected users (optional implementation).
- **Command support**: Users can issue commands like `/quit` to exit the chat (optional implementation).

## Technologies Used

- Python 3.x
- Socket programming
- Threading

## Requirements

- Python 3.x
- `socket` and `threading` modules (included in Python standard library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sujal-ec/OIBSIP_basic_chat_app-/tree/main.git
   ```

2. Navigate to the project directory:

   ```bash
   cd OIBSIP_basic_chat_app.git
   ```

3. Run the server:

   ```bash
   python chat_server.py
   ```

4. Open another terminal to run the client:

   ```bash
   python chat_client.py
   ```

5. Enter a username when prompted, and start chatting!

## Usage

- **To send a message**: Type your message and press Enter.
- **To exit**: Type `exit` and press Enter to leave the chat.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Inspired by the need for real-time communication.
- Thanks to the open-source community for providing valuable resources.

