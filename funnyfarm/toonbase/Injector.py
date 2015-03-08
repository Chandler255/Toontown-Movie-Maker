def runInjectorCode():
	global text
	exec (text.get(1.0, "end"), globals())

def openInjector():
	print 'INJECTOR ENABLED'
	import Tkinter as tk
	from direct.stdpy import thread
	root = tk.Tk()
	root.geometry('600x400')
	root.title('INJECTOR')
	root.resizable(False,False)
	global text
	frame = tk.Frame(root)
	text = tk.Text(frame,width=70,height=20)
	text.pack(side="left")
	tk.Button(root,text="Inject!",command=runInjectorCode).pack()
	scroll = tk.Scrollbar(frame)
	scroll.pack(fill="y",side="right")
	scroll.config(command=text.yview)
	text.config(yscrollcommand=scroll.set)
	frame.pack(fill="y")
	thread.start_new_thread(root.mainloop,())