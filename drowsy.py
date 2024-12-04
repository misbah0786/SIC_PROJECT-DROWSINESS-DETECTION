import tkinter as tk
from tkinter import ttk
from imutils import face_utils
import dlib
import cv2
from pygame import mixer
def on_button_click():
    label_result.config(text="Button has been clicked")
    thres = 6

    mixer.init()
    sound = mixer.Sound('alarm.mp3')

    dlist = []

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("facial-landmarks-recognition/shape_predictor_68_face_landmarks.dat")

    cap = cv2.VideoCapture(0)

    def dist(a, b):
        x1, y1 = a
        x2, y2 = b
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def draw_alert(frame, message):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, message, (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    while True:
        # Getting out image by webcam
        _, image = cap.read()
        # Converting the image to gray scale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get faces into webcam's image
        rects = detector(gray, 0)

        # For each detected face, find the landmark.
        for (i, rect) in enumerate(rects):
            # Make the prediction and transform it to numpy array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # Draw on our image, all the found coordinate points (x,y)
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

            le_38 = shape[37]
            le_39 = shape[38]
            le_41 = shape[40]
            le_42 = shape[41]

            re_44 = shape[43]
            re_45 = shape[44]
            re_47 = shape[46]
            re_48 = shape[47]

            dlist.append((dist(le_38, le_42) + dist(le_39, le_41) + dist(re_44, re_48) + dist(re_45, re_47)) / 4 < thres)
            if len(dlist) > 10:
                dlist.pop(0)

            # Drowsiness detected
            if sum(dlist) >= 4:
                message_label.config(text="Drowsiness detected! Please take a break.")
                draw_alert(image, "ALERT !!! DROWSINESS DETECTED...")
                try:
                    sound.play()
                except:
                    pass
            else:
                message_label.config(text="")
                try:
                    sound.stop()
                except:
                    pass

        # Show the image
        cv2.imshow("Output", image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    cap.release()

def on_enter(e):
    button_detect.config(style="Hover.TButton")

def on_leave(e):
    button_detect.config(style="TButton")

# Create the main window
root = tk.Tk()
root.title("Drowsiness Detection")
root.geometry("600x400")

# Set a light background color
root.configure(bg='#f0f8ff')

# Create a heading with stylish text
label_heading = tk.Label(root, text="Drowsiness Detection", font=("Helvetica", 24, "bold"), pady=20, bg='#f0f8ff')
label_heading.pack()

# Configure styles for the button
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", font=("Helvetica", 14), background='red', foreground='black')
style.configure("Hover.TButton", padding=6, relief="flat", font=("Helvetica", 14), background='white', foreground='blue')

# Create a button in the middle of the window
button_detect = ttk.Button(root, text="Detect", command=on_button_click, style="TButton")
button_detect.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add hover properties
button_detect.bind("<Enter>", on_enter)
button_detect.bind("<Leave>", on_leave)

# Add a label to display the result of button click
label_result = tk.Label(root, text="", bg='#f0f8ff')
label_result.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Add a text below the button
label_instruction = tk.Label(root, text="Click to detect", bg='#f0f8ff')
label_instruction.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

# Add a message label for drowsiness detection
message_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#f0f8ff')
message_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Ensure the labels are above the background color
label_heading.lift()
button_detect.lift()
label_result.lift()
label_instruction.lift()
message_label.lift()

# Run the application
root.mainloop()
