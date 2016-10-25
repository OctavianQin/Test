import sys, getopt
from PIL import Image
from numpy import array, zeros

def main(argv):
   """create a black (all 0) zone in an image, usage: python create_zone.py -i <image> -x1 <top_left_x> -y1 <top_left_y> -x2 <bottom_right_x> -y2 <bottom_right_y>"""
   x1 = 0
   y1 = 0
   x2 = 0
   y2 = 0
   input_image = ''
   try:
      opts, args = getopt.getopt(argv,"i:x1:y1:x2:y2")
   except getopt.GetoptError:
      print('image_transparent.py -w <width> -h <height>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-x1"):
         x1 = int(arg)
      elif opt in ("-y1"):
         y1 = int(arg)
      elif opt in ("-x2"):
         x2 = int(arg)
      elif opt in ("-y2"):
         y2 = int(arg)
      elif opt in ("-i"):
         input_image = arg

   img = Image.open(input_image)
   img_array = array(img)
   img_array[y1:y2, x1:x2, 0:3] = 0
   img = Image.fromarray(img_array)
   img.save('out.png')

if __name__ == "__main__":
   main(sys.argv[1:])