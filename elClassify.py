import tensorflow as tf
import cv2
import os
import time
import numpy as np

class ElClassify():
    def __init__(self, dir, area):
        self.name = 'classify'
        self.pieceFileName = 'E:/pieceImg.jpg'
        

        
        self.pic_width = area.pic_width
        self.pic_height = area.pic_height
        self.pic_top_margin = area.pic_top_margin
        self.pic_right_margin = area.pic_right_margin
        self.pic_buttom_margin = area.pic_buttom_margin
        self.pic_left_margin = area.pic_left_margin
        self.pic_piece_size = area.pic_piece_size
        self.rows = area.rows
        self.cols = area.cols
        self.step_x = int((self.pic_width - self.pic_left_margin - self.pic_right_margin)/self.cols)
        self.step_y = int((self.pic_height - self.pic_top_margin - self.pic_buttom_margin)/self.rows)
        
        #self.initAiType1()
        self.initAiType2()
    
    def initAiType2(self):
        self.work_dir = 'E:/el/'
        
        # init sess 1
        self.graph1_dir = self.work_dir + 'save1/'
        self.meta1 = self.graph1_dir +'model_complete.meta'
        
        self.labels1 = []
        for label in tf.gfile.GFile(self.graph1_dir+'el_labels.txt'):
            self.labels1.append(label.rstrip())
        
        self.graph1 = tf.Graph()
        self.sess1 = tf.Session(graph=self.graph1)
        with self.graph1.as_default():
                #import the model dir
                self.imported_meta1 = tf.train.import_meta_graph(self.meta1)
                self.imported_meta1.restore(self.sess1, tf.train.latest_checkpoint(self.graph1_dir))
                self.x1 = self.graph1.get_operation_by_name("x").outputs[0]
                self.predictions1 = self.graph1.get_operation_by_name("predictions").outputs[0]
                
        # init sess 2
        self.graph2_dir = self.work_dir + 'save2/'
        self.meta2 = self.graph2_dir +'model_complete.meta'
        
        self.labels2 = []
        for label in tf.gfile.GFile(self.graph2_dir+'el_labels.txt'):
            self.labels2.append(label.rstrip())
            
        self.graph2 = tf.Graph()
        self.sess2 = tf.Session(graph=self.graph2)
        with self.graph2.as_default():
                #import the model dir
                self.imported_meta2 = tf.train.import_meta_graph(self.meta2)
                self.imported_meta2.restore(self.sess2, tf.train.latest_checkpoint(self.graph2_dir))
                self.x2 = self.graph2.get_operation_by_name("x").outputs[0]
                self.predictions2 = self.graph2.get_operation_by_name("predictions").outputs[0]
                
    def initAiType1(self):
        self.graph_file1 = dir + 'el_graph_1.pb'
        self.label_file1 = dir+ 'el_labels_1.txt'
        
        self.graph_file2 = dir + 'el_graph_2.pb'
        self.label_file2 = dir+ 'el_labels_2.txt'
        
        self.labels1 = []
        self.labels2 = []
        
        for label in tf.gfile.GFile(self.label_file1):
            self.labels1.append(label.rstrip())

        for label in tf.gfile.GFile(self.label_file2):
            self.labels2.append(label.rstrip())
        
        # session1
        self.graph1 = tf.Graph()
        self.sess1 = tf.Session(graph=self.graph1)
        with self.graph1.as_default():
            with tf.gfile.FastGFile(self.graph_file1, 'rb') as f:
                g_def1 = tf.GraphDef()
                g_def1.ParseFromString(f.read())
                tf.import_graph_def(g_def1, name='')
        
        self.softmax_tensor1 = self.sess1.graph.get_tensor_by_name('final_result:0')
        
        # session2
        self.graph2 = tf.Graph()
        self.sess2 = tf.Session(graph=self.graph2)
        with self.graph2.as_default():
            with tf.gfile.FastGFile(self.graph_file2, 'rb') as f:
                g_def2 = tf.GraphDef()
                g_def2.ParseFromString(f.read())
                tf.import_graph_def(g_def2, name='')
        
        self.softmax_tensor2 = self.sess2.graph.get_tensor_by_name('final_result:0')
        
    def getFilePathNameExt(self, fileName):  
        (filepath,tempfilename) = os.path.split(fileName);  
        (shotname,extension) = os.path.splitext(tempfilename);  
        return filepath,shotname,extension
    
    def wirteImgPieceToFile(self, image, start_x, start_y, size_x, size_y):
        newImg = image[start_y:start_y+size_y, start_x:start_x+size_x]
        newImg_a = cv2.resize(newImg, (299,299), interpolation=cv2.INTER_AREA)
        cv2.imwrite(self.pieceFileName, newImg_a)
        
    def processImgPiece1(self):
        inputImg = tf.gfile.FastGFile(self.pieceFileName, 'rb').read()
        
        # Step1
        predict1 = self.sess1.run(self.softmax_tensor1, {'DecodeJpeg/contents:0': inputImg})
        top1 = predict1[0].argsort()[-len(predict1[0]):][::-1]
        top_label1 = self.labels1[top1[0]]
        index_tmp1 = top_label1.find(' ')
        print("topLabel=%s,index_tmp1=%d"%(top_label1, index_tmp1))
        result = int(top_label1[0:index_tmp1])
        
        if result == 0 or result == 5:
            return result
        
        # Step2
        predict2 = self.sess2.run(self.softmax_tensor2, {'DecodeJpeg/contents:0': inputImg})
        top2 = predict2[0].argsort()[-len(predict2[0]):][::-1]
        top_label2 = self.labels2[top2[0]]
        index_tmp2 = top_label2.find(' ')
        print("topLabe2=%s,index_tmp2=%d"%(top_label2, index_tmp2))
        result = int(top_label2[0:index_tmp2])
        
        return result
    
    def processImgPiece2(self,  input_image):
        result = 0
        input_img = np.asarray([cv2.resize(input_image,(128,128),interpolation=cv2.INTER_CUBIC)])
        # Step1
        predict = self.sess1.run(self.predictions1, {'x:0':input_img})
        label = self.labels1[predict[0]]
        index_tmp = label.find('_')
        print("label_1=%s,index_tmp=%d"%(label, index_tmp))
        result = int(label[0:index_tmp])
        
        if result == 0 or result == 5:
            return result
        
        # Step2
        predict = self.sess2.run(self.predictions2, {'x:0':input_img})
        label = self.labels2[predict[0]]
        index_tmp = label.find('_')
        print("label_2=%s,index_tmp=%d"%(label, index_tmp))
        result = int(label[0:index_tmp])

        return result

    def processFile(self, fileName, result):
        path,shortname,extension = self.getFilePathNameExt(fileName)
        
        if not extension == ".jpg":
            return 0
            
        img_ori = cv2.imread(fileName)
        img_w = img_ori.shape[1]
        img_h = img_ori.shape[0]

        if img_w != (self.pic_width) or img_h != (self.pic_height):
            print("input image is %d*%d, but expected size if %d*%d."%(img_w,img_h,self.pic_width,self.pic_height))
            return
            
        start_x = self.pic_left_margin
        start_y = self.pic_top_margin
        #self.result = np.zeros((self.rows, self.cols))
        
        print("===========process file: %s============"%(fileName))
        start = time.clock()
        for row in range(0, self.rows):
            start_x = self.pic_left_margin
            
            for col in range(0, self.cols):
                '''
                self.wirteImgPieceToFile(img_ori, start_x, start_y, self.step_x, self.step_y)
                piece_result = self.processImgPiece1()
                '''
                image_piece = img_ori[start_y:start_y+self.step_y, start_x:start_x+self.step_x]
                piece_result = self.processImgPiece2(image_piece)
                result[row][col] = piece_result
                start_x += self.step_x
                
            start_y += self.step_y
            
        end = time.clock()
        print ("consumed time=%fs"%(end-start))
        #return self.result
