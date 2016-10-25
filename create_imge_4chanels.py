import sys, getopt
from PIL import Image
from numpy import array, zeros

def main(argv):
   """create a white (all 255) 4 channel image, usage: python image_transparent.py -w <width> -h <height>"""
   w = 0
   h = 0
   try:
      opts, args = getopt.getopt(argv,"w:h:",["width=","height="])
   except getopt.GetoptError:
      print('image_transparent.py -w <width> -h <height>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-w", "--width"):
         w = int(arg)
      elif opt in ("-h", "--height"):
         h = int(arg)

   img_array = zeros((h,w,4), 'uint8')
   img_array[:, :, 0:3] = 255
   img_array[:,:,3] = 10
   img = Image.fromarray(img_array)
   img.save('out.png')

if __name__ == "__main__":
   main(sys.argv[1:])