import cv2

img = cv2.imread("PRO_1-4_C116_TemplateDoProjeto-main\solar-system.jpg")
print(img)

cv2.putText(img,
            "Sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (110, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (190, 160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Terra",
            (285, 160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (375, 160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Jupiter",
            (550, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (760, 120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.putText(img,
            "Uranos",
            (945, 120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.putText(img,
            "Netuno",
            (1100, 120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255)
            )

cv2.imshow("Resultado", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)