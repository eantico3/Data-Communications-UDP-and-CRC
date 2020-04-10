# UDP-and-CRC
Using UDP protocol, a forwarder is created to send a message from client to server, along with a CRC code.

After creating the forwarder and successfully sending a message from the client to the server along with the CRC code, 
a 40% probability is established within the forwarder that it will change the message before sending it along to the server.
Once the message is sent, the server checks if the forwarder changed the original message.
