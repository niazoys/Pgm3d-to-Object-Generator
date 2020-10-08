import numpy as np
class DrawFaces():

    def check_neighbors_add_face(self,data,label):
        verticeList=[]
        faceList=[]

        ## Loop over 3 dimension
        for z in range(data.shape[2]):
            for y in range(data.shape[1]):
                for x in range(data.shape[0]):
                    # Go for specific label voxel to create separat set of vertice and faces for each label
                    if label==data[x,y,z]:
                        #check if the neighbor exists in positive x direction
                        if x+1<=data.shape[0]-1:
                            #check if the labels are same or not
                            if data[x+1,y,z]!=data[x,y,z]:
                                verticeList.append([x+1,y,z])
                                verticeList.append([x+1,y,z+1])
                                verticeList.append([x+1,y+1,z+1])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x+1,y+1,z])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)])

                        #check if the neighbor exists in negative x direction           
                        if x-1>=0:
                             #check if the labels are same or not
                            if data[x-1,y,z]!=data[x,y,z]:
                                verticeList.append([x,y,z])
                                verticeList.append([x,y+1,z])
                                verticeList.append([x,y+1,z+1])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x,y,z+1])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)]) 
                        
                        #check if the neighbor exists in positive y direction
                        if y+1<=data.shape[1]-1:
                             #check if the labels are same or not
                            if data[x,y+1,z]!=data[x,y,z]:
                                verticeList.append([x,y+1,z])
                                verticeList.append([x+1,y+1,z])
                                verticeList.append([x+1,y+1,z+1])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x,y+1,z+1])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)])    
                        
                        #check if the neighbor exists in negative y direction
                        if y-1>=0:
                             #check if the labels are same or not
                            if data[x,y-1,z]!=data[x,y,z]:
                                verticeList.append([x,y,z])
                                verticeList.append([x,y,z+1])
                                verticeList.append([x+1,y,z+1])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x+1,y,z])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)])
                        
                        #check if the neighbor exists in positive z direction
                        if z+1<=data.shape[2]-1:
                             #check if the labels are same or not
                            if data[x,y,z+1]!=data[x,y,z]:
                                verticeList.append([x,y,z+1])
                                verticeList.append([x,y+1,z+1])
                                verticeList.append([x+1,y+1,z+1])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x+1,y,z+1])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)])  
                      
                        #check if the neighbor exists in negative z direction
                        if z-1>=0:
                             #check if the labels are same or not
                            if data[x,y,z-1]!=data[x,y,z]:
                                verticeList.append([x,y,z])
                                verticeList.append([x,y+1,z])
                                verticeList.append([x+1,y+1,z])
                                faceList.append([len(verticeList)-2,len(verticeList)-1,len(verticeList)])
                                verticeList.append([x+1,y,z])
                                faceList.append([len(verticeList)-3,len(verticeList)-1,len(verticeList)])
    
        return verticeList,faceList
    
    def encodeDataWithLabels (self,data,labels):
        '''This method encodes the labels in place of voxel values'''
        bins = np.linspace(1, 255, labels+1)
        bins=bins.astype('int')
        # Do binning of the data
        data=np.digitize(data,bins,right=False)
        #take out the uniqe labels
        labelsWithData=np.unique(data)
        return data,labelsWithData
