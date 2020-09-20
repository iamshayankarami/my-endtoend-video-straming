import socket, select, pickle, cv2, sys

camera = cv2.VideoCapture(sys.argv[1])
check_data=[]
while True:
    ret, frame = camera.read()
    cv2.imshow('test', frame)
    check_data.append(frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        with open('test.pickle', 'wb') as R:
            pickle.dump(check_data, R, protocol=pickle.HIGHEST_PROTOCOL)
        break
camera.release()
cv2.distroyAllWindows()
