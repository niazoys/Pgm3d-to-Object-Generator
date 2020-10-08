import os
import numpy as np 
import argparse
from DrawFaces import DrawFaces
from FileWriter import FileWriter
import sys

class MeshGenerator():

    def __init__(self):
        self.verticeList=[]
        self.faceList=[]
        self.faceMaker=DrawFaces()
        
    def readFile(self,filename):
        '''Reads the pgm3d file from directory'''
        with open(filename) as f:
            content = f.readlines()
        return content

    def processData(self,content):
        '''Process data and returns 3d numpy array'''

        #get the file extension
        extension=content[0]

        # get the volume shape
        x,y,z=content[1].split()
        
        #Parse into integer
        X,Y,Z=int(x),int(y),int(z)
        
        #parse the data into numpy array
        data=content[3:]
        data=np.array(data)
        data=list(map(int,data))

        #Reshape data 
        data=np.reshape(data, (X,Y,Z))
        
        return data
    
    def makeFace(self,data,actualLabels):
        '''Make the faces according to labels '''
        for label in (actualLabels):
            v_list,f_list=self.faceMaker.check_neighbors_add_face(data,label)
            self.verticeList.append(v_list)
            self.faceList.append(f_list)

        

def usage():
    print ("Please Give The Inputs in the Following Format * * * <program name.py> -f <File path of pgm3d file > -l <number of labels> * * * |Or check help with * * *<program name.py> -h help * * *")


class LabelValidator(argparse.Action):

    '''Handels the interger range checking'''
    def __call__(self, parser, namespace, values, option_string=None):
        if not 0 < values < 255:
            raise argparse.ArgumentError(self, "Labels needs to be Integer value and should be in range of 2 to 255")
        setattr(namespace, self.dest, values)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="Please Enter the file name with -f  \n" )
    parser.add_argument("-l","--label", help="Please Enter the number of labels with -l \n" ,type=int,action=LabelValidator)
    
    # Read arguments from the command line
    args = parser.parse_args()

    if args.file and args.label:
        
        #Create the mesh generator object
        meshGenerator=MeshGenerator()
        
        #Read the file from the directory
        rawData=meshGenerator.readFile(args.file)

        #Process the raw data into 3d numpy array        
        processedData=meshGenerator.processData(rawData)

        # Encode the labels in the volume data
        encodedData,actualLabels=meshGenerator.faceMaker.encodeDataWithLabels(processedData,args.label)

        # Check the neighbors and make the faces 
        meshGenerator.makeFace(encodedData,actualLabels)

        #create the object for .obj and material file writer 
        writer=FileWriter()

        #write Material file 
        writer.writeMaterialFile(len(actualLabels))

        #Write the .obj files
        writer.writeObjectFile(meshGenerator.verticeList,meshGenerator.faceList)

        print("Successful")

    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()