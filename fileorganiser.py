import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView

class FileOrganizerGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        
        self.label = Label(text="Select a folder to organize", size_hint=(1, 0.1))
        self.add_widget(self.label)

        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)

        self.organize_button = Button(text="Organize Files", size_hint=(1, 0.1))
        self.organize_button.bind(on_press=self.organize_files)
        self.add_widget(self.organize_button)

    def organize_files(self, instance):
        folder_path = self.file_chooser.path
        if folder_path:
            self.label.text = f"Organizing: {folder_path}"
            self.organize_logic(folder_path)
            self.label.text = "Organization Complete!"

    def organize_logic(self, folder_path):
        extensions_map = {
            "Documents": [".pdf", ".docx", ".txt"],
            "Images": [".jpg", ".png", ".gif"],
            "Videos": [".mp4", ".avi"],
            "Music": [".mp3", ".wav"],
            "Programs": [".exe", ".msi"]
        }

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()
                for category, extensions in extensions_map.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder_path, category)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_folder, file))

class FileOrganizerApp(App):
    def build(self):
        return FileOrganizerGUI()

if __name__ == "__main__":
    FileOrganizerApp().run()
