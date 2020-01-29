#-*-coding: gb2312-*-
from abaqusConstants import *
from abaqusGui import *
import os


thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

class TestDB(AFXDataDialog):
    [ID_1,ID_2,ID_LAST] = range(AFXDataDialog.ID_LAST,AFXDataDialog.ID_LAST+3)
    
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, '���������ģ�Ͳ���',
                               self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          
        
        tabLbs      = ['���γߴ�','���ϲ���','���ز���']     
        inputLabels = [['��Ƭ���','����뾶','��ͷλ��'],
                       ['����������ģ��','���ɱ�','�ض�','����ϵ��','��ͷ�ն�'],
                       ['�ϲ�ˮ��ѹ��','�²�ˮ��ѹ��','�������1','�������2']]  
        icons  = getIcons('pic')
        #--ҳ�沼��--
        TabBook = FXTabBook(self)                      
        tabs    = addTabs(TabBook,tabLbs)     
        
        for i in range(len(tabLbs)):
            va=AFXVerticalAligner ( tabs[ tabLbs[i]] )
            addTextFields(va,inputLabels[i])
            
        FXButton(tabs['���γߴ�'],'ʾ��ͼ',None,self,self.ID_1)
        FXButton(tabs['���ز���'],'ʾ��ͼ',None,self,self.ID_2)
        FXLabel(self,'��λ����kN-m-kPa��')
     
     #--------��Ϣ��--------------------------------------
        FXMAPFUNCS(self,SEL_COMMAND,self.ID_1,self.ID_2,TestDB.showTip)

        
    def showTip(self,sender,sel,ptr):
        icons  = getIcons('pic')    
        if SELID(sel) == self.ID_1:
            tip = Tips(self,icons['geometry.bmp'])
            tip.create()
            tip.showModal()
        elif SELID(sel) == self.ID_2:
            tip = Tips(self,icons['load.bmp'])
            tip.create()
            tip.showModal()
        return 1      

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):           
        self.resize(self.getDefaultWidth(), self.getDefaultHeight())
        AFXDataDialog.show(self)



class Tips(AFXDialog):    
    def __init__(self,owner,icon):
        AFXDialog.__init__(self,owner, 'ʾ��ͼ')   
        FXLabel(self,'',ic=icon)

#-----------Here are the widgets creation methods

def getIcons(pa):
    fileName = ['geometry.bmp', 'load.bmp']
    icons={}
    for bmp in fileName:        
        fa = '.\\%s\\%s'%(pa,bmp)
        icon = afxCreateBMPIcon(fa)
        icons[bmp] = icon            
    return icons

def addTextFields(p,labels):
   for label in labels:
       AFXTextField ( p, 16, labelText=label)
   return True

def addTabs(p,labels):
   tabs = {}
   for label in labels:
       tb_ld = FXTabItem(p, label)
       tafram1 = FXVerticalFrame(p)
       tabs[label] = tafram1
   return tabs
