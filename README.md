# CL-Chatbot
This a chatbot that allows users over the same wireless connection to communicate through their Command Line. This project utilizes socket programming and multi-threading to allow for multiple users to ping the server script at a given time. The Server script uses threading, the sys socket library, and OOP principles to listen and send out all messages while the client script utilizes the same socket library to listen to all messages from the server and to send messages directly to the server.

Necessary tools:
  - Any machine with capability to run Python code
How-To
The server script needs to be run on any given device within the wireless network and the client script must be run on any amount of user machines to create a chatroom experience.

Once the scripts are properly running, clients can type any message into their terminal and it will be sent out to all others on the chatroon network. Once users are finished with the chat room, they can simply enter 'q' to quit the script and run the client script again to re-enter.

NOTE: The IP address must be updated depending on the network the client scripts wil be connected to. You can do this by
  - Go to the Wifi Settings of your machine
  - Locate the Wifi properties
  - take note of the IP v4 address
  - update line 20 of the client Script


At this time, the chat room can only run on the same Internet Connection. Check back soon to see how to use this project to create a communication across different Internet connections! 

Thanks and Enjoy!!!


DISCLAIMER: This project was heavily inspired by and assisted www.thepythoncode.com
