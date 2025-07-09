from facenet_pytorch import InceptionResnetV1

facenet = InceptionResnetV1(pretrained='vggface2').eval() 