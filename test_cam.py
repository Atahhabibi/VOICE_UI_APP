import cv2

for index in [0, 1, 2]:
    print(f"Trying camera index {index}...")
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
    if cap.isOpened():
        print(f"✅ Camera {index} opened successfully")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Can't grab frame")
                break
            cv2.imshow("Test Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()
        break
    else:
        print(f"❌ Camera index {index} not available")
