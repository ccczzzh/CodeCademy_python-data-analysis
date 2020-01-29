#-*-coding: gb2312-*-
from abaqusConstants import *
from abaqusGui import *
import os


thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

class TestDB(AFXDataDialog):
    [ID_1,ID_2,ID_LAST] = range(AFXDataDialog.ID_LAST,AFXDataDialog.ID_LAST+3)
    
    def __init__(self, form):
        AFXDataDialog.__init__(self, form, '请输入计算模型参数',
                               self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)          
        
        tabLbs      = ['几何尺寸','材料参数','荷载参数']     
        inputLabels = [['管片厚度','计算半径','接头位置'],
                       ['混凝土弹性模量','泊松比','重度','基床系数','接头刚度'],
                       ['上部水土压力','下部水土压力','侧向荷载1','侧向荷载2']]  
        icons  = getIcons('pic')
        #--页面布局--
        TabBook = FXTabBook(self)                      
        tabs    = addTabs(TabBook,tabLbs)     
        
        for i in range(len(tabLbs)):
            va=AFXVerticalAligner ( tabs[ tabLbs[i]] )
            addTextFields(va,inputLabels[i])
            
        FXButton(tabs['几何尺寸'],'示意图',None,self,self.ID_1)
        FXButton(tabs['荷载参数'],'示意图',None,self,self.ID_2)
        FXLabel(self,'单位采用kN-m-kPa制')
     
     #--------消息绑定--------------------------------------
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
        AFXDialog.__init__(self,owner, '示意图')   
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
