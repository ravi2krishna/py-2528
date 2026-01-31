# LMS Application (For Watching Course Videos)

# Student       ->  Watch Videos

# VideoAdmin    ->  Watch Videos, Add Videos

# SuperAdmin    ->  Watch Videos, Add Videos & Delete Videos

class Student:
    # Watch Videos 
    def watch_videos(self):
       print("=" * 50) 
       print("Functionality For Watching Video")
       print("W")
       print("a")
       print("t")
       print("c")
       print("h")
       print("i")
       print("n")
       print("g")
       print("v")
       print("i")
       print("d")
       print("e")
       print("o")
       print(".")
       print(".")
       print(".")
       print("=" * 50)
       
class VideoAdmin(Student): # VideoAdmin can inherit watch_videos from Student
    # Add Videos 
    def add_videos(self):
       print("=" * 50) 
       print("Functionality For Adding Video")
       print("A")
       print("d")
       print("d")
       print("i")
       print("n")
       print("g")
       print("v")
       print("i")
       print("d")
       print("e")
       print("o")
       print(".")
       print(".")
       print(".")
       print("=" * 50)
       
class SuperAdmin(VideoAdmin): # SuperAdmin can inherit watch_videos & add_videos from VideoAdmin
   # Delete Videos 
    def del_videos(self):
       print("=" * 50) 
       print("Functionality For Deleting Video")
       print("D")
       print("e")
       print("l")
       print("e")
       print("t")
       print("i")
       print("n")
       print("g")
       print("v")
       print("i")
       print("d")
       print("e")
       print("o")
       print(".")
       print(".")
       print(".")
       print("=" * 50)
       
print("Student User")
student_user = Student()
student_user.watch_videos()

print("Video Admin User")
video_admin_user = VideoAdmin()
video_admin_user.watch_videos()
video_admin_user.add_videos()

print("Super Admin User")
super_admin_user = SuperAdmin()
super_admin_user.watch_videos()
super_admin_user.add_videos()
super_admin_user.del_videos()
