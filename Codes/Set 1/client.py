
import socket, cv2, pickle, struct

#create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostip = '127.0.0.1'
port = 9999
client_socket.connect((hostip, port))
data = b""
payload_size = struct.calcsize("Q")
while True:
	while len(data)<payload_size:
		packet = client_socket.recv(4*1024)
		if not packet: break
		data = data + packet
		print("ok")
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q", packed_msg_size)[0]

	while len(data)<msg_size:
		data = data + client_socket.recv(4*1024)
	frame_data = data[:msg_size]
	data = data[msg_size]
	frame = pickle.loads(frame_data)
	cv2.imshow("Received", frame)
	key = cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break
client_socket.close()
