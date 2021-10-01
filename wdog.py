import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

arq = "autoupdate.py"
src = open(arq).read()
code = compile(src, arq, 'exec')

class ManipuladorDeEventos(FileSystemEventHandler):

  def catch_all_handler(self, event):
    pass

  def on_created(self, event):
    exec(code)
    print(f"Atenção, {event.src_path} foi criado e essa modificação foi atualizada no repositório")
    self.catch_all_handler(event)

  def on_deleted(self, event):
    exec(code)
    print(f"Atenção, {event.src_path} foi deletado e essa modificação foi atualizada no repositório!")
    self.catch_all_handler(event)

  def on_modified(self, event):
    exec(code)
    print(f"Atenção, {event.src_path} foi modificado e essa modificação foi atualizada no repositório")
    self.catch_all_handler(event)

  def on_moved(self, event):
    exec(code)
    print(f"Atenção, someone moved {event.src_path} to {event.dest_path}, e essa modificação foi atualizada no repositório")
    self.catch_all_handler(event)

eventos = ManipuladorDeEventos()

path = "."
go_recursively = True
observador = Observer()
observador.schedule(eventos, path, recursive=go_recursively)

observador.start()
try:
  while True:
      time.sleep(1)
except:
  observador.stop()
observador.join()