import cv2

def img_resize(in_path, out_path, side_max_length):	
	img = cv2.imread(in_path)
	dim = img.shape[:2]

	big_side = max(dim)
	resized_dim = (int(dim[1]/big_side*side_max_length), int(dim[0]/big_side*side_max_length))

	res = cv2.resize(img, dsize=resized_dim, interpolation=cv2.INTER_CUBIC)
	cv2.imwrite(out_path, res)



# in_p = './images/test2.jpg'
# out_p = "./images/testFunction.jpg"
# side_max = 2048

# img_resize(in_p,out_p,side_max)