import cv2
import pyvirtualcam
import time
import keyboard

class VirtualWebcamFPS:
    def __init__(self, camera_index=0, target_fps=30, width=1280, height=720):
        self.camera_index = camera_index
        self.target_fps = target_fps
        self.width = width
        self.height = height
        self.frame_delay = 1.0 / target_fps
        self.cap = None
        self.is_running = False
        self.show_preview = True
        
    def start(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        
        if not self.cap.isOpened():
            raise Exception(f"Cannot open camera {self.camera_index}")
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        
        actual_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        print(f"Physical webcam: {actual_width}x{actual_height}")
        print(f"Starting virtual webcam at {self.target_fps} FPS...")
        
        self.is_running = True
        
    def set_fps(self, fps):
        self.target_fps = max(1, min(fps, 60))
        self.frame_delay = 1.0 / self.target_fps
        print(f"FPS set to: {self.target_fps}")
    
    def run(self):
        self.start()
        
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to read from camera")
            return
        
        h, w = frame.shape[:2]
        
        with pyvirtualcam.Camera(width=w, height=h, fps=self.target_fps, backend='obs') as cam:
            print(f'Virtual camera started: {cam.device}')
            print(f'Use this camera in Discord/Zoom/etc.')
            print('\nControls:')
            print('  Q - Quit (when preview is on)')
            print('  Ctrl+Q+P - Quit (when preview is off)')
            print('  + or = - Increase FPS by 1')
            print('  - or _ - Decrease FPS by 1')
            print('  P - Toggle preview window')
            
            last_time = time.time()
            fps_counter = 0
            fps_display = 0
            
            while self.is_running:
                frame_start = time.time()
                
                # Check for Ctrl+Q+P combo when preview is off
                if not self.show_preview:
                    if keyboard.is_pressed('ctrl+q+p'):
                        print("\nCtrl+Q+P detected - Quitting...")
                        break
                    if keyboard.is_pressed('ctrl+shift+p'):
                        self.show_preview = True
                        print("Preview enabled")
                
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                fps_counter += 1
                if time.time() - last_time >= 1.0:
                    fps_display = fps_counter
                    fps_counter = 0
                    last_time = time.time()
                
                display_frame = frame.copy()
                cv2.putText(display_frame, f"FPS: {fps_display} (Target: {self.target_fps})", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(display_frame, "Virtual Webcam Active", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                cam.send(frame_rgb)
                
                if self.show_preview:
                    cv2.imshow('Virtual Webcam Controller', display_frame)
                    
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q') or key == ord('Q'):
                        break
                    elif key == ord('+') or key == ord('='):
                        self.set_fps(self.target_fps + 1)
                    elif key == ord('-') or key == ord('_'):
                        self.set_fps(self.target_fps - 1)
                    elif key == ord('p') or key == ord('P'):
                        self.show_preview = not self.show_preview
                        if not self.show_preview:
                            cv2.destroyAllWindows()
                            print("Preview disabled - Press Ctrl+Q+P to quit or Ctrl+Shift+P to show preview")
                
                elapsed = time.time() - frame_start
                if elapsed < self.frame_delay:
                    time.sleep(self.frame_delay - elapsed)
                
                cam.sleep_until_next_frame()
        
        self.stop()
    
    def stop(self):
        self.is_running = False
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        print("\nVirtual webcam stopped")


if __name__ == "__main__":
    print("=" * 60)
    print("Virtual Webcam FPS Controller")
    print("=" * 60)
    
    controller = VirtualWebcamFPS(
        camera_index=0, 
        target_fps=30,
        width=1280,
        height=720
    )
    
    try:
        controller.run()
    except RuntimeError as e:
        print("\n" + "=" * 60)
        print("ERROR: Virtual Camera Not Available")
        print("=" * 60)
        print("\nInstall OBS Studio: https://obsproject.com/download")
        print("Then run this script again.")
        print("\nError details:", str(e))
    except KeyboardInterrupt:
        print("\nStopping...")
        controller.stop()


