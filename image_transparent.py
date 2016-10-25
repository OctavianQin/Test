import sys, getopt
from PIL import Image
from numpy import array

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('image_transparent.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('image_transparent.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

   img = Image.open(inputfile)
   img_array = array(img)
   img_array[:,:,3] = 0
   img = Image.fromarray(img_array)
   if outputfile!= '':
       img.save(outputfile)
   else:
       img.save(inputfile+'_transparent.png')

if __name__ == "__main__":
   main(sys.argv[1:])