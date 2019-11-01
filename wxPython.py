import wx

class myApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt = True)

        # init frame
        self.InitFrame()

    def InitFrame(self):
        frame = myFrame(parent = None, title = "My Frame", pos = (100, 100))
        frame.Show()


class myFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent = parent, title = title, pos = pos)
        self.OnInit()

    def OnInit(self):
        panel = myPanel(parent = self)

class myPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)


        startTimeInput = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, id = wx.ID_ANY, pos = (20, 20), name = 'startTimeInput')
        startTimeText = wx.StaticText(self, id = wx.ID_ANY, label = 'Start Time', pos = (135, 24))
        endTimeInput = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, id = wx.ID_ANY, pos= (20, 50))
        endTimeText = wx.StaticText(self, id=wx.ID_ANY, label='End Time', pos=(135, 54))
        # ID_ANY means that we dont care about the id

    # def onInputEnter(self, Evt):
    #     self.

if __name__ == "__main__":
    app = myApp()
    app.MainLoop()




import wx

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

# Initialize wx App
app = wx.App()
app.MainLoop()

# Call Dialog
x = ask(message = 'What is your name?')
print('Your name was', x)
# def create(parent):
#     return Frame1(parent)
#
# [wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1TEXT1,
# ] = [wx.NewId() for _init_ctrls in range(4)]
#
# class Frame1(wx.Frame):
#     def _init_ctrls(self, prnt):
#         # generated method, don't edit
#         wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
#               pos=wx.Point(249, 224), size=wx.Size(683, 445),
#               style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
#         self.SetClientSize(wx.Size(683, 445))
#
#         self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
#               pos=wx.Point(0, 0), size=wx.Size(683, 445),
#               style=wx.TAB_TRAVERSAL)
#
#         self.text1 = wx.TextCtrl(id=wxID_FRAME1TEXT1, name=u'text1',
#               parent=self.panel1, pos=wx.Point(268, 139), size=wx.Size(103, 25),
#               style=0, value=u'enter')
#
#         self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'click',
#               name='button1', parent=self.panel1, pos=wx.Point(279, 272),
#               size=wx.Size(85, 27), style=0)
#         self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
#               id=wxID_FRAME1BUTTON1)
#
#     def __init__(self, parent):
#         self._init_ctrls(parent)
#
#     def OnButton1Button(self, event):
#         event.Skip()
#         var = self.text1.GetValue()
#
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = create(None)
#     frame.Show()
#
#     app.MainLoop()
#     print(var)