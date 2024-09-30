import cv2
import face_recognition
import numpy as np

# Load known faces
known_face_encodings = []
known_face_names = []

# Load images and encode faces
try:
    known_person1_image = face_recognition.load_image_file("person1.jpg")
    known_person2_image = face_recognition.load_image_file("person2.jpg")
    known_person3_image = face_recognition.load_image_file("person3.jpg")

    known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
    known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
    known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

    known_face_encodings.append(known_person1_encoding)
    known_face_encodings.append(known_person2_encoding)
    known_face_encodings.append(known_person3_encoding)

    known_face_names.append("person1")
    known_face_names.append("person2")
    known_face_names.append("person3")
except Exception as e:
    print(f"Error loading images: {e}")

# Initialize webcam
video_capture = cv2.VideoCapture(1)

def detect_faces(frame):
    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    return frame

# Display the video stream
while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture image from camera.")
        break

    frame = detect_faces(frame)

    # Show the frame in a window
    cv2.imshow('Video Stream', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
