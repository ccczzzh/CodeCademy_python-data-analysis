class MyDB(AFXDataDialog):

    # My constructor
    def __init__(self):

        # Call base class constructor
        AFXDataDialog.__init__(self, form,  'My Dialog',
            self.OK|self.CANCEL)

        # Add widgets next...