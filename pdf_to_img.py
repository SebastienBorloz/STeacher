import pymupdf



doc_name = "An_sol"
doc = pymupdf.open(f"./exercise_resolution_dataset/{doc_name}.pdf")



for i in range(len(doc)):
	pix = doc[i].get_pixmap().pil_image()
	pix.save(f"./exercise_resolution_dataset/{doc_name}/page-{i+1}.png")