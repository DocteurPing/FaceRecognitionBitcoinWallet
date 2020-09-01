import sys
import os
import dlib
import glob

predictor_path = sys.argv[1]
face_rec_model_path = sys.argv[2]
faces_folder_path = sys.argv[3]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

#win = dlib.image_window()
first = 0
# Now process all the images
for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = dlib.load_rgb_image(f)
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        if first != 0:
            for i in face_descriptor:
                print(i)
            print(face_descriptor)
        prev_face = face_descriptor
        first = 1
        face_chip = dlib.get_face_chip(img, shape)        

        face_descriptor_from_prealigned_image = facerec.compute_face_descriptor(face_chip)
