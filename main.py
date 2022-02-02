import wx

class MyFrame(wx.Frame):  # создаем класс, наследующий свойства класса wx.Frame
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(
        400, 600))
        panel = wx.Panel(self)  # делаем панель

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(15)
        panel.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.txtCtrl = wx.ComboBox(panel)  # создаем поле ввода

        vbox.Add(self.txtCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        gbox = wx.GridSizer(5, 4, 5, 5)  # делаем новый сайзер
        # создаем кнопки внутри нового сайзера
        gbox.AddMany([(wx.Button(panel, label='C'), wx.ID_ANY, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='Close'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='7'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='8'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='9'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='/'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='4'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='5'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='6'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='*'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='1'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='2'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='3'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='-'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='0'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='.'), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='='), wx.ID_ANY, wx.EXPAND),
                      (wx.Button(panel, label='+'), wx.ID_ANY, wx.EXPAND)])
        # добавляем новый сайзер в вертикальный сайзер vbox
        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnClicked)  # связываем кнопки c функцией

    # делаем функцию, которая будет выполнятся при нажатии на кнопки
    def OnClicked(self, evt):
        label = evt.GetEventObject().GetLabel()  # создаем переменную, которая хранит нажатые кнопки

        if label == '=':
            compute = self.txtCtrl.GetValue()
            # игнорируем пустой ввод
            if not compute.strip():
                return

            result = eval(compute)
            self.txtCtrl.Insert(compute, 0)  # добавляем в историю наши расчеты
            self.txtCtrl.SetValue(str(result))  # показываем

        elif label == 'C':
            self.txtCtrl.SetValue("")
        elif label == 'Close':
            frame.Destroy()
        else:
            self.txtCtrl.SetValue(self.txtCtrl.GetValue() + label)



app = wx.App()
frame = MyFrame(None, 'Калькулятор на WX')
frame.Show()
app.MainLoop()