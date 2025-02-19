import cv2
import mediapipe as mp
import tkinter as tk
from tkinter import messagebox
from google.protobuf.json_format import MessageToDict


def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "password":
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(
            static_image_mode=False,
            model_complexity=1,
            min_detection_confidence=0.25,
            min_tracking_confidence=0.25,
            max_num_hands=8,
        )

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            if results.multi_hand_landmarks:
                if len(results.multi_handedness) > 2:
                    cv2.putText(
                        img,
                        "Multiple Hands",
                        (250, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )
                elif len(results.multi_handedness) == 2:
                    cv2.putText(
                        img,
                        "Both Hands",
                        (250, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )
                else:
                    for i in results.multi_handedness:
                        label = MessageToDict(i)["classification"][0]["label"]
                        if label == "Left":
                            cv2.putText(
                                img,
                                label + " Hand",
                                (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9,
                                (0, 255, 0),
                                2,
                            )
                        if label == "Right":
                            cv2.putText(
                                img,
                                label + " Hand",
                                (460, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9,
                                (0, 255, 0),
                                2,
                            )

            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        parent.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


parent = tk.Tk()
parent.title("Login Form")

username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")
password_entry.pack()

login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

parent.mainloop()
