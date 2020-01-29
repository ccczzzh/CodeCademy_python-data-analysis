class AFXDataDialog:
    AFXDataDialog(mode, owner, title, actionButtonIds=0,
              opts=DIALOG_NORMAL, x = 0, y = 0, w = 0, h = 0 )
    class GraphicsOptionsDB(AFXDataDialog):
        def __init__(self, form):
            AFXDataDialog.__init__(self, form, 'Graphics Options',
                               self.OK|self.APPLY|self.DEFAULTS|self.CANCEL)
            # Hardware frame
            #
            gb = FXGroupBox(self, 'Hardware',
                            FRAME_GROOVE|LAYOUT_FILL_X)
            hardwareFrame = FXHorizontalFrame(gb,
                                            0, 0,0,0,0, 0,0,0,0)
            FXLabel(hardwareFrame, 'Driver:')
            FXRadioButton(hardwareFrame, 'OpenGL',form.graphicsDriverKw, OPEN_GL.getId())
            FXRadioButton(hardwareFrame, 'X11',form.graphicsDriverKw, X11.getId())
            FXCheckButton(gb, 'Use double buffering',form.doubleBufferingKw)
            displayListBtn = FXCheckButton(gb, 'Use display lists',form.displayListsKw)
            # View Manipulation frame
            #
            gb = FXGroupBox(self, 'View Manipulation',FRAME_GROOVE|LAYOUT_FILL_X)
            hf = FXHorizontalFrame(gb, 0, 0,0,0,0, 0,0,0,0)
            FXLabel(hf, 'Drag mode:')
            FXRadioButton(hf, 'Fast (wireframe)', form.dragModeKw,FAST.getId())
            FXRadioButton(hf, 'As is', form.dragModeKw,AS_IS.getId())
            FXCheckButton(gb, 'Auto-fit after rotations',form.autoFitKw)