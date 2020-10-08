import numpy as np
import random
import os

class FileWriter():

    def writeObjectFile(self,vertice_list,face_list):
        ''' this method writes the object file for each of the individual labels'''

        for label in range(len (vertice_list)):
            filepath = "./simple_obj_label"+str(label)+".obj"

            with open(filepath, 'w') as f:
                f.write("# OBJ file\n")
                f.write("mtllib file.mtl\n")
                #iterate over the sub list of vertices in vertice_list
                for v in vertice_list[label] :
                    print
                    f.write("v ")
                    f.write( ' '.join(map(str, v)) )
                    f.write("\n")
                f.write("\n")
                f.write("usemtl mat"+str(label)+"\n")
                #iterate over the sub list of faces in face_list
                for p in face_list[label]:
                    f.write("f " )
                    f.write( ' '.join(map(str, p)))
                    f.write("\n")
    
    def writeMaterialFile(self,actualLabels):
        '''This method write the material file for each label'''
        filepath = "./file.mtl"
        
        with open(filepath, 'w') as f:
            for label in range(actualLabels):
                #Generate 3 random number for RGB values in each materials between 0 to 1
                RGBlist = np.random.uniform(1,0,3)
                f.write("newmtl mat"+str(label)+"\nNs 100.0 \nd 1.0\nillum 2\n")
                f.write("Kd ")
                #iterate over rgb list
                for i in range(len(RGBlist)) :
                    f.write( " "+str(RGBlist[i]))
                f.write("\nKa 1.0 1.0 1.0\n")
                f.write("Ks 1.0 1.0 1.0")
                f.write("\n\n")
