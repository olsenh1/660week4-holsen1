# 660week4-holsen1
SWDV-660 – Applied DevOps   
Maryville University, 2019   
Week 4 Assignment: Python Socket Client & Server   
Henrik Olsen (0913075)   


Submission answers:

1.	How many hours do you estimate that you used in completing this assignment?
I probably spent about 6 (maybe 7) hours on the assignment, including testing and debugging and answering these questions. 

2.	What was the most straightforward part of any task for you?
The logical flow of the system was probably most straight forward to me. I understand the concept of having a server running that a client can connect to, to get a response. 
I think all the parts of this assignment were somewhat equally challenging. One part doesn’t work without the other (or at least it’s hard to test if the server works correctly if the client doesn’t). I basically coded both the server and the client and then started the server up trying to connect from the client. When it didn’t work, most times I changed a little in both code files and tried again. So, I feel the parts were equally challenging and thus also equally straight forward. 

3.	Describe the most frustrating technical challenge you encountered, and how you overcame it.
Most frustrating technical challenge was getting the client and the server to communicate initially. I tried a few times and it didn’t seem to work. Then I went with the KISS principle and made it as simple as I could plus added some print statements along the way. Once I figured out how to transfer a string from the client to the server, I added the responses and conditions and then wrapped everything in loops.

4.	What one part, of the technologies used in this task, would you like to learn more about?
I think it was a great assignment and I appreciate the hands-on experience and the figuring-it-out part, as usual. As far as learning more about any specific thing, I would probably refer to the learning module rather than the assignment and point to something like network vulnerabilities and/or malicious attacks (DDoS, Ping-of-Death, etc.). I think the assignment provides us with a good basic understanding of the client/server technology and socket programming in Python.
5.	If you could have one magic piece of documentation that would make this assignment easier, what would it tell you how to do?
I really can’t think of a magic piece of information or documentation I could have benefitted from this week. I looked up the examples referred to in the module and it really didn’t take that long for me to get to work.


NOTE: For good measure, here’s a quick explanation of my programs.
Start the server. I ran my server in Thonny during implementation and debugging because it’s easy to stop it if necessary, in comparison to running it from a command prompt (“.\python server.py” from a command prompt). The server will listen for “requests” on localhost (127.0.0.1) port 9500 and it could look like it is not responding at all.
Start the client in separate command prompt: “.\python client.py” – it will give the user a menu of sorts. Enter whatever in the “command prompt” and it will be sent to the server. Only “Hello” from the client will trigger a “Hi” from the server (as specified in the assignment). Everything else will trigger a “Goodbye” from the server. To exit, enter “0” (zero) in the client “command prompt”. The server will keep running until terminated via Thonny or closing the shell it’s running in. So, if desired, a new client can be opened and it will communicate with the same server already running.

The only known bug at the moment is when running the client without having the server running. If attempting to send some data to the server the client will break with a ConnectionRefusedError, that I am not handling because the assignment states “Advanced error checking isn't required”. 


























