import socket, cv2, pickle, struct

#create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
print("Host IP: ",hostip)
port = 9999
socket_address = (hostip, port)

#socket bind
server_socket.bind(socket_address)

#listen socket
server_socket.listen(25)
print("Listening at: ",socket_address)

#accept socket
while True:
	client_socket, client_address = server_socket.accept()
	print('Got connection from: ',client_address)
	if client_socket:
		video = cv2.VideoCapture(0)
		while video.isOpened():
			_, frame  = video.read()
			a = pickle.dumps(frame)
			message = struct.pack("Q", len(a))+a
			client_socket.sendall(message)
			cv2.imshow('Transmitting video', frame)
			key = cv2.waitKey(1) & 0xFF
			if key==ord('q'):
				client_socket.close()
